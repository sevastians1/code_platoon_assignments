# Generated by Django 4.1.3 on 2022-11-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_img',
            field=models.TextField(blank=True, null=True),
        ),
    ]