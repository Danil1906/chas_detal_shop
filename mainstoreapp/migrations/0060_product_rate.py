# Generated by Django 3.2.9 on 2022-05-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0059_product_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.IntegerField(default=5, verbose_name='Суммарный рейтинг'),
        ),
    ]
