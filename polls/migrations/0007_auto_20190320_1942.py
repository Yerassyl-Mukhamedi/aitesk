# Generated by Django 2.1.7 on 2019-03-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[('Категория1', ((11, 'Credit Card'), (12, 'Student Loans'), (13, 'Taxes'))), ('Категория2', ((21, 'Books'), (22, 'Games'))), ('Категория3', ((31, 'Groceries'), (32, 'Restaurants')))], default=11),
        ),
    ]
