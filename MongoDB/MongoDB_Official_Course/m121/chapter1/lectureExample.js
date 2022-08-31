// Match: must come early in pipeline
// if using $text make sure it is in the first stage
// can't use $where in $match
db.solarSystem.aggregate([
	{ $match: { type: { $ne: "Star" } } },
	{ $count: "planets" },
]);

db.movies.aggregate([
	{
		$match: {
			"imdb.rating": { $gte: 7 },
			genres: { $nin: ["Crime", "Horror"] },
			rated: { $in: ["PG", "G"] },
			languages: { $all: ["English", "Japanese"] },
		},
	},
]);

// Project
db.solarSystem.aggregate([
	{ $project: { _id: 0, name: 1, "gravity.value": 1 } },
]);

db.solarSystem.aggregate([
	{ $project: { _id: 0, name: 1, surfaceGravity: "$gravity.value" } },
]);

db.solarSystem.aggregate([
	{
		$project: {
			_id: 0,
			name: 1,
			"gravity.value": 1,
			myWeight: { $multiply: [{ $divide: ["$gravity.value", 9.8] }, 86] },
		},
	},
]);

db.movies.aggregate([
	{
		$match: {
			"imdb.rating": { $gte: 7 },
			genres: { $nin: ["Crime", "Horror"] },
			rated: { $in: ["PG", "G"] },
			languages: { $all: ["English", "Japanese"] },
		},
	},
	{ $project: { _id: 0, title: 1, rated: 1 } },
]);

// Project and computing fields
db.movies.aggregate([
	{ $project: { _id: 0, titleArray: { $split: ["$title", " "] }, rated: 1 } },
	{ $match: { titleArray: { $size: 1 } } },
	{ $project: { title: { $first: "$titleArray" }, rated: 1 } },
]);

db.movies.aggregate([
	{ $match: { writers: { $elemMatch: { $exists: true } } } },
]);

db.movies.aggregate([
	{ $match: { writers: { $elemMatch: { $exists: true } } } },
	{
		$project: {
			writers: {
				$map: {
					input: "$writers",
					as: "writer",
					in: {
						$arrayElemAt: [{ $split: ["$$writer", " ("] }, 0],
					},
				},
			},
		},
	},
]);

// Labor of love
// check if the fields exist
db.movies.aggregate([
	{
		$match: {
			cast: { $elemMatch: { $exists: true } },
			writers: { $elemMatch: { $exists: true } },
			directors: { $elemMatch: { $exists: true } },
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
					in: {
						$arrayElemAt: [{ $split: ["$$writer", " ("] }, 0],
					},
				},
			},
		},
	},
	{
		$project: {
			lol: {
				$setIntersection: ["$writers", "$cast", "$directors"],
			},
		},
	},
	{
		$project: {
			lol: { $gt: [{ $size: "$lol" }, 0] },
		},
	},
	{
		$match: { lol: true },
	},
	{ $count: "love" },
]);
