from django.db import models

# Create your models here.


class Designer(models.Model):
    job_id = models.IntegerField()
    income = models.TextField()
    company_name = models.TextField()
    location =  models.TextField()
    services = models.TextField()
    email_address = models.EmailField()

    def __str__(self):
        return str(self.job_id)


class Manager(models.Model):
    job_id = models.IntegerField()
    income = models.TextField()
    company_name = models.TextField()
    services = models.TextField()
    location = models.TextField()
    email_address = models.EmailField()

    def __str__(self):
        return str(self.job_id)

class Accountant(models.Model):

    job_id = models.IntegerField()
    income = models.TextField()
    company_name = models.TextField()
    services = models.TextField()
    location = models.TextField()
    email_address = models.EmailField()
    def __str__(self):

        return str(self.job_id)

class Other(models.Model):
    job_id = models.IntegerField()
    income = models.TextField()
    company_name = models.TextField()
    services = models.TextField()
    description = models.TextField()
    location = models.TextField()
    email_address = models.EmailField()

    def __str__(self):
        return str(self.job_id)


class SoftwareEngineer(models.Model):
    
    job_id = models.IntegerField()
    income = models.TextField()
    company_name = models.TextField()
    services = models.TextField()
    location = models.TextField()
    email_address = models.EmailField()
    def __str__(self):
        return str(self.job_id)



class WebDesigner(models.Model):
    
    job_id = models.IntegerField()
    income = models.TextField()
    company_name = models.TextField()
    services = models.TextField()
    location = models.TextField()
    email_address = models.EmailField()
    def __str__(self):

        return str(self.job_id)