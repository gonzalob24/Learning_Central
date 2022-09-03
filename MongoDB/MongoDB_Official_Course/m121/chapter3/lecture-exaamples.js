db.movies.aggregate([
	{
		$group: { _id: "$year", num_films_in_year: { $sum: 1 } },
	},
	{
		$sort: { num_films_in_year: -1 },
	},
]);

db.movies.aggregate([
	{
		$group: {
			_id: {
				numDirectors: {
					$cond: [{ $isArray: "$directors" }, { $size: "$directors" }, 0],
				},
			},
			numFilms: { $sum: 1 }, // the number of documents that match
			averageMetacritic: { $avg: "$metacritic" },
		},
	},
	{
		$sort: { "_id.numDirectors": -1 },
	},
]);

db.movies.aggregate([
	{
		$match: { metacritic: { $gte: 0 } },
	},
	{
		$group: { _id: null, averageMetacritic: { $avg: "$metacritic" } },
	},
]);

db.movies.aggregate([
	{
		$group: {
			_id: null,
			count: { $sum: 1 },
		},
	},
]);

db.icecream_data.aggregate([
	{
		$project: {
			_id: 0,
			max_high: {
				$reduce: {
					input: "$trends",
					initialValue: -Infinity,
					in: {
						$cond: [
							{ $gt: ["$$this.avg_high_tmp", "$$value"] },
							"$$this.avg_high_tmp",
							"$$value",
						],
					},
				},
			},
		},
	},
]);

db.icecream_data.aggregate([
	{
		$project: {
			_id: 0,
			max_low: {
				$reduce: {
					input: "$trends",
					initialValue: Infinity,
					in: {
						$cond: [
							{ $lt: ["$$this.avg_low_tmp", "$$value"] },
							"$$this.avg_low_tmp",
							"$$value",
						],
					},
				},
			},
		},
	},
]);

// another way to achieve the same results
db.icecream_data.aggregate([
	{
		$project: {
			_id: 0,
			max_high: { $max: "$trends.avg_high_tmp" },
		},
	},
]);

db.icecream_data.aggregate([
	{
		$project: {
			_id: 0,
			max_low: { $min: "$trends.avg_low_tmp" },
		},
	},
]);

db.icecream_data.aggregate([
	{
		$project: {
			_id: 0,
			avg_cpi: { $avg: "$trends.icecream_cpi" },
			cpi_deviation: { $stdDevPop: "$trends.icecream_cpi" },
		},
	},
]);

db.icecream_data.aggregate([
	{
		$project: {
			_id: 0,
			"Yearly sales (millions)": { $sum: "$trends.icecream_sales_in_millions" },
		},
	},
]);

// how many films have awards
db.movies.aggregate([
	{
		$match: {
			awards: { $exists: true },
			awards: /Won \d{1,2} Oscars?/,
		},
	},
]);

// $unwind
db.movies.aggregate([
	{
		$match: {
			"imdb.rating": { $gt: 0 },
			year: { $gte: 2010, $lte: 2015 },
			runtime: { $gte: 90 },
		},
	},
	{
		$unwind: "$genres",
	},
	{
		$group: {
			_id: {
				year: "$year",
				genre: "$genres",
			},
			average_rating: { $avg: "$imdb.rating" },
			number_of_movies: { $sum: 1 },
		},
	},
	{
		$sort: { "_id.year": -1, average_rating: -1 },
	},
]);

db.movies.aggregate([
	{
		$match: {
			"imdb.rating": { $gt: 0 },
			year: { $gte: 2010, $lte: 2015 },
			runtime: { $gte: 90 },
		},
	},
	{
		$unwind: "$genres",
	},
	{
		$group: {
			_id: {
				year: "$year",
				genre: "$genres",
			},
			average_rating: { $avg: "$imdb.rating" },
			number_of_movies: { $sum: 1 },
		},
	},
	{
		$sort: { "_id.year": -1, average_rating: -1 },
	},
	{
		$group: {
			_id: "$_id.year",
			genres: { $first: "$_id.genre" },
			average_rating: { $first: "$average_rating" },
		},
	},
	{
		$sort: { _id: -1 },
	},
]);

// $lookup
db.air_alliances.aggregate([
	{
		$lookup: {
			from: "air_airlines",
			localField: "airlines",
			foreignField: "name",
			as: "airlines",
		},
	},
]);

// $graphLookup
// start to analyze from Eliot with its $_id
// start with parent and get all of it descendants.
// connectedFromField _id for subsequent searches
db.parent_reference.aggregate([
	{
		$match: { name: "Eliot" },
	},
	{
		$graphLookup: {
			from: "parent_reference",
			startWith: "$_id",
			connectFromField: "_id",
			connectToField: "reports_to",
			as: "all_reports",
		},
	},
]);

// field value matching to another field value document _id.
// recursively get all of the people someone reports to reports to
db.parent_reference.aggregate([
	{
		$match: { name: "Shannon" },
	},
	{
		$graphLookup: {
			from: "parent_reference",
			startWith: "$reports_to",
			connectFromField: "reports_to",
			connectToField: "_id",
			as: "bosses",
		},
	},
]);

// array value match to field, recursively gets all documents that contain the array value as part of the field value.
db.child_reference.aggregate([
	{
		$match: { name: "Dev" },
	},
	{
		$graphLookup: {
			from: "child_reference",
			startWith: "$direct_reports",
			connectFromField: "direct_reports",
			connectToField: "name",
			as: "all_reports",
		},
	},
]);

// array value match to field, recursively gets all documents that contain the array value as part of the field value.
// using depth
db.child_reference.aggregate([
	{
		$match: { name: "Dev" },
	},
	{
		$graphLookup: {
			from: "child_reference",
			startWith: "$direct_reports",
			connectFromField: "direct_reports",
			connectToField: "name",
			as: "till_2_level_reports",
			maxDepth: 1,
		},
	},
]);

// how many recursive lookups did I use
// what level is it at
db.child_reference.aggregate([
	{
		$match: { name: "Dev" },
	},
	{
		$graphLookup: {
			from: "child_reference",
			startWith: "$direct_reports",
			connectFromField: "direct_reports",
			connectToField: "name",
			as: "till_2_level_reports",
			maxDepth: 1,
			depthField: "level",
		},
	},
]);

// multiple collections
db.air_airlines.aggregate([
	{
		$match: { name: "TAP Portugal" },
	},
	{
		$graphLookup: {
			from: "air_routes",
			startWith: "$base",
			connectFromField: "dst_airport",
			connectToField: "src_airport",
			as: "chain",
			maxDepth: 1,
		},
	},
]);

db.air_airlines.aggregate([
	{
		$match: { name: "TAP Portugal" },
	},
	{
		$graphLookup: {
			from: "air_routes",
			startWith: "$base",
			connectFromField: "dst_airport",
			connectToField: "src_airport",
			as: "chain",
			maxDepth: 1,
			restrictSearchWithMatch: { "airline.name": "TAP Portugal" },
		},
	},
]);
