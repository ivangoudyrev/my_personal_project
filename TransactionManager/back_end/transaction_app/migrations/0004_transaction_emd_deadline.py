# Generated by Django 4.2.4 on 2023-08-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_app', '0003_transaction_inspection_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='emd_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
