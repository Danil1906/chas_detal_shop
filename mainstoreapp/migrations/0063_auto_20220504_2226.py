# Generated by Django 3.2.9 on 2022-05-04 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0062_auto_20220502_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='privacypolicy',
            options={'verbose_name': 'Политики конфиденциальности', 'verbose_name_plural': 'Политики конфиденциальности'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='purchased',
            field=models.JSONField(default={}, verbose_name='Купленные товары'),
        ),
    ]
