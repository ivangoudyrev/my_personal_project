# Generated by Django 4.2.4 on 2023-08-13 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmenu_app', '0006_remove_taskmenu_complete_remove_taskmenu_is_subtask_and_more'),
        ('subtaskmenu_app', '0003_alter_subtaskmenu_connected_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtaskmenu',
            name='connected_task_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtask', to='taskmenu_app.taskmenu'),
        ),
    ]
