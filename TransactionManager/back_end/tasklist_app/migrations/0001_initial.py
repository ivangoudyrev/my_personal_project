# Generated by Django 4.2.4 on 2023-08-14 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transaction_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tasklist', to='transaction_app.transaction')),
            ],
        ),
    ]
