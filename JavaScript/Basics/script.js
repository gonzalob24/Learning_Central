// Nameing ruled
// Can't start with numbers or simnbols only
// $ or _
//var firstName = 'John';
//

/*
console.log(firstName); // printing

var lastName = 'Smith';
var age = 28;

var fullAge = true;

console.log(fullAge);

var job; //undefined
console.log(job);

job = 'Teacher';

console.log(job + " Joe " + 3 + 3);

*/

// Variable Mutation and type coercion
/*
//Coercion
var firstName = 'John';
var age = 28;

console.log(firstName + ' ' + age);

var job, isMarries;
job = 'Teacher'
isMarried = false;

console.log(firstName + ' is a ' + age + ' year old ' +  job + '. Is he married? ' + isMarried);



//Mutation


age = 'twenty eight';
job = 'driver';

// alert is a pop up window
alert(firstName + ' is a ' + age + ' year old ' +  job + '. Is he married? ' + isMarried);


var lastName = prompt('What is his last name? ');

console.log(lastName + ' ' + firstName);

*/

/*************
* Basic Operators
*/
/*
var year, yearJohn, yearMark;
now = 2018;
ageJohn = 28;
ageMark = 33;

yearJohn = now - ageJohn;
yearMark = now - ageMark;
console.log(yearJohn / 3);

// Logical operators
var johnOlder = ageJohn < ageMark;
console.log(johnOlder);


// typeof

console.log(typeof(johnOlder));

*/

// Operator precedence

/*
var now = 2020;
var yearJohn = 1989;
var fullAge = 18;

var isFullAge = now - yearJohn >= fullAge;

console.log(isFullAge);

var ageJohn = now - yearJohn;
var ageMark = 35;
var avg = (ageJohn + ageMark) / 2

console.log(avg);

var x, y;
x = y = (3 + 5) * 4 - 6;
console.log(x, y);

 Associativity
 right to left: yield, !, =, ? :, new

 Coding challenge

BMI = mass / height^2

var massJohn = 81;
var heightJohn = 1.34;
var massMark = 67;
var heightMark = 1.45;

var bmiJohn = massJohn / (heightJohn * heightJohn);
var bmiMark = massMark / (heightMark * heightMark);

var lowerBMI = bmiJohn < bmiMark;

console.log('Is John\'s BMI lower than Mark\'s? ' + lowerBMI);

*/

// if else stmts
/*
var firstName = 'John';
var status = 'Single';

if (status == 'married')
{
    console.log(firstName + ' is married');
} else
    {
        console.log(firstName + ' is not married');
    }


var isMarried = true;

if (isMarried)
{
    console.log(firstName + ' is married');
} else
{
    console.log(firstName + ' is not married');
}
*/

// boolean logic

// if else block

/*
var firstName = 'John';
var age = 20;

if (age < 13)
{
    console.log(firstName + ' is a boy.');
} else if (age < 20)
{
    console.log(firstName + ' is a teen.');
} else if (age < 30)
{
    console.log(firstName + ' is a young man.');
} else
{
    console.log(firstName + ' is a man.');
}

*/

//terniary operator or conditional operator

/*
var firstName = 'John';
var age = 16;

age >= 18 ? console.log('Drinks beer') : console.log('Does not drink beer')

var drink = age >= 18 ? 'bear' : 'juice';
console.log(drink);

*/

//Switch stmt

/*
var job = 'Driver';

switch(job)
{
    case 'Teacher':
    case 'Instructor':
        console.log('John teachers kids hot to code');
        break;
    case 'Driver':
        console.log('Drives uber');
        break;
    default:
        console.log('Is a student');
}

var firstName = 'John';
var age = 30;
switch (true)
{
    case age <= 13:
        console.log(firstName + ' is a boy.');
        break;
    case age < 20:
        console.log(firstName + ' is a teen.');
        break;
    case age <= 30:
        console.log(firstName + ' is a young man.');
        break;
    default:
        console.log(firstName + ' is a man.');
}

*/

//Truthy and Falsy values and equality operators

// falsy values: undefined, null, 0, '', NaN
// truthy values: all values that are not falsy

/*
var height;

if (height)
{
    console.log('Variable is defined')
} else
{
    console.log('variable has NOT been defined');
}
 */

var teamJohnAvg = (89 + 120 + 103) / 3;
var teamMikeAvg = (116 + 94 + 123) / 3;
var teamMaryAvg = (97 + 134 + 105) / 3;
//var winner = max(teamJohnAvg, teamMaryAvg, teamMikeAvg);

/*
if (teamJohnAvg > teamMikeAvg && teamJohnAvg > teamMaryAvg)
{
    console.log('Johns team has a higher average');
} else if (teamMikeAvg > teamMaryAvg && teamMikeAvg > teamMaryAvg)
{
    console.log('Mikes team has a higher average');
} else if (teamMaryAvg > teamJohnAvg && teamMaryAvg > teamMikeAvg)
{
    console.log('Marys team has a higher average');
} else if (teamJohnAvg == teamMaryAvg || teamJohnAvg == teamMikeAvg)
{
    console.log('there is a tie');
}

*/

// Functions. Function stmts and expression

function calcAge(birthYear)
{
    return 2020 - birthYear;
}

var ageJohn = calcAge(1986);
console.log(ageJohn);


var whatDoYouDo = function(job, firstName)
{
    switch(job)
    {
        case 'Teacher':
            return firstName + ' teacher kids how to code';
        case 'Driver':
            return firstName + ' is an uber driver';
        case 'Designer':
            return firstName + ' designs clothing';
        default:
            return firstName + ' is rich does not need to work!';
    }
}

console.log(whatDoYouDo('rich', 'John'));

// 03-15-2020 Functions







































