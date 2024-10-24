// findOne() finds the first document where condition is met
db.movies.findOne({});

// find gives back a courser
// find gives back all documents
db.movies.find();

// find queries on equality
db.movies.find({ name: 'The Last Ship' });
db.movies.find({ runtime: 60 });

// Comparison operators
db.movies.find({ runtime: { $eq: 60 } }); // this is the same as the one above
// because mongo queries on equality by default
db.movies.find({ runtime: { $ne: 60 } });

db.movies.find({ runtime: { $lte: 42 } });

// embedded documents
// query a path using dot notation
db.movies.find({ 'rating.average': { $gt: 7 } });

// is value this or this. These two are equivalent
db.movies.find({ runtime: { $in: [60, 90] } });
db.movies.find({ $or: [{ runtime: { $eq: 60 } }, { runtime: { $eq: 90 } }] });

// movies of Drama or Action
db.movies.find({ $or: [{ genres: 'Drama' }, { genres: 'Action' }] });
// and is the default in mongo
db.movies.find({ 'imdb.rating': { $gt: 9 }, genres: 'Drama' });

// use $expr to compare two fields
db.movies.find({ $expr: { $gt: ['$field_1', '$field_2'] } });

// query a field that is an ARRAY
// searching like this checks to see if drama is in the array
db.movies.find({ genres: 'Drama' });
// Drama like this mongo looks to see if genres is the only one in the array
db.movies.find({ genres: ['Drama'] });
// search for title in hobbies array that has Sports
db.users.find({ 'hobbies.title': 'Sports' }).count();
//this does not care of sports frequency is gte 2
db.users.find({ $and: [{ 'hobbies.title': 'Sports' }, { 'hobbies.frequency': { $gte: 2 } }] });
//
db.users.find({ hobbies: { $elemMatch: { title: 'Sports', frequency: { $gte: 5 } } } });

//find all movies with exactly two genres
db.movies.find({ genres: { $size: 2 } });
// find all movies which aired in 2018
db.movies.find({ year: { $eq: '2018' } });
// find all movies which have a rating greater than 8 but less than 10
db.movies.find({ 'imdb.rating': { $gt: 8 }, 'imdb.rating': { $lt: 10 } });
db.users.insertMany([
	{
		name: 'Max',
		hobbies: [
			{ title: 'Sports', frequency: 3 },
			{ title: 'Cooking', frequency: 6 },
		],
		phone: '1232322233',
		age: 30,
	},
	{
		name: 'Matt',
		hobbies: [
			{ title: 'Cars', frequency: 2 },
			{ title: 'Cooking', frequency: 5 },
		],
		phone: 4444444444,
	},
]);

db.users.insertOne({
	name: 'Ana',
	hobbies: [
		{ title: 'Sports', frequency: 2 },
		{ title: 'Yoga', frequency: 3 },
	],
	phone: '5555555555',
	age: null,
});

db.users.insertOne({
	name: 'Chris',
	hobbies: [
		{ title: 'Sports', frequency: 2 },
		{ title: 'Cooking', frequency: 3 },
		{ title: 'Hiking', frequency: 3 },
	],
	phone: '5555555555',
	age: null,
});

db.users.find({ age: { $ne: null } });
db.users.find({ age: { $exists: true } });
// age exists and equals 30
db.users.find({ age: { $exists: true, $eq: 30 } });

// exists and not eq null
db.users.find({ age: { $exists: true, $ne: null } });
// check for type
db.users.find({ phone: { $type: 'string' } });
db.users.find({ phone: { $type: 'double' } });

// size need to be an exact match
db.users.find({ hobbies: { $size: 3 } });

// find genre in this order
db.movies.find({ genres: ['Action', 'Thriller'] });

// order does not matter
db.movies.find({ genres: { $all: ['Action', 'Thriller'] } });

// find all user who have a hobby  of sports and frequency of 3
db.users.find({ 'hobbies.title': 'Sports', 'hobbies.frequency': 2 });
// this seems to return the correct results, however, we find all documents in hobbies with title sports
// and a document with frequency gte 3, they do not have to be the same documents
db.users.find({ $and: [{ 'hobbies.title': 'Sports' }, { 'hobbies.frequency': { $gte: 2 } }] });
db.users.find({ $and: [{ 'hobbies.title': 'Sports' }, { 'hobbies.frequency': { $gte: 3 } }] });

// use elemMatch: Pass in the field , then elemMatch then pass in what you are checking for
// We can look inside embedded documents with elemMatch
db.users.find({ hobbies: { $elemMatch: { title: 'Sports', frequency: { $gte: 3 } } } });

db.movies.find({ genres: { $all: ['Drama', 'Horror'] } }, { 'genres.$': 1 });

db.movies.find({ genres: 'Drama' }, { genres: { $elemMatch: { $eq: 'Horror' } } });
//
db.sales.insertMany([
	{ volume: 100, target: 120 },
	{ volume: 80, target: 80 },
	{ volume: 200, target: 177 },
]);

// where is volume above target
// this will not work, it will compare the two string
db.sales.find({ $expr: { $gt: ['volume', 'target'] } });
// use $ to refer to the field value
db.sales.find({ $expr: { $gt: ['$volume', '$target'] } });
// where volume is above 190 the difference to target has to be at least 10.
db.sales.find({
	$expr: {
		$gt: [
			{
				$cond: {
					if: { $gte: ['$volume', 190] },
					then: { $subtract: ['$volume', 10] },
					else: '$volume',
				},
			},
			'$target',
		],
	},
});

//
db.movies.find({ genres: { $all: ['Drama', 'Horror'] } }, { 'genres.$': 1 });
db.movies.find({ genres: 'Drama' }, { genres: { $elemMatch: { $eq: 'Horror' } } });
