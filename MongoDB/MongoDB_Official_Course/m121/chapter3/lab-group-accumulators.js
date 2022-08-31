/**
 * For all films that won at least 1 Oscar, calculate the standard deviation, highest,
 * lowest, and average imdb.rating. Use the sample standard deviation expression.
 *
 * HINT - All movies in the collection that won an Oscar begin with a string resembling
 * one of the following in their awards field
 */

// $elemMatch is used to see if an array exists

db.movies.aggregate([
	{
		$match: {
			awards: { $exists: true },
			awards: /Won \d{1,2} Oscars?/,
		},
	},
	{
		$group: {
			_id: null,
			imdb_rating_min: { $min: "$imdb.rating" },
			imdb_rating_max: { $max: "$imdb.rating" },
			imdb_rating_avg: { $avg: "$imdb.rating" },
			imdb_rating_stdve: { $stdDevSamp: "$imdb.rating" },
		},
	},
]);
