# Generated by Django 2.1.3 on 2018-12-07 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_admin_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='phone',
        ),
        migrations.AlterField(
            model_name='admin',
            name='history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.History'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='test',
            field=models.CharField(blank=True, default='test', max_length=10),
        ),
    ]