# Generated by Django 4.2 on 2023-04-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.TextField(),
        ),
    ]
