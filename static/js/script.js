// Tracker Overview

// Bar chart

document.getElementById('income-bar').style.height = '50px';
document.getElementById('expense-bar').style.height = '50px';

let percentage = 50;

const perc1 = document.getElementsByClassName('rotation')[0];

// let str = "";

// for (let i = 0; i < perc1.length; i++) {
// 	console.log(perc1[i]);
// 	str += perc1[i].innerHTML;
// }

let str = "";

for (let i = 0; i < percentage; i++) {
    str += document.getElementById('pie-chart').innerHTML;
}

document.getElementById('pie-chart').innerHTML += str;