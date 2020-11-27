// Own hash value
// Not constant time
// not very random, generates some similar outputs.
const hash = (key, arrayLength) => {
	let total = 0;
	for (let char of key) {
		let value = char.charCodeAt(0) - 96;
		total = (total + value) % arrayLength;
	}
	return total;
};

// Letters in numerical order starting from 1
// console.log("a".charCodeAt() - 96);
console.log(hash("pink", 10));

const hash2 = (key, arrayLength) => {
	let total = 0;
	let PRIME = 31; // Helps reduce collisions
	for (let i = 0; i < Math.min(key.length, 100); i++) {
		let char = key[i];
		let value = char.charCodeAt(0) - 96;
		total = (total * PRIME + value) % arrayLength;
	}
	return total;
};

console.log(hash2("hello", 13));
console.log(hash2("cyan", 13));
console.log(hash2("pink", 13));
console.log(hash2("good", 13));
