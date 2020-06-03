// Everything is almos an object in JS.
// Primitives: Numbers, strings, boolean, undefined, null
// Everything else is an object: Array, functions, Objects, Dates, Wrappers for numbers, string booleans
// Look at inheritance and the prototype chain
// Objects interact with one another though methods and properties.
// We use them to store data, structure apps into modules and they also keep code clean

// Constructors and prototypes: are basically classes with attributes.
// 

///////////////////////////////////////////////////////
// FUNCTION CONSTRUCTORS
//////////////////////////////////////////////////////

let name = "John"; 
name = "Pete";
sayHi();

function sayHi() {
    console.log("Hi, " + name);
}

// function is an instance of the Object type
// it behaves like an object
// can be stored inside variables
// pass it as an arg.
// return it 

/*
var john = 
{
    name: 'John',
    birthYear: 1990,
    job: 'Teacher'
};


// Function constructor: pattern for writting a blueprint
// Capital letter for constructor: Similar to creating a class in Java.
var Person = function(name, birthYear, job) {
    this.name = name;
    this.birthYear = birthYear;
    this.job = job;
//    this.calcAge = function() {
//        console.log(2016- this.birthYear);
//    };
};


// method is no longer in the constructor but we can use inheritance 
// so that other objects can use the calcAge function
Person.prototype.calcAge = function() {
    console.log(2016 - this.birthYear);
};

// the last name will be inherited on all of them.
Person.prototype.lastName = 'Smith';

// new creates an empty object and Person creates the object
// this.name from empty new object points to Person parameters to create the object
var john = new Person('John', 1990, 'Teacher'); // instantiate the Person object

var jane = new Person('Jane', 1969, 'Designer');

var mark = new Person('Mark', 1948, 'Retired');


john.calcAge();
jane.calcAge();
mark.calcAge();

console.log(john.lastName);
console.log(jane.lastName);
console.log(mark.lastName);
//
//console.log(john.hasOwnProperty('lasName'));
//
//console.log(john instanceof Person);

*/

///////////////////////////////////////////////////////
// object.create method. Builds the object that inherits directly
// from the one that we passed. Constructor the newly created object
// inherits from the constructor property
//////////////////////////////////////////////////////

/*
var personProto = {
    calcAge: function() {
        console.log(2016 - this.birthYear);
    },
    lastname: 'Smith'
};

// Object.create() will inherit values from personProto even if personProto is not a constructor
var john = Object.create(personProto);

//console.log(john.hasOwnProperty('calcAge'));
//console.log(personProto.hasOwnProperty('calcAge'));
//
john.name = 'John';
john.birthYear = 1990;
john.job = 'Teacher';
////john.lastname = 'None';  // adding another lastname will replace inherited lastname
//
//console.log(john.lastname);
//

// another way to create the Object
var jane = Object.create(personProto,
{
    name: {value: 'jane'},
    birthYear: {value: 1969},
    job: {value: 'Design'}
});

*/

///////////////////////////////////////////////////////
// PRIMITIVES vs. OBJECTS
//////////////////////////////////////////////////////


// numbers, strings, booleans undefined, null are primitives everything
// else are objects

// Primitives hold the data
// objects don't contain the object they contain a reference to the location
// in memory where the data is held

/*

var a = 23;
var b = a;

a = 46;

// Each of the primitive values holds a copy of the data
console.log(a);
console.log(b); // does not change it is still 23



// OBJECTS
var obj1 = {
    name: 'John',
    age: 26
};
//
//// both objects hold a reference to the object in memory. They are pointing to the same 
//// object in memory
var obj2 = obj1;

obj1.age = 30;
obj1.name = 'Changed'
console.log(obj1.age);
console.log(obj2.age);


//// FUNCTIONS
var age = 27;

var obj = {
    name: 'Gonzalo',
    city: 'Houston'
};

function change(a, b) {
    a = 30;
    b.city = 'Seattle';
    
}

change(age, obj)

console.log(age);
console.log(obj.city); 

*/

///////////////////////////////////////////////////////
// PASSING FUNCTIONS AS ARGUMENTS
//////////////////////////////////////////////////////

/*
var years = [1990, 1965, 1937, 2005, 1986];

function arrayCalc(arr, func) {
    var arrResults = [];
    for (var i = 0; i < arr.length; i++)  {
        arrResults.push(func(arr[i]));
    }
    return arrResults;
}

function calculateAge(el) {
    return 2020 - el;
}

function isFullAge(el) {
    return el >= 18;
}


function maxHeartRate(el) {
    if (el >= 18 && el <= 81) {
        return Math.round(206.9 - (0.67 * el));
    } else {
        return - 1; 
    }
}

var ages = arrayCalc(years, calculateAge);
console.log(ages);

var resBool = arrayCalc(ages, isFullAge);
console.log(resBool);

var heartRate = arrayCalc(ages, maxHeartRate);
console.log(heartRate);

*/

///////////////////////////////////////////////////////
// RETURNING FUNCTIONS
//////////////////////////////////////////////////////

/*
function interviewQuestion(job) 
{
   if (job === 'designer') 
   {
       return function(name) 
       {
           console.log(name + ', can you please explain what UX design is?');
       }
   } else if (job === 'teacher') 
    {
        return function(name) 
        {
            console.log('What subject do you teach, ' + name + '?');
        } 
    } else 
    {
        return function(name) 
        {
            console.log('Hello ' + name + ', what do you do?');
        }
   }
}

var teacherQuestion = interviewQuestion('teacher');
teacherQuestion('John');


var designerQuestion = interviewQuestion('designer');
designerQuestion('Jane');


designerQuestion('Mike');

interviewQuestion('teacher')('Jordan'); // Jordan name calls the function that gets returns by interviewQuestion

*/


///////////////////////////////////////////////////////
// IIFE: IMMEDIATELY INVOKED FUNCTION EXPRESSIONS
//////////////////////////////////////////////////////

/*

//function game() {
//    var score = Math.random() * 10;
//    console.log(score >= 5);
//}
//
//game();    


// wrap the function in parenthesis to trick the console that it is an expression
// this creates data privacy because score can't be accessed outside the function 
// whats inside te () can't be a statemnt. 

(function(goodLuck) {
    var score = Math.random() * 10;
    console.log(score >= 5 -  goodLuck);
})(1); 

*/

///////////////////////////////////////////////////////
// CLOSURES
//////////////////////////////////////////////////////

/*
// closure use scope rules and access items that are in the execution stack
function retirement(retAge) {
    var a = ' years left until retirement.';
    return function(birthYear) {
        var age = 2020 - birthYear;
        console.log((retAge - age) + a);
    }
}

var retirementUS = retirement(66);
var retirementGermany = retirement(65);
var retirementIceland = retirement(67);

retirementUS(1990);
retirementGermany(1990);
retirementIceland(1990);

// rewrite the interview questions using closures

function interviewQuestion(job) {
    var a = ', can you please what UX design is?';
    var b = 'What subject do you teach, ';
    var c = ', what do you teach?';    

    return function(name) {
        if (job === 'designer') {
            console.log(name + a);
        } else if (job === 'teacher') {
            console.log(b + name + '?');
            
        } else {
            console.log('Hello ' + name + c);
        }
    }
}


interviewQuestion('teacher')('John');

*/

///////////////////////////////////////////////////////
// BIND, CALL & APPLY
//////////////////////////////////////////////////////

/*
var john = {
    name: 'John',
    age: 26,
    job: 'teacher',
    presentation: function(style, timeOfDay) {
        if (style === 'formal') {
            console.log('Good ' + timeOfDay + ' Ladies and Gentelmen! I\'m ' + this.name + ', I\'m a ' + this.job + ' and I\'m ' + this.age + ' years old.');
        } else if (style === 'friendly') {
            console.log('Hey! What\'s up? I\'m ' + this.name + ' I\'m a ' + this.job + ' and I\'m ' + this.age + ' years old. Have a nice ' + timeOfDay + '.');
        }
    }
};


var emily = {
    name: 'Emily',
    age: 35,
    job: 'designer',
};

john.presentation('formal', 'morning');

//////////
// CALL //
/////////
// Method borrowing for emily object call(this variable, param1, param2, paramN)
john.presentation.call(emily, 'friendly', 'afternoon'); 

///////////
// APPLY //
///////////
//Apply accepts an ARRAY
john.presentation.apply(emily, ['formal', 'afternoon'])

///////////
// BIND ///
///////////
// bind does not call the function but instead generates a copy of the function with a preset argument
var johnFriendly = john.presentation.bind(john, 'friendly');
johnFriendly('morning');
johnFriendly('night');


var emilyFormal = john.presentation.bind(emily, 'formal');
emilyFormal('Zoo');



var years = [1990, 1965, 1937, 2005, 1998];

function arrayCalc(arr, fn) {
    var arrResults = [];
    for (var i = 0; i < arr.length; i++)  {
        arrResults.push(fn(arr[i]));
    }
    return arrResults;
}

function calculateAge(el) {
    return 2020 - el;
}

function isFullAge(limit, el) {
    return el >= limit;
}


var ages = arrayCalc(years, calculateAge);

// "this" is the presete limit = 20
var fullJapan = arrayCalc(ages, isFullAge.bind(this, 20) );
console.log(ages);
console.log(fullJapan);

*/

///////////////////////////////////////////////////////
// CODING CHALLENGE
//////////////////////////////////////////////////////

/*

// 1.Build a quize game
//      Allow user to select the correct answer from within console
// 2. create a couple of questions using the constructor
// 3. Store them all inside an array
// 4. Select a random quesion (write a method for the question objects)
// 5. Use the prompt function to ask the user to enter the correct number
// 6. check of the answer is correct., write another method for this
// Make sure code is private 


// this function creates privacy 
(function() {
    // constructor
    function Question(question, answer, correct) {
        this.question = question;
        this.answer = answer;
        this.correct = correct;
    }
    
    // displays the question using prototyp
    Question.prototype.displayQuestion = 
        function() {
        console.log(this.question);

        // go over the answers
        for(var i = 0; i < this.answer.length; i++) {
            console.log(i + ': ' + this.answer[i]);
        }
    }

    Question.prototype.checkAnswer = 
        function(ans, kpscore) {
        var sc;
        
        if (ans === this.correct) {
            console.log('Correct!!!');
            sc = kpscore(true);
        } else {
            console.log('Not Correct');
            sc = kpscore(false);
        }
        this.displayScore(sc);
    }

    var q1 = new Question('Is basketball the best sport?', ['Yes', 'No'], 0);

    var q2 = new Question('What is the name of this course?', ['CSI', 'JS', 'mmm'], 1);

    var q3 = new Question('What does NBA stand for?', ['National Basketball Association', 'Not Bad All', 'No Boys Allowed'], 0);
    
    // add questions to an array to select at random with Math.random()
    var questions = [q1, q2, q3];
    
    function score() {
        var points = 0;
        return function(correct) {
            if(correct) {
                points++;
            }
            return points;
        }
    }
    

    Question.prototype.displayScore = function(score) {
        console.log('Your current score is : ' + score);
        console.log('------------------------------');
    }

    var keepScore = score();
    
    function nextQuestion() {

        var n = Math.floor(Math.random() * questions.length);

        questions[n].displayQuestion();

        // promt 
        // parseInt --> casting
        var answer = prompt('Please select the correct answer: ');
        
        if (answer !== 'exit') {
            questions[n].checkAnswer(parseInt(answer), keepScore); 
            
            
            nextQuestion();    
        }
    }
    
    nextQuestion();
})();  // call it at the end 

*/














