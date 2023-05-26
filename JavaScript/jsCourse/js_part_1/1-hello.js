console.log('Hello');
// alert('Hey');

let me;
let iamNull = null;
console.log(me);
console.log(iamNull);

if (true) {
	var functionScope = 'eight';
	let blockScope = 'nine';
}

// console.log(functionScope);
// console.log(blockScope);

let x = 10;
let y = 10;

// console.log(x++);
// console.log(++y);

let z = ++x - 5 * 2;

console.log(z);

// let bmi = mass / height ** 2 = mass / (height * height)

let marksHeight = 1.69;
let marksWeight = 92;
let johnsHeight = 1.96;
let johnsWeight = 86;

let markBmi = marksWeight / marksHeight ** 2;
let johnBmi = johnsWeight / johnsHeight ** 2;

console.log(markBmi, johnBmi);

// Booleans
console.log(Boolean(0));
console.log(Boolean(undefined));
console.log(Boolean('Me'));
console.log(Boolean({}));

// Better to use logical operators

// const favorite = prompt('Whats your favorite number? ');
// console.log(typeof favorite);

// Switch cases

const day = 'offf';

switch (day) {
	case 'monday': // this compares a strict equality
		console.log('its monday');
		break;
	case 'tuesday':
		console.log('its tuesday');
		break;
	case 'wednesday':
		console.log('its wednesday');
		break;
	case 'thursday':
	case 'friday':
		console.log('its tuesday or friday');
		break;
	// case 'thursday':
	// 	console.log('its tuesday');
	// 	break;
	case 'saturday':
		console.log('its tuesday');
		break;
	case 'sunday':
		console.log('i am off');
		break;
	default:
		console.log('do nothing... I wish');
}
