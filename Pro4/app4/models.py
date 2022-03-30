from ast import Index
from asyncio.windows_events import NULL
from cProfile import label
from enum import auto
from tracemalloc import start
from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    Email = models.EmailField(default=None)
    Display_picture = models.ImageField(upload_to = "images/")

# class category(models.Model):
#     Man = models.CharField(max_length=100)
#     Woman = models.CharField(max_length=100)
#     Kids = models.CharField(max_length=100)
#     Electronics = models.CharField(max_length=100)


# class Employee(models.Model):
#     STANDARD = 'STD'
#     MANAGER = 'MGR'
#     SR_MANAGER = 'SRMGR'
#     PRESIDENT = 'PRES'

#     EMPLOYEE_TYPES = (
#         (STANDARD, 'base employee'),
#         (MANAGER, 'manager'),
#         (SR_MANAGER, 'senior manager'),
#         (PRESIDENT, 'president')
#     )

#     role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     manager = models.ForeignKey('self', null=True, related_name='employee')

#     def __str__(self):
#         return "<Employee: {} {}>".format(self.first_name, self.last_name)

#     def __repr__(self):
#         return self.__str__()

class Category(models.Model):
    MAN = 'man'
    WOMAN = 'woman'
    KIDS = 'kids'
    ELECTRONICS = 'electronics'
    
    CATEGORY_CHOICES = [
    ('Man', (
            ('Man_Footwer', 'Footwer'),
            ('Man_T-shirt', 'T-shirt'),
            ('Man_Kurta', 'Kurta'),
            ('Man_Smart Watches', 'Smart Watches'),
            ('Man_Sports & Fitness Store', 'Sports & Fitness Store'),

        )
    ),
    ('Woman', (
            ('Woman_Footwer', 'Footwer'),
            ('Woman_T-shirt', 'T-shirt'),
            ('Woman_Kurta', 'Kurta'),
            ('Woman_Smart Watches', 'Smart Watches'),
            ('Woman_Sports & Fitness Store', 'Sports & Fitness Store'),

        )
    ),
   ('KId', (
           ('KId_Footwer', 'Footwer'),
            ('KId_T-shirt', 'T-shirt'),
            ('KId_Kurta', 'Kurta'),
            ('KId_Smart Watches', 'Smart Watches'),
            ('KId_Sports & Fitness Store', 'Sports & Fitness Store'),

        )
    ),
    ('Electronic', (
            ('Electronic_Mobiles', 'Mobiles'),
            ('Electronic_Laptops', 'Laptops'),
            ('Electronic_Speakers', 'Speakers'),
            ('Electronic_Smart Home Automation', 'Home Automation'),
            ('Electronic_Network Components', 'Network Components'),
            ('Electronic_Health Care Appliances', 'Health Care Appliances'),

        )
    ),
]

    CATEGORY_TYPES = [
        
        (MAN, 'MAN'),
        (WOMAN, 'WOMAN'),
        (KIDS, 'KIDS'),
        (ELECTRONICS, 'ELECTRONICS')
    ]

    MAN_SUBCATEGORY = 'man_subcategory'
    WOMAN_SUBCATEGORY = 'woman_subcategory'
    KIDS_SUBCATEGORY = 'kids_subcategory'
    ELECTRONICS_SUBCATEGORY = 'electronics_subcategory'

    SUB_CATEGORY_TYPES = [
        
        (MAN_SUBCATEGORY, 'WATCHES'),
        (WOMAN_SUBCATEGORY, 'JEWLRY'),
        (KIDS_SUBCATEGORY, 'TOY'),
        (ELECTRONICS_SUBCATEGORY, 'TELEVISION')
    ]
    
    id = models.AutoField(primary_key=True)
    # id = models.AutoField(primary_key=False)
    category = models.CharField(max_length=100)
    # subcategory = models.(max_length=100)
    P_category_id = models.IntegerField(default='0')
    # sub_category = models.CharField(max_length=100, choices=[],default='select')
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,default='0')
    # category = models.CharField(max_length=100, choices=CATEGORY_TYPES,default='select')
    # sub_category = models.CharField(max_length=100, choices=SUB_CATEGORY_TYPES,default='select')
    # primary = models.ForeignKey('self', null=True, related_name='Category',on_delete=models.CASCADE)

    # def __str__(self):
    #     return "<Category: {} {}>".format(self.category,self.sub_category)

    # def __repr__(self):
    #     return self.__str__()