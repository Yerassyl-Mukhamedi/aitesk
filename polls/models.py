from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, default='category_name')
    slug = models.SlugField(max_length=150, unique=True ,db_index=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    
    sub_category = models.BooleanField(default = True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        unique_together = ('slug', 'parent',) 
        verbose_name_plural = 'categories'

        

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       return reverse('polls:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True, default='product_name')
    slug = models.SlugField(max_length=100, db_index=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 1)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField( default = 1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    image = models.FileField(upload_to='products/%Y/%m/%d', blank=True)

    garant = models.TextField('Гарантия', blank=True)
    specification1 = models.TextField('Общие характеристики',blank=True)
    specification2 = models.TextField('Программирование',blank=True)
    specification3 = models.TextField('Дополнительная функциональность',blank=True)

    pdf = models.FileField(upload_to='products/%Y/%m/%d', blank=True)

    usage = models.TextField('Применение', max_length=200, null=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
       return reverse('polls:product_detail', args=[self.id, self.slug])










# class Product(models.Model):
#     product_name = models.CharField(max_length=200)
#     product_price = models.IntegerField(default=0)
#     product_image = models.ImageField(upload_to="img/polls", blank=True, null=True)
#     product_description = models.CharField(max_length=200, null=True)
#     CATEGORY1 = 'KT1'
#     CATEGORY2 = 'KT2'
#     CATEGORY3 = 'KT3'

#     CATEGORY_CHOICES = (
#         ('Категория1', (
#             (11, 'Credit Card'),
#             (12, 'Student Loans'),
#             (13, 'Taxes'),
#         )),
#         ('Категория2', (
#             (21, 'Books'),
#             (22, 'Games'),
#         )),
#         ('Категория3', (
#             (31, 'Groceries'),
#             (32, 'Restaurants'),
#         )),
#     )


#     category = models.IntegerField(
#         choices = CATEGORY_CHOICES,
#         default = 11,
#     )

#     def __str__(self):
#         return self.product_name
    
#     def image_tag(self):
#         return u'<img src="%s" />'

#     image_tag.short_description = 'Image'
#     image_tag.allow_tags = True



# class SubCategory(models.Model):
#     sub_category_name = models.CharField(max_length=100)
#     parent_category = models.ForeignKey(Product , on_delete=models.CASCADE)

#     sub_category_choices = Product.objects.order_by('id')

#     def __str__(self):
#         return self.sub_category_name
