# Generated by Django 4.2.7 on 2023-11-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume_manager", "0003_job_description_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="job_description",
            name="skill1",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="job_description",
            name="skill2",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="job_description",
            name="skill3",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
