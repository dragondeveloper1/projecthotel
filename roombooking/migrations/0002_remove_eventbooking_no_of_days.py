# Generated by Django 3.1.7 on 2021-12-15 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roombooking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventbooking',
            name='no_of_days',
        ),
    ]