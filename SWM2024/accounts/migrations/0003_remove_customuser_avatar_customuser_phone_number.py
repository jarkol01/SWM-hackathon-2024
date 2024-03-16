# Generated by Django 5.0.1 on 2024-03-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_customuser_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="avatar",
        ),
        migrations.AddField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
