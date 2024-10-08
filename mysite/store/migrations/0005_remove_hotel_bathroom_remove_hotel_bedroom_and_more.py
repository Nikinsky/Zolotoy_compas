# Generated by Django 5.1.1 on 2024-10-07 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_address_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='bathroom',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='bedroom',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='car_bikes',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='offered_amenities',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='pets_allow',
        ),
        migrations.AddField(
            model_name='hotel',
            name='title_name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_conditions', models.CharField(max_length=32)),
                ('icon', models.ImageField(upload_to='icon_conditions/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='store.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Offered_amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_offered', models.CharField(max_length=32)),
                ('icon', models.ImageField(upload_to='icons_offered/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offereds', to='store.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Safety_and_hydigene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_safety', models.CharField(max_length=32)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons_safety/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='safetys', to='store.hotel')),
            ],
        ),
    ]
