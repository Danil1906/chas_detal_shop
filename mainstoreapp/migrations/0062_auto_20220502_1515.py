# Generated by Django 3.2.9 on 2022-05-02 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainstoreapp', '0061_privacypolicy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FixedPost',
        ),
        migrations.AlterModelOptions(
            name='privacypolicy',
            options={'ordering': ['text'], 'verbose_name': 'Политики конфиденциальности', 'verbose_name_plural': 'Политики конфиденциальности'},
        ),
    ]
