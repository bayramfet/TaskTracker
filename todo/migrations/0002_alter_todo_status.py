# Generated by Django 4.1.5 on 2023-01-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'Completed'), ('P', 'Pending')], default='P', max_length=1),
        ),
    ]