# Generated by Django 3.2.15 on 2022-10-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("search", "0004_make_total_results_not_null"),
    ]

    operations = [
        migrations.AlterField(
            model_name="searchquery",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]