from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to="img/polls", blank=True, null=True)

    CATEGORY1 = 'KT1'
    CATEGORY2 = 'KT2'
    CATEGORY3 = 'KT3'

    CATEGORY_CHOICES = (
        (CATEGORY1, 'Категория1'),
        (CATEGORY2, 'Категория2'),
        (CATEGORY3, 'Категория3'),
    )
    category = models.CharField(
        max_length=100,
        choices = CATEGORY_CHOICES,
        default = CATEGORY1,
    )

    def __str__(self):
        return self.product_name
    
    def image_tag(self):
        return u'<img src="%s" />'

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
