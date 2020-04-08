///////////////////////////////////////////////////////
// FUNCTION CONSTRUCTORS
//////////////////////////////////////////////////////
/*

}var john = {
    name: 'John',
    birthYear: 1990,
    job: 'Teacher'
};

// Function constructor: pattern for writting a blueprint
// Capital letter for constructor
var Person = function(name, birthYear, job) {
    this.name = name;
    this.birthYear = birthYear;
    this.job = job;
//    this.calcAge: function() {
//        console.log(2020 - this.birthYear)
//    }
}

// method is no longer in the constructor but we can use inheritance 
// so that other objects can use the calcAge function
Person.prototype.calcAge = function() {
    console.log(2020 - this.birthYear);
};

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

console.log(john.hasOwnProperty('lasName'));

console.log(john instanceof Person);

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
    }
};

var john = Object.create(personProto);

john.name = 'John';
john.birthYear = 1990;
john.job = 'Teacher';

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

// both objects hold a reference to the object in memory. They are pointing to the same 
// object in memory
var obj2 = obj1;

obj1.age = 30;

console.log(obj1.age);
console.log(obj2.age);


// FUNCTION
var age = 27;

var obj = {
    name: 'Gonzalo',
    city: 'Houston'
};

function change(a, b) {
    a= 30;
    b.city = 'Seattle';
}

change(age, obj)

console.log(age);
console.log(obj.city);










