# Generated by Django 3.2 on 2021-12-08 19:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core_main_app", "0001_initial"),
        ("core_website_app", "0001_initial"),
        ("core_parser_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "core_user_registration_app",
                "permissions": (
                    ("access_register", "Can access register"),
                    ("access_user_data_structure", "Can access user data structure"),
                ),
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="UserTemplateVersionManager",
            fields=[
                (
                    "templateversionmanager_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core_main_app.templateversionmanager",
                    ),
                ),
                ("is_default", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
            bases=("core_main_app.templateversionmanager",),
        ),
        migrations.CreateModel(
            name="UserMetadata",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dict_content", models.JSONField(blank=True, null=True)),
                (
                    "title",
                    models.CharField(
                        max_length=200,
                        validators=[
                            django.core.validators.RegexValidator(
                                code="invalid_title",
                                message="Title must not be empty or only whitespaces",
                                regex=".*\\S.*",
                            )
                        ],
                    ),
                ),
                ("xml_file", models.TextField()),
                (
                    "creation_date",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "last_modification_date",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "last_change_date",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("user_id", models.CharField(max_length=200)),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core_main_app.template",
                    ),
                ),
                (
                    "workspace",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core_main_app.workspace",
                    ),
                ),
            ],
            options={
                "verbose_name": "User metadata",
                "verbose_name_plural": "User metadata",
            },
        ),
        migrations.CreateModel(
            name="UserDataStructure",
            fields=[
                (
                    "datastructure_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core_parser_app.datastructure",
                    ),
                ),
                ("form_string", models.TextField(blank=True)),
                (
                    "data",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core_main_app.data",
                    ),
                ),
            ],
            bases=("core_parser_app.datastructure",),
        ),
        migrations.CreateModel(
            name="AccountRequestMetadata",
            fields=[
                (
                    "accountrequest_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core_website_app.accountrequest",
                    ),
                ),
                (
                    "metadata",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core_user_registration_app.usermetadata",
                    ),
                ),
            ],
            options={
                "verbose_name": "Account request metadata",
                "verbose_name_plural": "Account request metadata",
            },
            bases=("core_website_app.accountrequest",),
        ),
        migrations.AddIndex(
            model_name="usermetadata",
            index=models.Index(
                fields=["title", "last_modification_date", "template", "user_id"],
                name="core_user_r_title_cc1330_idx",
            ),
        ),
    ]
