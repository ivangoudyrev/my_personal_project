# Generated by Django 4.2.4 on 2023-08-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_app', '0002_alter_transaction_closing_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='inspection_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]