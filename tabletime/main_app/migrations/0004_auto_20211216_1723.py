# Generated by Django 3.2.9 on 2021-12-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20211216_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='occasion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='restaurant',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='restaurant',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
