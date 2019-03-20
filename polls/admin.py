from django.contrib import admin

from .models import Product

admin.site.register(Product)

fields = ( 'image_tag', )
readonly_fields = ('image_tag',)