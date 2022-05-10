# Generated by Django 3.2.9 on 2022-01-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0029_remove_promocode_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='discount',
            field=models.IntegerField(blank=True, default=0, help_text='Поле для промокода \n    скидок, обязательно только для промокодов дающие скидку на корзину. Значение которое будет установлено это процент,\n     который скинется пользувателю в общей суммы.', max_length=2, null=True, verbose_name='Скидка в %'),
        ),
    ]
