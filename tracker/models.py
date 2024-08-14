from django.db import models
from django.contrib.auth.models import User

FREQ = ((0, "Not recurring"), (1, "Monthly"), (3, "Quarterly"), (12, "Annually") )

# Create your models here.
class Income(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")
    source = models.CharField(max_length=120)
    recurring = models.BooleanField(default=False)
    pay_frequency = models.IntegerField(choices=FREQ, default = 0)
    pay_amount = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ["-date_added"]
    
    def __str__(self):
        return f"{self.source}"