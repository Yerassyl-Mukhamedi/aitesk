# Generated by Django 2.1.7 on 2019-04-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20190401_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='usage',
            field=models.CharField(max_length=200, null=True, verbose_name='Применение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification1',
            field=models.TextField(blank=True, verbose_name='Общие характеристики'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification2',
            field=models.TextField(blank=True, verbose_name='Программирование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification3',
            field=models.TextField(blank=True, verbose_name='Дополнительная функциональность'),
        ),
    ]