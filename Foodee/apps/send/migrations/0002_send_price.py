# Generated by Django 3.0.4 on 2022-04-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='send',
            name='price',
            field=models.CharField(default=100, max_length=100),
        ),
    ]
