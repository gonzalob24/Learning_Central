/**
 * $match
 */

db.contacts.aggregate([{ $match: { age: { $gt: 30 } } }]);

/**
 * find sum of persons living in a state
 * _id: defines which fields I want to group by
 *
 * $ --> refers to field of document
 *
 * can add an accumulator in group, for every document that is grouped together
 */
db.contacts.aggregate([
	{ $match: { gender: "female" } },
	{ $group: { _id: { state: "$location.state" }, totalPersons: { $sum: 1 } } },
]);

/**
 * more grouping
 * $sort
 */
db.contacts.aggregate([
	{ $match: { gender: "female" } },
	{ $group: { _id: { state: "$location.state" }, totalPersons: { $sum: 1 } } },
	{ $sort: { totalPersons: -1 } },
]);

/**
 * transform data with project
 * transform the name --> fullName
 * $ --> refers to field of current document
 *
 * $toUpper --> everything is upper
 */
db.contacts.aggregate([
	{
		$project: {
			_id: 0,
			gender: 1,
			fullName: {
				$concat: [{ $toUpper: "$name.first" }, " ", { $toUpper: "$name.last" }],
			},
		},
	},
]);

db.contacts.aggregate([
	{
		$project: {
			_id: 0,
			gender: 1,
			fullName: {
				$concat: [
					{ $toUpper: { $substrCP: ["$name.first", 0, 1] } },
					{
						$substrCP: [
							"$name.first",
							1,
							{ $subtract: [{ $strLenCP: "$name.first" }, 1] },
						],
					},
					" ",
					{ $toUpper: "$name.last" },
				],
			},
		},
	},
]);

/**
 * More projection
 *
 * for birthdate I can also use toDate
 *
 * use convert for error handling
 */

db.contacts.aggregate([
	{
		$project: {
			_id: 0,
			name: 1,
			email: 1,
			birthdate: { $convert: { input: "$dob.date", to: "date" } },
			age: "$dob.age",
			location: {
				type: "Point",
				coordinates: [
					{
						$convert: {
							input: "$location.coordinates.longitude",
							to: "double",
							onError: 0.0,
							onNull: 0.0,
						},
					},
					{
						$convert: {
							input: "$location.coordinates.latitude",
							to: "double",
							onError: 0.0,
							onNull: 0.0,
						},
					},
				],
			},
		},
	},
	{
		$project: {
			gender: 1,
			email: 1,
			birthdate: 1,
			age: 1,
			location: 1,
			fullName: {
				$concat: [
					{ $toUpper: { $substrCP: ["$name.first", 0, 1] } },
					{
						$substrCP: [
							"$name.first",
							1,
							{ $subtract: [{ $strLenCP: "$name.first" }, 1] },
						],
					},
					" ",
					{ $toUpper: "$name.last" },
				],
			},
		},
	},
]);

/**
 * adding a group stage
 */
db.contacts.aggregate([
	{
		$project: {
			_id: 0,
			name: 1,
			email: 1,
			birthdate: { $convert: { input: "$dob.date", to: "date" } },
			age: "$dob.age",
			location: {
				type: "Point",
				coordinates: [
					{
						$convert: {
							input: "$location.coordinates.longitude",
							to: "double",
							onError: 0.0,
							onNull: 0.0,
						},
					},
					{
						$convert: {
							input: "$location.coordinates.latitude",
							to: "double",
							onError: 0.0,
							onNull: 0.0,
						},
					},
				],
			},
		},
	},
	{
		$project: {
			gender: 1,
			email: 1,
			birthdate: 1,
			age: 1,
			location: 1,
			fullName: {
				$concat: [
					{ $toUpper: { $substrCP: ["$name.first", 0, 1] } },
					{
						$substrCP: [
							"$name.first",
							1,
							{ $subtract: [{ $strLenCP: "$name.first" }, 1] },
						],
					},
					" ",
					{ $toUpper: "$name.last" },
				],
			},
		},
	},
	{
		$group: {
			_id: { birthYear: { $isoWeekYear: "$birthdate" } },
			numPersons: { $sum: 1 },
		},
	},
	{ $sort: { numPersons: -1 } },
]);

/**
 * push  all items into allHobbies: allHobbies is an array of arrays
 */

db.persons.aggregate([
	{ $group: { _id: { age: "$age" }, allHobbies: { $push: "$hobbies" } } },
]);

/**
 * pushing values from an array to another array
 * unwind: pass in field name: flattens out the array, spits out multiple documents
 */

db.persons.aggregate([
	{ $unwind: "$hobbies" },
	{ $group: { _id: { age: "$age" }, allHobbies: { $push: "$hobbies" } } },
]);

/**
 * remove duplicate values
 * $addToSet
 */

db.persons.aggregate([
	{ $unwind: "$hobbies" },
	{ $group: { _id: { age: "$age" }, allHobbies: { $addToSet: "$hobbies" } } },
]);

/**
 * using projection with arrays
 *
 */
db.persons.aggregate([
	{ $project: { _id: 0, examScores: { $slice: ["$examScores", 1] } } },
]);

/**
 * size of an array
 */

db.persons.aggregate([
	{ $project: { _id: 0, numScores: { $size: "$examScores" } } },
]);

/**
 * filter: filter out certain elements in the array based on some condition
 * -
 * $ --> looks for field name of current document
 * $$ --> used to access the temp variable of current document
 */

db.persons.aggregate([
	{
		$project: {
			_id: 0,
			examScores: {
				$filter: {
					input: "$examScores",
					as: "sc",
					cond: { $gt: ["$$sc.score", 60] },
				},
			},
		},
	},
]);

/**
 * output highest exam score for every person
 *
 */

db.persons.aggregate([
	{ $unwind: "$examScores" },
	{ $project: { _id: 1, name: 1, age: 1, score: "$examScores.score" } },
	{ $sort: { score: -1 } },
	{
		$group: {
			_id: "$_id",
			name: { $first: "$name" },
			maxScore: { $max: "$score" },
		},
	},
]);