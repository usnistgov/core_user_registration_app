# Generated by Django 4.2.8 on 2024-03-13 21:06

from django.apps import apps as global_apps
from django.db import migrations


def forwards_func(apps, schema_editor):
    """Initialize the registry.
       Add the user template and configure xslt.

    Returns:

    """
    from core_user_registration_app import discover

    # Initialize registry
    discover.init_registration_app()
    if global_apps.is_installed("django_celery_beat"):
        discover.init_periodic_tasks()


class Migration(migrations.Migration):

    dependencies = [
        ("core_user_registration_app", "0002_template_formats"),
    ]

    operations = [
        migrations.RunPython(forwards_func, migrations.RunPython.noop)
    ]

    if global_apps.is_installed("django_celery_beat"):
        dependencies.append(
            ("django_celery_beat", "0018_improve_crontab_helptext")
        )