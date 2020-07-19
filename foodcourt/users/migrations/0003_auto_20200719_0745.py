# Generated by Django 3.0.7 on 2020-07-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171227_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Admin'), (10, 'Buyer'), (20, 'Seller')], default=10),
        ),
    ]