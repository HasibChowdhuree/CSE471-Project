# Generated by Django 3.0.4 on 2022-04-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('receiver_name', models.CharField(max_length=100)),
                ('sender_email', models.CharField(max_length=100)),
                ('receiver_email', models.CharField(max_length=100)),
                ('sender_phone', models.CharField(max_length=100)),
                ('receiver_phone', models.CharField(max_length=100)),
                ('sender_address', models.CharField(max_length=100)),
                ('receiver_address', models.CharField(max_length=100)),
            ],
        ),
    ]
