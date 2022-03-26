from django.db import models

class Employee(models.Model):
    #eid=models.CharField(max_length=120,unique=True,primary_key=True)
    employee_name=models.CharField(max_length=120)
    designation=models.CharField(max_length=120)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField()
    image = models.ImageField(upload_to="images", null=True)


    def __str__(self):
        return self.employee_name

#qs=Employees(employee_name='Ann',designation='UI',salary='40000',expirence='4')
