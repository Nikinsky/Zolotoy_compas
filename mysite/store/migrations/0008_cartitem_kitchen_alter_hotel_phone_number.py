# Generated by Django 5.1.1 on 2024-10-02 17:16

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='kitchen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.kitchen'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG'),
        ),
    ]
