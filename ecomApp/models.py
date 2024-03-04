from django.db import models

# Create your models here.

class wrk(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    # image=models.ImageField(upload_to='image/',blank=False)
    def __str__(self):
        return str(self.name)


class userfeedback(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    msg=models.TextField()
    def __str__(self):
        return str(self.email)