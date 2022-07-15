// Putting it together
// { "title" : "The Christmas Tree",
// "imdb" : { "rating" : 1.1, "votes" : 264 }, "normalized_rating" : 1.0507662218131615 }
db.movies.aggregate([
	{
		$match: {
			languages: { $in: ["English"] },
			"imdb.rating": { $gte: 1 },
			"imdb.votes": { $gte: 1 },
			year: { $gte: 1990 },
		},
	},
	{
		$addFields: {
			avg_rating: {
				$avg: [
					"$imdb.rating",
					{
						$add: [
							1,
							{
								$multiply: [
									9,
									{
										$divide: [
											{ $subtract: ["$imdb.votes", 5] },
											{ $subtract: [1521105, 5] },
										],
									},
								],
							},
						],
					},
				],
			},
		},
	},
	{
		$sort: {
			avg_rating: 1,
		},
	},
	{
		$project: {
			avg_rating: 1,
			title: 1,
			year: 1,
		},
	},
	{
		$limit: 1,
	},
]);
