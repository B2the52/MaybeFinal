# Generated by Django 4.2.6 on 2023-12-13 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_service_serv_rev'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='service_id',
        ),
        migrations.RemoveField(
            model_name='service',
            name='serv_rev',
        ),
    ]