# Generated by Django 4.1.4 on 2022-12-30 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("all_models", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee", name="phone", field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name="employee", name="salary", field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="teacher", name="phone", field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name="teacher", name="salary", field=models.CharField(max_length=5),
        ),
    ]
