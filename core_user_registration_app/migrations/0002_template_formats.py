""" Migrations
"""

# Generated by Django 4.2.3 on 2023-08-15 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core_user_registration_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usermetadata",
            old_name="xml_file",
            new_name="file",
        ),
    ]
