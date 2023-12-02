// I can take a sql approach
db.products.insertOne({ name: 'A T-Shirtk', price: 20.99, details: null });

// Types
//
db.companies.insertOne({
	name: 'Fresh Apples Inc',
	isStartup: true,
	employees: 33,
	funding: 12345678901234567890, // this number gets cut off because its to big. Store them separately or as a string
	details: { ceo: 'Mark Super' },
	tags: [{ title: 'super' }, { title: 'perfect' }],
	foundingDate: new Date(),
	insertedAt: new Timestamp(),
});

db.patients.insertOne({ name: 'Max', age: 29, diseaseSummary: 'Sumary-max-1' });
db.diseaseSummaries.insertOne({ _id: 'summary-max-1', diseases: ['cold', 'broken leg'] });
// used two queries to get this
var dsid = db.patients.findOne().diseaseSummar;
db.diseaseSummaries.findOne({ _id: dsid });

// for 1-1 use embedded documents
db.patients.insertOne({ name: 'Max', age: 29, diseaseSummary: { diseases: ['cold', 'broken leg'] } });

db.persons.insertOne({ name: 'Max', car: { model: 'BMW', price: 40000 } });
db.persons.insertOne({ name: 'Max', age: 29, salary: 3000 });

db.cars.insertOne({ model: 'BMW', price: 40000, owner: ObjectId('6558c2d5223eb0719b2df5f2') });

// 1-many relation

db.questionThreads.insertOne({ name: 'Max', question: 'How does that all work?', answers: ['q1a1', 'q2a2'] });
db.answers.insertMany([{ _id: 'q1a1', text: 'it works like that', _id: 'q2a2', text: 'Thanks' }]);

// embedded might be better
db.questionThreads.insertOne({ name: 'Max', question: 'How does that all work?', answers: [{ text: 'it works like that' }, { text: 'Thanks' }] });

// 1-Many may not be a good idea when to much data is being transferred, 16MB limit
db.cities.insertOne({ name: 'New York City', coordinates: { lat: 21, lng: 55 } });
db.citizens.insertMany([
	{ name: 'Gonzalo B.', cityId: ObjectId('6558c65e223eb0719b2df5f9') },
	{ name: 'Maria C.', cityId: ObjectId('6558c65e223eb0719b2df5f9') },
]);

// many to many relationship
// use references
// three tables from sql world
db.products.insertOne({ title: 'A Book', price: 12.99 });
db.customers.insertOne({ name: 'Max', age: 29 });
db.ordersRef.insertOne({ productId: ObjectId('6558c713223eb0719b2df5fc'), customerId: ObjectId('6558c72d223eb0719b2df5fd') });
// I can use two tables instead in mongodb
db.customersEmbedded.insertOne({ name: 'Max', age: 29 });
db.customersEmbedded.updateOne({}, { $set: { orders: [{ productId: ObjectId('6558c713223eb0719b2df5fc'), quantity: 2 }] } });
db.customersEmbedded.updateOne({}, { $set: { orders: [{ title: 'A Book', price: 12.99 }] } });

// using refs
// taking this approach I may need to change data in multiple places
db.books.insertOne({
	name: 'My fav',
	authors: [
		{ name: 'Maria C', age: 29 },
		{ name: 'Gonzalo B', age: 29 },
	],
});
db.authors.insertMany([
	{ name: 'Maria C', age: 29, address: { street: 'Not main' } },
	{ name: 'Gonzalo B', age: 29, address: { street: '8125 Rose' } },
]);

// use refs
// this is better
db.books.updateOne({}, { $set: { authors: [ObjectId('6558ca64223eb0719b2df602'), ObjectId('6558ca64223eb0719b2df603')] } });

// Joining with look
// from: which other collection
// localField: in current collection where can references in other collection be found
db.books.aggregate([{ $lookup: { from: 'authors', localField: 'authors', foreignField: '_id', as: 'creators' } }]);

// comments
db.users.insertMany([
	{ name: 'Maria', age: 29, email: 'me@test.com' },
	{ name: 'Gonzalo', age: 29, email: 'gon@test.com' },
]);

db.posts.insertOne({
	title: 'First',
	text: 'adsfjha asdkfjhs First',
	tags: ['new', 'happy'],
	creator: ObjectId('6558cf41223eb0719b2df604'),
	comments: [
		{ text: 'I like it', author: ObjectId('6558cf41223eb0719b2df605') },
		{ text: 'Good job', author: ObjectId('6558cf41223eb0719b2df604') },
	],
});
