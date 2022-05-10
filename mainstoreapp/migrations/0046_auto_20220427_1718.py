# Generated by Django 3.2.9 on 2022-04-27 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainstoreapp', '0045_auto_20220427_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='discont',
            new_name='discount',
        ),
        migrations.CreateModel(
            name='Discont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(default=0, verbose_name='скидка')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
    ]
