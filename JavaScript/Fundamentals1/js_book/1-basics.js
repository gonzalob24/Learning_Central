//
'use strict';
console.log('' + 1 + 0);
console.log(null + 1);
console.log(undefined + 1);

console.log('2' + '3');

console.log(+'2' + +'3');
console.log('Z' > 'A');

console.log(null || 2 || undefined);

const hashed_2 = {};
hashed_2[100] = 0;
console.log(hashed_2);
console.log(100 in hashed_2);

// cloning
let user = { name: 'Alexa', size: { shoe: 12 } };
let skill = { can_pass: true };
let skill_2 = { can_kick: true };

Object.assign(user, skill, skill_2);
let player_2 = {};
Object.assign(player_2, user);
console.log(user);
console.log(player_2);
//
console.log(user == player_2);
console.log(user === player_2);

// they are the same object. To solve this issue we need to perform deep cloning
// can also use lodash, _.cloneDeep(obj)
console.log(user.size == player_2.size);

let player_3 = { id: Symbol('id'), name: 'Maria' };
console.log(player_3);

// hash functions review
let user_2 = {
	age: 11,
	name: 'Alison',
	sport: 'soccer',
	intro: function () {
		console.log('I am the best');
	},
};

user_2.skill = 'Kicking';
console.log(user_2);

const soccer_player = {
	u_name: 'Alexa',
	skill: 'running',
	// arrow function do not have a this keyword
	// intro: () => console.log(`Hi my name is ${this.u_name} and I love ${this.skill}`),
	intro: function () {
		console.log(this);
		console.log(`Hi my name is ${this.u_name} and I love ${this.skill}`);
	},
};

soccer_player.intro();
let say_hi = soccer_player.intro;
// the this keyword is lost here:

console.log('1');
console.log('2');
console.log('3');

const one = () => {
	const get_data = () =>
		setTimeout(() => {
			console.log('time out');
		}, 2000);
	const get_data_2 = () =>
		setTimeout(() => {
			console.log('more time');
		}, 1000);

	get_data();
	get_data_2();
	console.log('oneeee');
};

// one();

let num = new Number('123');
console.log(typeof num);
// type is object..
if (num) {
	console.log('its truthy');
}

let num2 = Number('123');
console.log(typeof num2);

// type is of type number
if (num2) {
	console.log('still truthy');
}
// 64 bits to store a number, 52 are used to store the digit and 11 to store precision
console.log((123).toString());
console.log((123.456).toFixed(2));
console.log(0.1 + 0.2 == 0.3);
console.log(0.1 + 0.2); // loss of precision

/**
 * numbers are store in memory as binary
 * 0.1 -- 1/10 -> in binary becomes an endless binary fraction
 * 03. -- 1/3 --> 0.33333 to infinity
 */

// precision loss is still there, we are simply rounding
console.log(Number((0.1 + 0.2).toFixed(2)) == 0.3);
console.log(Number((0.1 + 0.2).toFixed(2)));
console.log((1.35).toFixed(1));
console.log((6.35).toFixed(1)); // 6.4 due to precision loss
console.log((1.35).toFixed(20));
console.log((6.35).toFixed(20));
console.log(Math.round(6.35 * 10) / 10);

// Strings

// There are many array strings, look up the ones that are needed
// indexOf, startsWith, endsWith, includes, slice()

// comparing strings, uppercase before lowercase
// all strings are encoded using UTF-16

// arrays
const arr_1 = new Array(4);
const arr_2 = [];
console.log(arr_1); // created with 4 empty items
console.log(arr_2);

const max_sub_sum = (arr) => {
	let current_sum = 0;
	let max_sum = 0;

	for (let i = 0; i < arr.length; i++) {
		current_sum = Math.max(current_sum + arr[i], arr[i]);
		max_sum = Math.max(current_sum, max_sum);
	}

	return max_sum;
};

console.log(max_sub_sum([-1, 2, 3, -9]));
console.log(max_sub_sum([2, -1, 2, 3, -9]));

// in place sort values are treated as strings and then compared
console.log([1, 15, 2].sort());

const compare = (a, b) => {
	if (a > b) {
		return 1;
	}
	if (a == b) {
		return 0;
	}
	if (a < b) {
		return -1;
	}
};

console.log([1, 15, 2].sort(compare));

let arr_3 = [1, 2, 3, 4, 5];

let sum = arr_3.reduce((sum, current_number) => sum + current_number, 0);
console.log(sum);

function sort_by_age(arr) {
	return arr.sort((a, b) => (a.age > b.age ? 1 : -1));
}

const users = [
	{ name: 'Alexa', age: 11 },
	{ name: 'Alison', age: 6 },
	{ name: 'Gonzalo', age: 37 },
	{ name: 'Mary', age: 35 },
];

console.log(sort_by_age(users));
