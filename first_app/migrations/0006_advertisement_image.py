# Generated by Django 4.2.3 on 2023-08-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='firstProject/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]