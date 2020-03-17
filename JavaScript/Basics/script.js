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


var teamJohnAvg = (89 + 120 + 103) / 3;
var teamMikeAvg = (116 + 94 + 123) / 3;
var teamMaryAvg = (97 + 134 + 105) / 3;

*/
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

/*
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

*/

// Arrays
/*
var names = ['John', 'Mark', 'Jane'];
var years = [1990, 1969, 1948];

var john = ['John', 'Smith', 1990, 'Teacher']
john.push('blue') // adds at the end
john.unshift('Mr') //adds to the front
names[names.length] = 'Mary';
console.log(names);
console.log(john);

john.pop() //pop last item

console.log(john);
john.shift();  //removed from the front
console.log(john);

console.log(john.indexOf(1990)); // looks for the element 

*/

// coding challeng tip calculator

/*
var restaurant = [124, 48, 268];

function calcTip(bill)
{
    if (bill < 50)
    {
        return bill * 0.2; 
    }
    else if (bill <= 200)
        {
            return bill * 0.15;
        }
    else 
        {
            return bill * 0.10;
        }
}


var tipAmount = [];
var paidAmount = [];
for (i = 0; i < restaurant.length; i++)
{
    tipAmount.push(calcTip(restaurant[i]));
    paidAmount[i] = tipAmount[i] + restaurant[i];
    
}

console.log(tipAmount);
console.log(paidAmount);


*/

// Objects and methods


/*

// oject literal key value pairs
var john = 
{
    firstName: 'John',
    lastName: 'Smith',
    birthYear: 1990,
    family: ['Jane', 'Mark', 'Bob', 'Emily'],
    job: 'Teacher',
    isMarried: false,
    calcAge: function()
    {
        //return 2018 - this.birthYear;
        this.age = 2018 - this.birthYear;
    }
};


console.log(john);
console.log(john.firstName);  // same dot notation to access elements
var x = 'birthYear';
console.log(john['job']);
console.log(john[x]);

john.job = 'Designer';
console.log(john['job']);

//john.isMarried = true;
//console.log(john);

var jane = new Object();
jane.name ='Jane';
jane.birthYear = 1969;
jane['lastName'] = 'Smith';
jane.job = 'Doctor';

console.log(jane);



// atach functions to objects

console.log(john.calcAge(1990));

//john.age = john.calcAge();
john.calcAge();
console.log(john);


//Coding challenge

var johnInfo =
{
    fullName: 'John Smith',
    mass: 80,
    height: 1.57,
    calcBmi: function()
    {
        this.bmi = this.mass / (this.height * this.height);
        // I can also return the BMI to assign it to a variable instead of assigning it
        // to the object as an element
    }
};

var markInfo =
{
    fullName: 'Mark Smith',
    mass: 67,
    height: 1.65,
    calcBmi: function()
    {
        this.bmi = this.mass / (this.height * this.height);
    }
};


console.log(johnInfo);
console.log(markInfo);
johnInfo.calcBmi()
console.log(johnInfo.fullName + '\'s BMI is ' + johnInfo.bmi);

*/

// LOOPS

/*
for (i = 0; i < 10; i++)
{
    console.log(i + 1);
}

var john = ['John', 'Smith', 1990, 'Designer', false];

for (i = 0; i < john.length; i++)
{
    if (typeof john[i] !== 'string') break;
    console.log(john[i]);
}

var i = 0;
while (i < john.length)
{
    if (typeof john[i] !== 'string') continue;
    console.log(john[i]);
    i++;
}


// Continue and break statements

for (i = john.length - 1; i >= 0; i--)
{
    console.log(john[i]);
}

*/



// Tip Calulator challenge

/*
var restaurantBills = [124, 48, 268, 180, 42];

var tipCalculator =
{
    tipAmount: function(bills)
    {
        this.tips = [];
        this.totalPaid = [];
        for (i = 0; i < bills.length; i++)
        {
            
            if (bills[i] < 50)
            {
                this.tips[i] = bills[i] * 0.2;
            } 
            else if (bills[i] <= 200)
                {
                    this.tips[i] = bills[i] * 0.15;    
                }
            else
                {
                   this.tips[i] = bills[i] * 0.10; 
                }
            this.totalPaid[i] = this.tips[i] + bills[i];
        }
    },
//    total: function(bills)
//    {
//        this.totalPaid = [];
//        for (i = 0; i < this.tips.length; i++)
//        {
//            this.totalPaid[i] = this.tips[i] + bills[i];
//        }
//    }
};

tipCalculator.tipAmount(restaurantBills);
//tipCalculator.total(restaurantBills);
console.log(tipCalculator)


function calcAvgTips(tips)
{
    var sum = 0;
    for (i = 0; i < tips.length; i++)
    {
        sum += tips[i];
    }
    return sum / tips.length;
}

tipCalculator.tipAmount(restaurantBills);
tipCalculator.avergae = calcAvgTips(tipCalculator.tips);
console.log(tipCalculator.avergae);

*/
















