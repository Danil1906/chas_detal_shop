# Generated by Django 3.2.9 on 2022-05-09 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0078_order_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_date_order',
            field=models.DateTimeField(default=datetime.datetime(1111, 1, 1, 1, 1, 1), verbose_name='Дата последнего заказа'),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_orders',
            field=models.IntegerField(default=0, verbose_name='Общее количество заказов'),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_sum',
            field=models.IntegerField(default=0, verbose_name='Общая сумма заказов за все время'),
        ),
        migrations.AlterField(
            model_name='product',
            name='notify_list',
            field=models.JSONField(default=dict, help_text='Тут заносятся email пользователей, которых нужно уведомить о поступлении товара. Это просходит автоматически.', verbose_name='Список уведомлений'),
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.JSONField(default=dict, verbose_name='Отзывы на товар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='purchased',
            field=models.JSONField(blank=True, default=dict, verbose_name='Купленные товары'),
        ),
    ]
