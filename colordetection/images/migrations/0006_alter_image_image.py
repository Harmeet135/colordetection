# Generated by Django 4.2.2 on 2023-06-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_rename_image_color_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
