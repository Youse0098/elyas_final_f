# Generated by Django 4.0.3 on 2022-04-18 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0002_remove_grade_slug_grade_created_grade_parent"),
    ]

    operations = [
        migrations.CreateModel(
            name="installment",
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
                ("paid", models.BooleanField(default=False)),
                ("amount", models.IntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="installment",
                        to="student.student",
                    ),
                ),
            ],
        ),
    ]
