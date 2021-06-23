
import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Student')
    firstname=models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    program_branch= models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    yearofadmission = models.CharField(max_length=50)
    year_of_passing_out = models.CharField(max_length=50)
    hobbies =  models.CharField(max_length=50,default="")
    tech_known =  models.CharField(max_length=50,default="")
    internships =  models.CharField(max_length=50,default="")
    About_you= models.CharField(max_length=150,default="")
    status = models.CharField(max_length=20, default="0")
    avatar = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def _str_(self):
        return self.user.username

class Alumni(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Alumni')
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    official_id = models.CharField(max_length=50)
    year_of_passout= models.CharField(max_length=50)
    Current_job = models.CharField(max_length=50)
    Branch_in_undergrad = models.CharField(max_length=50)
    college_gpa = models.CharField(max_length=50)
    Examination_taken = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=50, default="")
    tech_known = models.CharField(max_length=50, default="")
    internships = models.CharField(max_length=50, default="")
    Job_Sector = models.CharField(max_length=50)
    Previous_company = models.CharField(max_length=50)
    current_company = models.CharField(max_length=50)
    years_of_experience= models.CharField(max_length=50)
    About_you = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default="1")
    noofviews = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def _str_(self):
        return self.user.username

class Questions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Questions')
    question=models.CharField(max_length=50)

    def _str_(self):
        return self.user.username

class Answers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Answers')
    answer=models.CharField(max_length=50)

    def _str_(self):
        return self.user.username

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Chat')
    message=models.TextField()
    created_date = models.DateTimeField(default=now)

class Blog(models.Model):

    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='blogs/pdfs/')

    def __str__(self):
        return self.title