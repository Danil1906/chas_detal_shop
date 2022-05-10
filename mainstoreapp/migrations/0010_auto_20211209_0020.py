# Generated by Django 3.2.9 on 2021-12-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0009_product_special_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='special_offer',
            field=models.BooleanField(default=False, help_text='\n    При активации данного поля товар дополнительно попадает в список " спецпредложений ", которые отображются в бургере,\n     из основной категории он не пропадает конечно же.', verbose_name='Спецпрелдожение'),
        ),
    ]
