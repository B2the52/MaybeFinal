# Generated by Django 4.2.6 on 2023-12-13 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_service_serv_rev'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='serv_rev',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='website.review'),
        ),
    ]
