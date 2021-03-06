import re

from sqlalchemy import inspect, String
from sqlalchemy.sql.elements import TextClause

from jet_bridge_base.db import get_mapped_base
from jet_bridge_base.models import data_types
from jet_bridge_base.permissions import HasProjectPermissions
from jet_bridge_base.responses.json import JSONResponse
from jet_bridge_base.serializers.model_description import ModelDescriptionSerializer
from jet_bridge_base.utils.common import merge
from jet_bridge_base.utils.db_types import sql_to_map_type, sql_to_db_type
from jet_bridge_base.views.base.api import APIView


def map_column_default(column):
    if column.server_default is not None:
        if hasattr(column.server_default, 'arg') and isinstance(column.server_default.arg, TextClause):
            value = column.server_default.arg.text
            if value.lower() == 'now()':
                return {
                    'default_type': 'datetime_now'
                }
            elif value.lower() == 'true':
                return {
                    'default_type': 'value',
                    'default_value': True
                }
            elif value.lower() == 'false':
                return {
                    'default_type': 'value',
                    'default_value': False
                }

            value_regex = re.search("^'(?P<value>.+)'::(?P<type>.+)$", value)
            if value_regex:
                match = value_regex.groupdict()
                return {
                    'default_type': 'value',
                    'default_value': match['value']
                }

            nextval_regex = re.search("^nextval\((?P<value>.+)\)$", value)
            if nextval_regex:
                match = nextval_regex.groupdict()
                return {
                    'default_type': 'sequence',
                    'default_value': match['value']
                }


def map_column(column, editable):
    params = {}

    try:
        map_type = sql_to_map_type(column.type)
    except:
        map_type = 'NullType'

    try:
        db_type = sql_to_db_type(column.type)
    except:
        db_type = 'NullType'

    if column.foreign_keys:
        foreign_key = next(iter(column.foreign_keys))
        map_type = data_types.FOREIGN_KEY
        params['related_model'] = {
            'model': foreign_key.column.table.name
        }

        table_primary_keys = foreign_key.column.table.primary_key.columns.keys()
        table_primary_key = table_primary_keys[0] if len(table_primary_keys) > 0 else None

        if not table_primary_key or foreign_key.column.name != table_primary_key:
            params['custom_primary_key'] = foreign_key.column.name

    if isinstance(column.type, String):
        params['length'] = column.type.length

    optional = column.autoincrement or column.default or column.server_default or column.nullable

    result = {
        'name': column.name,
        'db_column': column.name,
        'field': map_type,
        'db_field': db_type,
        'filterable': True,
        'required': not optional,
        'null': column.nullable,
        'editable': editable,
        'params': params
    }

    server_default = map_column_default(column)
    if server_default:
        result['default_type'] = server_default['default_type']
        if 'default_value' in server_default:
            result['default_value'] = server_default['default_value']

    return result


# def map_relation(relation):
#     field = None
#
#     if relation.direction == ONETOMANY:
#         field = 'ManyToOneRel'
#
#     return {
#         'name': relation.key,
#         'related_model': {
#             'model': relation.table.name
#         },
#         'field': field,
#         'related_model_field': relation.primaryjoin.right.name,
#         'through': None
#     }
#
# def table_relations(mapper):
#     return list(map(map_relation, filter(lambda x: x.direction == ONETOMANY and hasattr(x, 'table'), mapper.relationships)))
#
# def table_m2m_relations(mapper):
#     result = []
#     name = mapper.selectable.name
#
#     for relation in mapper.relationships:
#         if relation.direction != ONETOMANY or not hasattr(relation, 'table'):
#             continue
#
#         m2m_relationships = relation.mapper.relationships.values()
#
#         if len(m2m_relationships) != 2:
#             continue
#
#         if len(relation.table.columns) > 5:
#             continue
#
#         self_relationship = m2m_relationships[1] if m2m_relationships[1].table.name == name else \
#         m2m_relationships[0]
#         other_relationship = m2m_relationships[0] if self_relationship == m2m_relationships[1] else \
#         m2m_relationships[1]
#
#         result.append({
#             'name': 'M2M {} {}'.format(self_relationship.table.name, other_relationship.table.name),
#             'related_model': {
#                 'model': other_relationship.table.name
#             },
#             'field': 'ManyToManyField',
#             'related_model_field': self_relationship.table.name,
#             'through': {'model': relation.table.name}
#         })
#
#     return result

def map_table(cls, hidden, non_editable):
    mapper = inspect(cls)
    name = mapper.selectable.name

    from jet_bridge_base.configuration import configuration
    additional = configuration.get_model_description(name)

    result = {
        'model': name,
        'db_table': name,
        'fields': list(map(lambda x: map_column(x, x.name not in non_editable), mapper.columns)),
        'hidden': name in hidden or name in configuration.get_hidden_model_description(),
        # 'relations': table_relations(mapper) + table_m2m_relations(mapper),
        'primary_key_field': mapper.primary_key[0].name
    }

    if additional:
        result = merge(result, additional)

    return result


class ModelDescriptionView(APIView):
    serializer_class = ModelDescriptionSerializer
    permission_classes = (HasProjectPermissions,)

    def get_queryset(self, request):
        non_editable = ['id']
        hidden = ['__jet__token']
        MappedBase = get_mapped_base(request)

        return list(map(lambda x: map_table(x, hidden, non_editable), MappedBase.classes))

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset(request)
        serializer = self.serializer_class(instance=queryset, many=True)
        return JSONResponse(serializer.representation_data)
