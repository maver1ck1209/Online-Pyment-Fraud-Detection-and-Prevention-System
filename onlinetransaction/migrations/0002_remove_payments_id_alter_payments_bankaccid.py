# Generated by Django 4.1.7 on 2023-03-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onlinetransaction", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payments",
            name="id",
        ),
        migrations.AlterField(
            model_name="payments",
            name="bankaccid",
            field=models.AutoField(
                default=10000, max_length=10, primary_key=True, serialize=False
            ),
        ),
    ]