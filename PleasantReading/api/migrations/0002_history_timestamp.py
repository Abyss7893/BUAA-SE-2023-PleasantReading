# Generated by Django 4.2 on 2023-05-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="history",
            name="timestamp",
            field=models.DateField(default="2000-01-01"),
            preserve_default=False,
        ),
    ]
