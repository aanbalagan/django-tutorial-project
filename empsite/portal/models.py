from django.db import models

# Create your models here.

class Employee(models.Model):

    emp_name = models.TextField()
    emp_id = models.IntegerField()
    emp_phone = models.IntegerField()
    emp_address = models.CharField(max_length=150)

    def __str__(self):
        return self.emp_name


class Points(models.Model):

    emp_tech = models.IntegerField()
    emp_comm = models.IntegerField()
    emp_fb = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_fb

