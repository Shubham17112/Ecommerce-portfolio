# Generated by Django 5.1.3 on 2024-12-03 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_popularevent_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='popularevent',
            old_name='city',
            new_name='detail_date',
        ),
    ]
