# Generated by Django 4.2.4 on 2023-08-16 22:33

from django.db import migrations, models
import django.db.models.deletion
import validator.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contactslist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, validators=[validator.validator.validate_name])),
                ('mid_init', models.CharField(blank=True, max_length=255, null=True, validators=[validator.validator.validate_name])),
                ('last_name', models.CharField(max_length=255, validators=[validator.validator.validate_name])),
                ('phone', models.CharField(blank=True, max_length=255, null=True, unique=True, validators=[validator.validator.validate_phone])),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('contactslist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lenders', to='contactslist_app.contactslist')),
            ],
        ),
    ]
