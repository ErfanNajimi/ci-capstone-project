from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm

CATEGORY = {
    0: "Rent", 
    1: "Mortgage Loan", 
    2: "Utilities", 
    3: "Food", 
    4: "Transportation",
    5: "Car Insurance",
    6: "Car Repairs",
    7: "Fuel", 
    8: "Entertainment", 
    9: "Furnishings",
    10: "Home Insurnace",
    11: "Life Insurnace", 
    12: "Retirement", 
    13: "Savings",
    14: "Student Loans",
    15: "Loan", 
    16: "Child Expenses",
    17: "Mobile phone",
    18: "Broadband",
    19: "Other", 
    20: "Blank",
}

# Create your views here.
def overview(request):

    incomes = Income.objects.all().order_by("-date_added").filter(account=request.user)
    expenses = Expense.objects.all().order_by("-date_added").filter(account=request.user)

    if request.method == "POST":
        income_form = IncomeForm(data=request.POST)
        if income_form.is_valid():
            income = income_form.save(commit=False)
            income.account = request.user
            income.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Income source added'
            )

    income_form = IncomeForm()

    if request.method == "POST":
        expense_form = ExpenseForm(data=request.POST)
        if expense_form.is_valid():
            expense = expense_form.save(commit=False)
            expense.account = request.user
            expense.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Expense added'
            )

    expense_form = ExpenseForm()

    return render(
        request,
        'tracker/overview.html',
        {
            "expenses": expenses,
            "incomes": incomes,
            "income_form": income_form,
            "expense_form": expense_form,
        },
    )

def income(request):
    incomes = Income.objects.all().order_by("-date_added").filter(account=request.user)

    return render(
        request,
        'tracker/income.html',
        {
        #     # "expenses": expenses,
            "incomes": incomes,
        #     # "income_form": income_form,
        #     # "expense_form": expense_form,
        },
    )

def expense(request):
    expenses = Expense.objects.all().order_by("-date_added").filter(account=request.user)

    return render(
        request,
        'tracker/expense.html',
        {
            "expenses": expenses,
        #     # "incomes": incomes,
        #     # "income_form": income_form,
        #     # "expense_form": expense_form,
            "category": CATEGORY,
        },
    )
