/**
 * $match is the filter:
 */
const pipeline = [
	{ $match: { "location.address.state": "MN" } },
	{ $project: { "location.address.city": 1 } },
	{ $sort: { "location.address.city": 1 } },
	{ $limit: 3 },
];

const findTopRomanceMovies = () => {
	print("Finding top classic Romance Movies");

	const pipeline = [
		{
			$match: {
				genres: { $in: ["Romance"] },
				released: { $lte: new ISODate("2001-01-01T00:00:00Z") },
			},
		},
		{ $sort: { "imdb.rating": -1 } },
		{ $limit: 3 },
		{ $project: { title: 1, genres: 1, released: 1, imdb: 1 } },
	];

	const results = db.movies.aggregate(pipeline);
	print(results);
};

/**
 * group all by rating
 *
 */

const pipeline2 = [{ $group: { _id: "$rated" } }];

/**
 * identify total number of movies in each group
 */

const pipeline3 = [
	{
		$group: {
			_id: "$rated",
			numTiles: { $sum: 1 },
		},
	},
];

/**
 * finding the total runtime for every rating film in the collection
 *
 */

const pipeline4 = [
	{
		$group: {
			_id: "$rated",
			sumRuntime: { $sum: "$runtime" },
		},
	},
];

/**
 * calc the average runtime and $trunc the decimal to whole number
 */
const pipeline5 = [
	{
		$group: {
			_id: "$rated",
			avgRuntime: { $avg: "$runtime" },
		},
	},
	{
		$project: {
			roundedAvgTime: { $trunc: "$avgRuntime" },
		},
	},
];

/**
 * For only movies older than 2001, find the average and maximum popularity for each genre, sort the genres by popularity, and find the adjusted (with trailers) runtime of the longest movie in each genre.
 *
 * find the pipelines:
 * $match: {}
 * $group: {}
 * $sort: {}
 * $project: {}
 */

const pipeline6 = [
	{
		$match: {
			released: { $lt: new ISODate("2001-01-01T00:00:00Z") },
		},
	},
	{
		$group: {
			_id: { $arrayElemAt: ["$genres", 0] },
			popularity: { $avg: "$imdb.rating" },
			top_movie: { $max: "$imdb.rating" },
			longest_runtime: { $max: "$runtime" },
		},
	},
	{
		$sort: { popularity: -1 },
	},
	{
		$project: {
			_id: 1,
			popularity: 1,
			top_movie: 1,
			adjusted_runtime: { $add: ["$longest_runtime", 12] },
		},
	},
];

/**
 * $match: {}
 * $group: {}
 * $sort: {}
 * $projection: {}
 */

const pipeline7 = [
	{
		$match: {
			released: { $lte: new ISODate("2001-01-01T00:00:00Z") },
			runtime: { $lte: 218 },
			"imdb.rating": { $gte: 7.0 },
		},
	},
	{
		$sort: { "imdb.rating": -1 },
	},
	{
		$group: {
			_id: { $arrayElemAt: ["$genres", 0] },
			recommended_title: { $first: "$title" },
			recommended_rating: { $first: "$imdb.rating" },
			recommended_raw_runtime: { $first: "$runtime" },
			popularity: { $avg: "$imdb.rating" },
			top_movie: { $max: "$imdb.rating" },
			longest_runtime: { $max: "$runtime" },
		},
	},
	{
		$project: {
			_id: 1,
			popularity: 1,
			top_movie: 1,
			recommended_title: 1,
			recommended_rating: 1,
			recommended_raw_runtime: 1,
			adjusted_runtime: { $add: ["$longest_runtime", 12] },
		},
	},
];

const pipeline7_1 = [
	{
		$match: {
			released: { $lt: new ISODate("2001-01-01T00:00:00Z") },
			runtime: { $lt: 218 },
			"imdb.rating": { $gte: 7.0 },
		},
	},
	{
		$sort: { "imdb.rating": -1 },
	},
	{
		$group: {
			_id: { $arrayElemAt: ["$genres", 0] },
			recommended_title: { $first: "$title" },
			recommended_rating: { $first: "$imdb.rating" },
			recommended_raw_runtime: { $first: "$runtime" },
			popularity: { $avg: "$imdb.rating" },
			top_movie: { $max: "$imdb.rating" },
			longest_runtime: { $max: "$runtime" },
		},
	},
	{
		$project: {
			_id: 1,
			popularity: 1,
			top_movie: 1,
			recommended_title: 1,
			recommended_rating: 1,
			recommended_raw_runtime: 1,
			adjusted_runtime: { $add: ["$longest_runtime", 12] },
		},
	},
];

/**
 * using lookup
 */

const lookupExample = [
	{
		$match: { $or: [{ name: "Catelyn Stark" }, { name: "Ned Stark" }] },
	},
	{
		$lookup: {
			from: "comments",
			localField: "name",
			foreignField: "name",
			as: "comments",
		},
	},
	{ $limit: 2 },
];

/**
 * with unwind the comments are visible within the user object
 */
const lookupUnwindExample = [
	{
		$match: { $or: [{ name: "Catelyn Stark" }, { name: "Ned Stark" }] },
	},
	{
		$lookup: {
			from: "comments",
			localField: "name",
			foreignField: "name",
			as: "comments",
		},
	},
	{ $unwind: "$comments" },
	{ $limit: 2 },
];
