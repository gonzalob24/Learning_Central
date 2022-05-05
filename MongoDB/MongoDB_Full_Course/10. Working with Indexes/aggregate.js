db.persons.aggregate([
	{ $match: { gender: "female" } },
	{ $group: { _id: { state: "$location.state" }, totalPersons: { $sum: 1 } } },
	{ $sort: { totalPersons: -1 } },
]);

db.persons.aggregate([
	{
		$project: {
			_id: 0,
			name: 1,
			email: 1,
			birthdate: { $toDate: "$dob.date" },
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
			email: 1,
			gender: 1,
			location: 1,
			birthdate: 1,
			age: 1,
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
					{ $toUpper: { $substrCP: ["$name.last", 0, 1] } },
					{
						$substrCP: [
							"$name.last",
							1,
							{ $subtract: [{ $strLenCP: "$name.last" }, 1] },
						],
					},
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

// group by age anc combine hobbies.
// combining array values: $push new elements into allHobbies for every incoming document
// this will push the entire array
// unwind stage to pull out elements:
// pass in element that holds an array: flattens the array by repeating the document
// with elements in array.
// with each iteration hobbies will be an individual item
// the new result will have multiple values in allHobbies array
db.friends.aggregate([
	{ $unwind: "$hobbies" },
	{ $group: { _id: { age: "$age" }, allHobbies: { $push: "$hobbies" } } },
]);

db.friends.aggregate([
	{ $unwind: "$hobbies" },
	{ $group: { _id: { age: "$age" }, allHobbies: { $addToSet: "$hobbies" } } },
]);

// examScores: out first value of array
// $slice: array, numberOfItemsIwant || [array, start, stop]
// like python I can use negative numbers
db.friends.aggregate([
	{ $project: { _id: 0, examScore: { $slice: ["$examScores", -1] } } },
]);

// how many exams each person took
db.friends.aggregate([
	{ $project: { _id: 0, numExams: { $size: "$examScores" } } },
]);

// tranform exam score to be an array using greater than a certain value
// $filter: certain elements in an array for score > 60
// input array I want to filter
// as: local variable name
// cond: condition --> expressions
// $sc -> looks for a field named sc
// use $$sc
// recall sc will be each object in array so use dot notation to get the score
db.friends.aggregate([
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

//only output the highest exam score for each person
db.friends.aggregate([
	{ $group: { _id: 0, examScores: { $push: "$examScores.score" } } },
	{ $project: { highestScore: { $max: examScores } } },
]);

// unwind array: think about this and then group by person
// examScores: field name
// $examScores: value of field name
// can sort by examScores.score or add a projection
db.friends.aggregate([
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
	{ $sort: { maxScore: -1 } },
]);

// understand the distribution of the data i have
// boundaries are the buckets
db.persons.aggregate([
	{
		$bucket: {
			groupBy: "$dob.age",
			boundaries: [0, 18, 30, 50, 80, 120],
			output: {
				numPersons: { $sum: 1 },
				averageAge: { $avg: "$dob.age" },
			},
		},
	},
]);

db.persons.aggregate([
	{
		$bucketAuto: {
			groupBy: "$dob.age",
			buckets: 5,
			output: {
				numPersons: { $sum: 1 },
				averageAge: { $avg: "$dob.age" },
			},
		},
	},
]);

// 10 persons with oldest birthday
// then the next 10
// order of sort, skip, limit matters
db.persons.aggregate([
	{
		$project: {
			_id: 0,
			name: { $concat: ["$name.first", " ", "$name.last"] },
			birthdate: { $toDate: "$dob.date" },
		},
	},
	{ $sort: { birthdate: 1 } },
	{ $skip: 10 },
	{ $limit: 10 },
]);

// I can match afterwards but I will have more data to work with in the pipeline
// match first to limit the data I am working with.
// if I match later make sure too include the gender in project
db.persons.aggregate([
	{ $match: { gender: "male" } },
	{
		$project: {
			_id: 0,
			name: { $concat: ["$name.first", " ", "$name.last"] },
			birthdate: { $toDate: "$dob.date" },
		},
	},
	{ $sort: { birthdate: 1 } },
	{ $skip: 10 },
	{ $limit: 10 },
	{ $out: "oldestMales" },
]);
