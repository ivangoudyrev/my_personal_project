# Generated by Django 4.2.4 on 2023-08-13 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmenu_app', '0003_taskmenu_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmenu',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]