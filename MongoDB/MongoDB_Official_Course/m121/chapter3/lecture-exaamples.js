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
