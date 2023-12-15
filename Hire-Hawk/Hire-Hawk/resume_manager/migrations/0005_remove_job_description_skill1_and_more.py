# Generated by Django 4.2.7 on 2023-12-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "resume_manager",
            "0004_job_description_skill1_job_description_skill2_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job_description",
            name="skill1",
        ),
        migrations.RemoveField(
            model_name="job_description",
            name="skill2",
        ),
        migrations.RemoveField(
            model_name="job_description",
            name="skill3",
        ),
        migrations.AddField(
            model_name="applicant",
            name="rank",
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name="Rank",
        ),
    ]
