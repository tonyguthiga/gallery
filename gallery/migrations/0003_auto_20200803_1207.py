# Generated by Django 3.0.8 on 2020-08-03 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200802_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='location',
            new_name='image_location',
        ),
    ]