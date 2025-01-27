# Generated by Django 4.2.18 on 2025-01-27 13:36

from django.db import migrations, models
import taxi.validators


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="license_number",
            field=models.CharField(
                max_length=255,
                unique=True,
                validators=[taxi.validators.LicenseNumberValidator()],
            ),
        ),
    ]
