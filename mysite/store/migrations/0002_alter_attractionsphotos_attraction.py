# Generated by Django 5.1.1 on 2024-10-05 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractionsphotos',
            name='attraction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attraction_photos', to='store.attractions'),
        ),
    ]
