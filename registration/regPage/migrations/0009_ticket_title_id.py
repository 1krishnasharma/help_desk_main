# Generated by Django 3.2.16 on 2022-10-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regPage', '0008_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='title_id',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
