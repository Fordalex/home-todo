# Generated by Django 3.0.5 on 2020-04-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20200428_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='colour',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]