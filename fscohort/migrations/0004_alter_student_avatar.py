# Generated by Django 4.1.5 on 2023-01-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0003_delete_teacher_alter_student_options_student_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='student'),
        ),
    ]
