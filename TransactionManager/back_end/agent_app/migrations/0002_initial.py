# Generated by Django 4.2.4 on 2023-08-28 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent_app', '0001_initial'),
        ('contactslist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='contactslist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='contactslist_app.contactslist'),
        ),
    ]
