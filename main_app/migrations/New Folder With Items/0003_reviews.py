# Generated by Django 3.2.9 on 2021-12-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('star_rating', models.TextField(max_length=100)),
            ],
        ),
    ]