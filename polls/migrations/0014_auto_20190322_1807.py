# Generated by Django 2.1.7 on 2019-03-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20190322_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_choice',
            field=models.CharField(choices=[('cat1', 'Credit Card'), ('cat2', 'Student Loans'), ('cat3', 'Taxes'), ('cat4', 'Books'), ('cat5', 'Games'), ('cat6', 'Groceries')], default='cat1', max_length=50),
        ),
    ]
