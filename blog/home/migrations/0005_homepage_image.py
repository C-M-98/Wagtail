# Generated by Django 5.1.3 on 2024-11-08 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_body'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage'),
        ),
    ]
