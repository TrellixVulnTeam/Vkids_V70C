# Generated by Django 2.1.3 on 2018-12-09 16:50

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0017_auto_20181209_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]