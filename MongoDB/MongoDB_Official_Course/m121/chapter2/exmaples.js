// $geoNear must come first in the pipeline
db.nycFacilities.aggregate([
	{
		$geoNear: {
			near: {
				type: "Point",
				coordinates: [-73.98769766092299, 40.757345233626594],
			},
			distanceField: "distanceFromMongoDB",
			spherical: true,
			query: { type: "Hospital" },
		},
	},
	{
		$limit: 5,
	},
]);

db.solarSystem.aggregate([
	{
		$match: {
			type: "Terrestrial planet",
		},
	},
	{
		$project: {
			_id: 0,
			name: 1,
			numberOfMoons: 1,
		},
	},
	{
		$limit: 3,
	},
	{
		$skip: 2,
	},
]);
db.solarSystem.aggregate([]);

db.solarSystem.aggregate([
	{
		$match: {
			type: "Terrestrial planet",
		},
	},
	{
		$project: {
			_id: 0,
			name: 1,
			numberOfMoons: 1,
		},
	},
	{
		$count: "terrestrial planets",
	},
]);

const favorites = [
	"Sandra Bullock",
	"Tom Hanks",
	"Julia Roberts",
	"Kevin Spacey",
	"George Clooney",
];

// movie collection
db.movies.aggregate([
	{
		$match: {
			countries: "USA",
			"tomatoes.viewer.rating": { $gte: 3 },
			cast: { $in: favorites },
		},
	},
	{
		$project: {
			cast: 1,
			title: 1,
			"tomatoes.viewer.rating": 1,
		},
	},
	{
		$addFields: {
			num_fav: { $size: { $setIntersection: ["$cast", favorites] } },
		},
	},
	{
		$sort: { num_fav: -1, "tomatoes.viewer.rating": -1, title: -1 },
	},
	{
		$skip: 24,
	},
	{
		$limit: 1,
	},
]);

db.movies.aggregate([
	{
		$match: {
			languages: { $elemMatch: { $exists: true } },
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
		$sort: { normalized_rating: 1 },
	},
	{
		$project: { _id: 0, title: 1 },
	},
	{
		$limit: 1,
	},
]);
