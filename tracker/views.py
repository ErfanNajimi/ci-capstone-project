from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
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

def income_delete(request, income_id):
    if request.method == "POST":
        # incomes = Income.objects.all().order_by("-date_added").filter(account=request.user)
        income = get_object_or_404(Income, pk=income_id)

        if income.account == request.user:
            income.delete()
            messages.add_message(request, messages.SUCCESS, 'Income deleted!')
        else:
            messages.add_message(request, messages.ERROR, 'You cannot delete this!')

    return HttpResponseRedirect(reverse('tracker'))