from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    established_at = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    emp_salary = models.BigIntegerField()

    def __str__(self):
        return self.emp_name