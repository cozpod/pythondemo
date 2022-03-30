from django.db import models

class Category(models.Model): 
    MAN = 'man'
    WOMAN = 'woman'
    KIDS = 'kids'
    ELECTRONICS = 'electronics'
    MAN_SUBCATEGORY = 'man_subcategory'
    WOMAN_SUBCATEGORY = 'woman_subcategory'
    KIDS_SUBCATEGORY = 'kids_subcategory'

    CATEGORY_TYPES = (
        (MAN, 'footwer','Watches','Clothing','Accessories','Perfumes'),
        (WOMAN, 'footwer','Watches','Clothing','Accessories','Perfumes'),
        (KIDS, 'footwer','Watches','Clothing','Accessories','Perfumes'),
        (ELECTRONICS, 'Television','Washing Machine','Kitchen Appliances','Air Conditioners','Refrigerators')
    )

    category = models.CharField(max_length=100, choices=CATEGORY_TYPES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subcategory = models.ForeignKey('self', null=True, related_name='Category')

    def __str__(self):
        return "<Category: {} {}>".format(self.first_name, self.last_name)

    def __repr__(self):
        return self.__str__()