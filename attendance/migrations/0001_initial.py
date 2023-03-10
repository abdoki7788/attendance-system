# Generated by Django 4.1.4 on 2022-12-08 12:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Class",
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
                ("class_id", models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                (
                    "number",
                    models.CharField(max_length=11, verbose_name="Phone Number"),
                ),
                (
                    "class_room",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="attendance.class",
                        verbose_name="Class",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
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
                ("date", models.DateField(default=datetime.datetime.now)),
                (
                    "absents",
                    models.ManyToManyField(
                        related_name="absent_dates", to="attendance.student"
                    ),
                ),
                (
                    "class_room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendances",
                        to="attendance.class",
                    ),
                ),
            ],
        ),
    ]
