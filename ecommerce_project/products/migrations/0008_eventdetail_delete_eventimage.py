# Generated by Django 5.1.3 on 2024-12-04 12:25

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_eventimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='event_details/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='event_details/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='event_details/')),
                ('description', tinymce.models.HTMLField()),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='products.event')),
            ],
        ),
        migrations.DeleteModel(
            name='EventImage',
        ),
    ]
