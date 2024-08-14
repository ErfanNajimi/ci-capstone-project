from django.shortcuts import render
from .models import Income, Expense

# Create your views here.
def tracker(request):

    incomes = Income.objects.all().order_by("-date_added")
    expenses = Expense.objects.all().order_by("-date_added")

    return render(
        request,
        'tracker/tracker.html',
        {
            "expenses": expenses,
            "incomes": incomes,
        },
    )