# Generated by Django 3.2.9 on 2022-05-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0060_product_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default=' ', verbose_name='Политика')),
            ],
            options={
                'verbose_name': 'Политики конфиденциальности',
                'verbose_name_plural': 'Политики конфиденциальности',
            },
        ),
    ]
