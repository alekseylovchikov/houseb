# Generated by Django 2.1.5 on 2019-01-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dombrusapp', '0004_auto_20190128_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo_1',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
