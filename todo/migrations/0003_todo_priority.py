# Generated by Django 4.1.5 on 2023-01-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.SmallIntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=2),
        ),
    ]
