# Generated by Django 2.1.7 on 2019-03-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20190319_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
