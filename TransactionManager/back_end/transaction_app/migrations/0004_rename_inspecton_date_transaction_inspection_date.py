# Generated by Django 4.2.4 on 2023-08-13 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_app', '0003_alter_transaction_agent_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='inspecton_date',
            new_name='inspection_date',
        ),
    ]
