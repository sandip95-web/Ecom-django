# Generated by Django 4.2 on 2023-04-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0008_alter_cart_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
