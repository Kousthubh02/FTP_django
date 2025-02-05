# Generated by Django 5.1 on 2024-09-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testingApp', '0002_pdfs'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultancyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=255)),
                ('name_of_project', models.CharField(max_length=255)),
                ('type_of_grant', models.CharField(max_length=255)),
                ('funding_organization', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('CV', models.FileField(upload_to='CVs')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('date_of_joining', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('teacher_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.ImageField(upload_to='uploads/')),
                ('teacher_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('publications', models.FileField(upload_to='pdfs')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=255)),
                ('name_of_project', models.CharField(max_length=255)),
                ('type_of_grant', models.CharField(max_length=255)),
                ('funding_organization', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('semester', models.IntegerField()),
                ('teacher_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Pdfs',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
