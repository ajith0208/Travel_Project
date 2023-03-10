# Generated by Django 4.1.4 on 2022-12-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app2", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=250)),
                ("img", models.ImageField(upload_to="pics")),
                ("description", models.TextField()),
            ],
        ),
    ]
