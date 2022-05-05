/*
 * Amit Phaltankar
 * 22/08/2020
 *
 * Packt MongoDB For Begginers.
 * Chapter 5
 */

// Exercise code for Packt MongoDB For Begginers.
// Exercise 5.02 Delete a low rated movie

/**
 * Your task for this exercise
 * 1. Prepare and execute a delete command
 * 2. The query condition should find movies by IMDb rating of less than 2
 * 3. The IMDb vote count should be more than 50000
 * 4. Find all such movies and delete the one with least number of awards
 * 5. Return the deleted document in respose and include title field.
 *
 */
db.movies.findOneAndDelete(
	{ "imdb.rating": { $lt: 2 }, "imdb.votes": { $gt: 50000 } },
	{
		sort: { "awards.won": 1 },
		projection: { title: 1 },
	}
);

db.movies.find(
	{ "imdb.rating": { $lt: 2 }, "imdb.votes": { $gt: 50000 } },
	{ _id: 0, title: 1, year: 1 }
);

db.users.insertMany([
	{ _id: 2, name: "Jon Snow", email: "Jon.Snow@got.es" },
	{ _id: 3, name: "Joffrey Baratheon", email: "Joffrey.Baratheon@got.es" },
	{ _id: 5, name: "Margaery Tyrell", email: "Margaery.Tyrell@got.es" },
	{ _id: 6, name: "Khal Drogo", email: "Khal.Drogo@got.es" },
]);

db.users.replaceOne(
	{ name: "Margaery Tyrell" },
	{ name: "Tommen Baratheon", email: "Tommen.Baratheon@got.es" },
	{ upsert: true }
);

db.new_movies.insertMany([
	{ _id: 1011, title: "Macbeth" },
	{ _id: 1513, title: "Macbeth" },
	{ _id: 1819, title: "Macbeth" },
	{ _id: 2117, title: "Macbeth" },
]);

db.movies.insertMany([
	{ _id: 1, title: "Macbeth", year: 2014, type: "series" },
	{
		_id: 2,
		title: "Inside Out",
		year: 2015,
		type: "movie",
		num_mflix_comments: 1,
	},
	{
		_id: 3,
		title: "The Martian",
		year: 2015,
		type: "movie",
		num_mflix_comments: 1,
	},
	{
		_id: 4,
		title: "Everest",
		year: 2015,
		type: "movie",
		num_mflix_comments: 1,
	},
]);
