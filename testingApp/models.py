from django.db import models

# total models = 8
    
class CV(models.Model):
    teacher_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=100)
    CV = models.FileField(upload_to='CVs')
    
    def __str__(self):
        return self.teacher_id
    
class Publications(models.Model):
    teacher_id = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    publications = models.FileField(upload_to='publicationss')
    
    def __str__(self):
        return self.teacher_id

class PersonalDetails(models.Model):
    teacher_id = models.CharField(max_length=255,primary_key=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.teacher_id

class Profile(models.Model):
    teacher_id = models.CharField(max_length=255,primary_key=True)
    image_path = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.teacher_id

class Specialization(models.Model):
    teacher_id = models.CharField(max_length=255)
    area = models.CharField(max_length=255)

    def __str__(self):
        return self.teacher_id

class Subject(models.Model):
    teacher_id = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    semester = models.IntegerField()

    def __str__(self):
        return self.teacher_id

class ResearchProject(models.Model):
    teacher_id = models.CharField(max_length=255)
    name_of_project = models.CharField(max_length=255)
    type_of_grant = models.CharField(max_length=255)
    funding_organization = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.teacher_id

class ConsultancyProject(models.Model):
    teacher_id = models.CharField(max_length=255)
    name_of_project = models.CharField(max_length=255)
    type_of_grant = models.CharField(max_length=255)
    funding_organization = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.teacher_id