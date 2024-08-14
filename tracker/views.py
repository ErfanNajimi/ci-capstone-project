from django.shortcuts import render
from django.contrib import messages
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm

# Create your views here.
def tracker(request):

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
        'tracker/tracker.html',
        {
            "expenses": expenses,
            "incomes": incomes,
            "income_form": income_form,
            "expense_form": expense_form,
        },
    )