# Generated by Django 5.0.3 on 2024-05-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="plat",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="plat_images"),
        ),
    ]
