db.movies.aggregate([
	{
		$match: {
			cast: { $elemMatch: { $exists: true } },
			directors: { $elemMatch: { $exists: true } },
			writers: { $elemMatch: { $exists: true } },
		},
	},
	{
		$project: {
			_id: 0,
			cast: 1,
			directors: 1,
			writers: {
				$map: {
					input: "$writers",
					as: "writer",
					in: { $arrayElemAt: [{ $split: ["$$writer", " ("] }, 0] },
				},
			},
		},
	},
	{
		$project: {
			lol: {
				$gt: [
					{ $size: { $setIntersection: ["$cast", "$directors", "$writers"] } },
					0,
				],
			},
		},
	},
	{ $match: { lol: true } },
	{ $count: "labors of love" },
])[{ "labors of love": 1596 }];
