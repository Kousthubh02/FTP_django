# Generated by Django 5.1 on 2024-09-08 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testingApp', '0005_remove_cv_id_alter_cv_teacher_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='teacher_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
