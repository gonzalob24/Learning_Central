db.solarSystem.aggregate([{ $project: { gravity: "$gravity.value" } }]);

// this can be tedious
// so we can use $addFields to get the same results
db.solarSystem.aggregate([
	{
		$project: {
			_id: 0,
			gravity: "$gravity.value",
			name: 1,
			meanTemperature: 1,
			density: 1,
			mass: "$mass.value",
			radius: "$radius.value",
			sma: "$sma.value",
		},
	},
]);

// this does not remove the other fields it appends these ones as new ones
db.solarSystem.aggregate([
	{
		$addFields: {
			gravity: "$gravity.value",
			mass: "$mass.value",
			radius: "$radius.value",
			sma: "$sma.value",
		},
	},
]);

// these shows the fields we wish to retain, I don't need to go one by one for larger pipelines
db.solarSystem.aggregate([
	{
		$project: {
			_id: 0,
			name: 1,
			gravity: 1,
			mass: 1,
			radius: 1,
			sma: 1,
		},
	},
	{
		$addFields: {
			gravity: "$gravity.value",
			mass: "$mass.value",
			radius: "$radius.value",
			sma: "$sma.value",
		},
	},
]);

// collection needs a geo index
db.nycFacilities.aggregate([
	{
		$geoNear: {
			near: {
				type: "Point",
				coordinates: [-73.98769766092299, 40.757345233626594],
			},
			distanceField: "distanceFromMongoDB",
			spherical: true,
		},
	},
]);

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
]);

// Cursor Examples
// with find
db.solarSystem.find({}, { _id: 0, name: 1, numberOfMoons: 1 });

// using aggregate

// limit
db.solarSystem.aggregate([
	{ $project: { _id: 0, name: 1, numberOfMoons: 1 } },
	{ $limit: 5 },
]);

// skip
// this will project in natural order since I don't have a sort
db.solarSystem.aggregate([
	{ $project: { _id: 0, name: 1, numberOfMoons: 1 } },
	{ $skip: 1 },
]);

// count
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
	{ $count: "terrestrial planets" },
]);

// the project can be removed since I am not using it
db.solarSystem.aggregate([
	{
		$match: {
			type: "Terrestrial planet",
		},
	},
	{ $count: "terrestrial planets" },
]);

// sort: needs a field to sort on. Can sort on multiple fields
db.solarSystem.aggregate([
	{
		$project: {
			_id: 0,
			name: 1,
			numberOfMoons: 1,
		},
	},
	{
		$sort: { numberOfMoons: -1 },
	},
]);

// sort multiple fields
db.solarSystem.aggregate([
	{
		$project: {
			_id: 0,
			name: 1,
			numberOfMoons: 1,
			hasMagneticField: 1,
		},
	},
	{
		$sort: { hasMagneticField: -1, numberOfMoons: -1 },
	},
]);

// optimize the search using allowDiskUse: true
db.solarSystem.aggregate(
	[
		{
			$project: {
				_id: 0,
				name: 1,
				numberOfMoons: 1,
				hasMagneticField: 1,
			},
		},
		{
			$sort: { hasMagneticField: -1, numberOfMoons: -1 },
		},
	],
	{ allowDiskUse: true }
);

// $sample stage
db.nycFacilities.aggregate([
	{
		$sample: { size: 200 },
	},
]);

// using cursor like stages
const favorites = [
	"Sandra Bullock",
	"Tom Hanks",
	"Julia Roberts",
	"Kevin Spacey",
	"George Clooney",
];

db.movies.aggregate([
	{
		$match: {
			countries: "USA",
			"tomatoes.viewer.rating": { $gte: 3 },
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
			num_favs: {
				$setIntersection: ["$cast", favorites],
			},
		},
	},
	{
		$match: {
			num_favs: { $gt: [{ $size: "$num_favs" }, 1] },
		},
	},
]);

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
			title: 1,
			cast: 1,
			"tomatoes.viewer.rating": 1,
			countries: 1,
		},
	},
	{
		$addFields: {
			num_favs: {
				$size: { $setIntersection: ["$cast", favorites] },
			},
		},
	},
	{
		$sort: { num_favs: -1, "tomatoes.viewer.rating": -1, title: -1 },
	},
	{
		$skip: 24,
	},
	{
		$limit: 1,
	},
]);

// 573a1399f29313caabcec992

// Group stage
db.movies.aggregate([{ $group: { _id: "$year" } }]);

// using accumulation with group
db.movies.aggregate([
	{
		$group: {
			_id: "$year",
			num_films_in_year: { $sum: 1 },
		},
	},
	{
		$sort: {
			num_films_in_year: 1,
		},
	},
]);

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
