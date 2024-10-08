// Tracker Overview

// Bar chart
const totalMonthlyIncome = parseFloat(document.getElementById('total-monthly-income').innerHTML);
const totalMonthlyExpense = parseFloat(document.getElementById('total-monthly-expense').innerHTML);
const totalQuarterlyIncome = parseFloat(document.getElementById('total-quarterly-income').innerHTML);
const totalQuarterlyExpense = parseFloat(document.getElementById('total-quarterly-expense').innerHTML);
const totalAnnuallyIncome = parseFloat(document.getElementById('total-annually-income').innerHTML);
const totalAnnuallyExpense = parseFloat(document.getElementById('total-annually-expense').innerHTML);

let totalIncome = totalMonthlyIncome + (totalQuarterlyIncome / 3) + (totalAnnuallyIncome / 12);
let totalExpense = totalMonthlyExpense + (totalQuarterlyExpense / 3) + (totalAnnuallyExpense / 12);

const greaterAmount = totalIncome > totalExpense ? totalIncome : totalExpense;

document.getElementById('income-bar').style.height = `${(totalIncome / greaterAmount) * 200}px`;
document.getElementById('expense-bar').style.height = `${(totalExpense / greaterAmount) * 200}px`;

document.getElementById('income-bar').innerHTML = `£${Math.round(totalIncome)}`;
document.getElementById('expense-bar').innerHTML = `£${Math.round(totalExpense)}`;