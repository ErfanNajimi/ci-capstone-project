from django.db import models
from django.contrib.auth.models import User

FREQ = ((0, "Not recurring"), (1, "Monthly"), (3, "Quarterly"), (12, "Annually"), (-1, "Other") )
CATEGORY = (
    (0, "Rent"), 
    (1, "Mortgage Loan"), 
    (2, "Utilities"), 
    (3, "Food"), 
    (4, "Transportation"),
    (5, "Car Insurance"),
    (6, "Car Repairs"),
    (7, "Fuel"), 
    (8, "Entertainment"), 
    (9, "Furnishings"),
    (10, "Home Insurnace"),
    (11, "Life Insurnace"), 
    (12, "Retirement"), 
    (13, "Savings"),
    (14, "Student Loans"),
    (15, "Loan"), 
    (16, "Child Expenses"),
    (17, "Mobile phone"),
    (18, "Broadband"),
    (19, "Other"), 
)

# Create your models here.
class Income(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incomes")
    source = models.CharField(max_length=120)
    recurring = models.BooleanField(default=False)
    freq = models.IntegerField(choices=FREQ, default = 0)
    amount = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ["-date_added"]
    
    def __str__(self):
        return f"{self.source}"

class Expense(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    description = models.CharField(max_length=120)
    category = models.IntegerField(choices=CATEGORY, blank=True)
    recurring = models.BooleanField(default=False)
    freq = models.IntegerField(choices=FREQ, default = 0)
    amount = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ["-date_added"]
    
    def __str__(self):
        return f"{self.description}"