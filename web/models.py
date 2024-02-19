from django.db import models
from django.utils import timezone

# Create your models here.
class Graphics_Design(models.Model):
    name=models.CharField(max_length=50)
    course_name=models.CharField(max_length=50)
    course_details=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='media')
    image2=models.ImageField(upload_to='media')

    def __str__(self):
        return self.course_name
    


class Digital_Marketing(models.Model):
    name=models.CharField(max_length=50)
    course_name=models.CharField(max_length=50)
    course_details=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='media')
    image2=models.ImageField(upload_to='media')

    def __str__(self):
        return self.course_name
    


class Writing_Translation(models.Model):
    name=models.CharField(max_length=50)
    course_name=models.CharField(max_length=50)
    course_details=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='media')
    image2=models.ImageField(upload_to='media')

    def __str__(self):
        return self.course_name
    


class Music_Audio(models.Model):
    name=models.CharField(max_length=50)
    course_name=models.CharField(max_length=50)
    course_details=models.TextField()
    price=models.FloatField()
    image=models.ImageField(upload_to='media')
    image2=models.ImageField(upload_to='media')

    def __str__(self):
        return self.course_name
    







class Teachers(models.Model):
    name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    teacher_details=models.TextField()
    teacher_details2=models.TextField()

    def __str__(self):
        return self.name

class SocialAccounts(models.Model):
    teacher = models.OneToOneField(Teachers, on_delete=models.CASCADE, related_name='social_accounts')
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    pinterest = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)

    def __str__(self):
        return f"Social accounts for {self.teacher.name}"




class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.first_name
    



class Blog(models.Model):
    course_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media', blank=True)
    topic = models.CharField(max_length=254)
    subject = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic