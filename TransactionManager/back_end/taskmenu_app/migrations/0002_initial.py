# Generated by Django 4.2.4 on 2023-08-16 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmenu_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmenu',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menutasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
