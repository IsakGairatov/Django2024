# Generated by Django 5.0.3 on 2024-03-09 01:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_alter_busketitems_purch'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='default_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.adress'),
        ),
    ]
