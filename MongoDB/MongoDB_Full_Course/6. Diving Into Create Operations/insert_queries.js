// insert one
db.persons.insertOne({ name: 'Gonzalo', age: 32, hobbies: ['sports', 'cooking'] });

db.persons.insertOne({ name: 'Maria', age: 32, hobbies: ['running', 'cooking'] });

// use an array of documents
db.persons.insertMany([
	{ name: 'Alison', age: 5, hobbies: ['running', 'soccer'] },
	{ name: 'Alexa', age: 10, hobbies: ['running', 'soccer'] },
]);

db.persons.insert([{ name: 'Canelo', age: 5, hobbies: ['running', 'soccer'] }]);

// order inserts
db.hobbies.insertMany([{ _id: 'sports' }, { _id: 'cooking' }, { _id: 'cars' }]);
db.hobbies.insertMany([{ _id: 'yoga' }, { _id: 'cooking' }, { _id: 'hiking' }]);

// the ones that fail are not inserted --> default behave
db.hobbies.insertMany([{ _id: 'basketball' }, { _id: 'cooking' }, { _id: 'soccer' }], { ordered: false });

// nothing will be inserted isf something fails
db.hobbies.insertMany([{ _id: 'nothing' }, { _id: 'biking' }, { _id: 'trees' }], { ordered: true });
