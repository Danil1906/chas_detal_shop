# Generated by Django 3.2.9 on 2022-04-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0047_delete_discont'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='wholesale_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена для оптовика'),
        ),
    ]
