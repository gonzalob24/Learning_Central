db.companies.aggregate([
	{
		$match: { $text: { $search: "network" } },
	},
]);

db.companies.aggregate([
	{
		$match: { $text: { $search: "network" } },
	},
	{
		$unwind: "$offices",
	},
	{
		$match: { "$offices.city": { $ne: "" } },
	},
	{
		$sortByCount: "$offices.city",
	},
]);

db.companies.aggregate([
	{
		$match: { founded_year: { $gt: 1980 }, number_of_employees: { $ne: null } },
	},

	{
		$bucket: {
			groupBy: "$number_of_employees",
			boundaries: [0, 20, 50, 100, 500, 1000, Infinity],
		},
	},
]);

// using $facets to run access data multiple times
db.movies.aggregate([
	{
		$match: {
			metacritic: { $gte: 0 },
			"imdb.rating": { $gte: 0 },
		},
	},
	{
		$sort: { "imdb.rating": -1, title: 1 },
	},
	{
		$limit: 10,
	},
	{
		$project: { title: 1 },
	},
]);

db.movies.aggregate([
	{
		$match: {
			metacritic: { $gte: 0 },
			"imdb.rating": { $gte: 0 },
		},
	},
	{
		$sort: { metacritic: -1, title: 1 },
	},
	{
		$limit: 10,
	},
	{
		$project: { title: 1 },
	},
]);

db.movies.aggregate([
	{
		$match: {
			metacritic: { $gte: 0 },
			"imdb.rating": { $gte: 0 },
		},
	},
	{
		$facet: {
			top_10_imdb: [
				{
					$sort: { "imdb.rating": -1, title: 1 },
				},
				{
					$limit: 10,
				},
				{
					$project: { title: 1 },
				},
			],
			top_10_metacritic: [
				{
					$sort: { metacritic: -1, title: 1 },
				},
				{
					$limit: 10,
				},
				{
					$project: { title: 1 },
				},
			],
		},
	},
	{
		$project: {
			movies_in_both_top_10: {
				$setIntersection: ["$top_10_imdb", "$top_10_metacritic"],
			},
		},
	},
]);
