from .models import Income, Expense
from django import forms

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('source', 'amount', 'freq')

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('description', 'amount', 'freq')