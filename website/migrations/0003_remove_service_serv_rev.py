# Generated by Django 4.2.6 on 2023-12-13 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_service_serv_rev'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='serv_rev',
        ),
    ]
