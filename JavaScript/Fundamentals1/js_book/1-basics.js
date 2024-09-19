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

one();
