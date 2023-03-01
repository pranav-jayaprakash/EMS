from django.db import models
from django.contrib.auth.models import User


class LeaveApplicationModel(models.Model):
    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    apply_date = models.DateField(auto_now=False, auto_now_add=True, editable=False)
    nature_of_leave = models.CharField(max_length=250)
    first_day = models.DateField()
    last_day = models.DateField()
    number_of_days = models.IntegerField()
    status = models.CharField(max_length=20, default='pending',
                              choices=(('pending', 'Pending'),('approved', 'Approved'), ('reject', 'Rejected')))

  
    def __str__(self):
        return self.employee
