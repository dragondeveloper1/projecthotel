# Generated by Django 3.1.7 on 2021-12-15 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roominfoapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roombooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roominfoapi.roominfo')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roominfoapi.roomdetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Eventbooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=250)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('no_of_days', models.IntegerField()),
                ('persons', models.IntegerField()),
                ('comment', models.CharField(max_length=1000)),
                ('payment', models.CharField(choices=[('card', 'Card'), ('online', 'Online'), ('cheque', 'Cheque'), ('cash', 'Cash'), ('others', 'Others')], default='card', max_length=25)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roominfoapi.packages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
