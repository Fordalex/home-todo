# Generated by Django 3.0.5 on 2020-04-27 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200427_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
