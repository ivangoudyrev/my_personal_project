# Generated by Django 4.2.4 on 2023-08-18 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent_app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
