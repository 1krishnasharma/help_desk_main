# Generated by Django 4.1.1 on 2022-10-21 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regPage', '0005_activeuser_totalactivetime1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeuser',
            name='TotalActiveTime1',
        ),
    ]
