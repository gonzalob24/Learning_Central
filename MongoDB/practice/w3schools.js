/****************** https://www.w3resource.com/mongodb-exercises/ ******************/
/***********************************************************************************/

// 1. Write a MongoDB query to display all the documents in the collection restaurants.
db.restaurants.aggregate([{ $group: { _id: "_id", count: { $sum: 1 } } }]);
db.restaurants.find().count();

// 2. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.
db.restaurants.aggregate([
	{ $project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1 } },
]);

// 3. Write a MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant.
db.restaurants.aggregate([
	{ $project: { _id: 0, restaurant_id: 1, name: 1, borough: 1, cuisine: 1 } },
]);

// 4. Write a MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant.
db.restaurants.aggregate([
	{
		$project: {
			_id: 0,
			restaurant_id: 1,
			name: 1,
			borough: 1,
			zipcode: "$address.zipcode",
		},
	},
]);

// 5. Write a MongoDB query to display all the restaurant which is in the borough Bronx.
db.restaurants.aggregate([{ $match: { borough: "Bronx" } }]);

// 6. Write a MongoDB query to display the first 5 restaurant which is in the borough Bronx.
db.restaurants.aggregate([{ $match: { borough: "Bronx" } }, { $limit: 5 }]);

// 7.Write a MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx.
db.restaurants.aggregate([
	{ $match: { borough: "Bronx" } },
	{ $skip: 5 },
	{ $limit: 5 },
]);

// 8. Write a MongoDB query to find the restaurants who achieved a score more than 90.
// both of these return documents where any score is greater than 90.
db.restaurants.aggregate([{ $match: { "grades.score": { $gt: 90 } } }]);

db.restaurants.find({ grades: { $elemMatch: { score: { $gt: 90 } } } });

// this method will return docments where this condition is met.
// https://www.mongodb.com/docs/manual/reference/operator/query/elemMatch/
db.restaurants.find({ "grades.score": { $gt: 90 } });

// 9. Write a MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100.
db.restaurants.find({
	grades: { $elemMatch: { score: { $gt: 80, $lt: 100 } } },
});

db.restaurants.aggregate([
	{
		$match: {
			grades: { $elemMatch: { score: { $gt: 80, $lt: 100 } } },
		},
	},
]);

db.restaurants.aggregate([
	{
		$match: {
			grades: { $elemMatch: { score: { $gt: 80, $lt: 100 } } },
		},
	},
	{ $count: "total" },
]);

// thid does not work because this says as long as there is a document in grades that meets the condition
// return the entire document.
db.restaurants.aggregate([
	{ $match: { "grades.score": { $gt: 80, $lt: 100 } } },
]);

// 10. Write a MongoDB query to find the restaurants which locate in latitude value less than -95.754168.
// the dot notation for indexing arrays works for first level only not nested arrays
db.restaurants.aggregate([
	{ $match: { "address.coord.0": { $lt: -95.754168 } } },
]);

// 11. Write a MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168.
db.restaurants.aggregate([
	{
		$match: {
			cuisine: { $ne: "American " },
			grades: { $elemMatch: { score: { $gt: 70 } } },
			"address.coord": { $lt: -65.754168 },
		},
	},
]);

// 12. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168.
// Note : Do this query without using $and operator.
// same as above
db.restaurants.aggregate([
	{
		$match: {
			cuisine: { $ne: "American " },
			grades: { $elemMatch: { score: { $gt: 70 } } },
			"address.coord": { $lt: -65.754168 },
		},
	},
]);

// 13. Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American ' and achieved a grade point 'A' not belongs to the borough Brooklyn. The document must be displayed according to the cuisine in descending order.
// FOR LATER: only return embedded documents in grades array with grade A.
db.restaurants.aggregate([
	{
		$match: {
			cuisine: { $ne: "American " },
			grades: { $elemMatch: { grade: "A" } },
			borough: { $ne: "Brooklyn" },
		},
	},
	{ $sort: { cuisine: -1 } },
]);

// 14. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name.
db.restaurants.aggregate([
	{
		$match: {
			name: { $regex: "^Wil" },
		},
	},
	{
		$project: {
			restaurant_id: 1,
			borough: 1,
			cuisine: 1,
			name: 1,
		},
	},
]);

// 15. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'ces' as last three letters for its name.
db.restaurants.aggregate([
	{ $match: { name: { $regex: "ces$" } } },
	{
		$project: {
			restaurant_id: 1,
			borough: 1,
			cuisine: 1,
			name: 1,
		},
	},
]);

// 16. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which contain 'Reg' as three letters somewhere in its name.
db.restaurants.aggregate([
	{ $match: { name: { $regex: ".*Res.*" } } },
	{ $project: { restaurant_id: 1, borough: 1, cuisine: 1, name: 1 } },
]);

// 17. Write a MongoDB query to find the restaurants which belong to the borough Bronx and prepared either American or Chinese dish.
db.restaurants.aggregate([
	{
		$match: {
			borough: "Bronx",
			$or: [{ cuisine: "American " }, { cuisine: "Chinese" }],
		},
	},
]);

// 18. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronxor Brooklyn.
db.restaurants.aggregate([
	{
		$match: {
			$or: [
				{ borough: "Staten Island" },
				{ borough: "Queens" },
				{ borough: "Bronxor Brooklyn" },
			],
		},
	},
	{ $project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1 } },
]);

db.restaurants.aggregate([
	{
		$match: {
			borough: { $in: ["Staten Island", "Queens", "Bronxor Brooklyn"] },
		},
	},
	{ $project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1 } },
]);

// 19. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn.
db.restaurants.aggregate([
	{
		$match: {
			borough: { $nin: ["Staten Island", "Queens", "Bronxor Brooklyn"] },
		},
	},
	{ $project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1 } },
]);

// 20. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which achieved a score which is not more than 10.
db.restaurants.aggregate([
	{ $match: { grades: { $elemMatch: { score: { $not: { $gt: 10 } } } } } },
	{ $project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1 } },
]);
db.restaurants.aggregate([
	{ $match: { grades: { $elemMatch: { score: { $not: { $gt: 10 } } } } } },
	{ $count: "total" },
]);
db.restaurants.aggregate([
	{ $match: { grades: { $elemMatch: { score: { $not: { $gt: 10 } } } } } },
	{ $project: { name: 1, grades: 1 } },
]);
// LOOK AT THE DIFFERENCE BETWEEN THESE TWO QUERIES UP AND DOWN
db.restaurants.aggregate([
	{ $match: { "grades.score": { $not: { $gt: 10 } } } },
	{ $count: "total" },
]);
db.restaurants.aggregate([
	{ $match: { "grades.score": { $not: { $gt: 10 } } } },
	{ $project: { name: 1, grades: 1 } },
]);

db.restaurants.find(
	{ "grades.score": { $not: { $gt: 10 } } },
	{
		restaurant_id: 1,
		name: 1,
		borough: 1,
		cuisine: 1,
	}
);

// 21. Write a MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants which prepared dish except 'American' and 'Chinees' or restaurant's name begins with letter 'Wil'.
db.restaurants.aggregate([
	{
		$match: {
			$or: [
				{ cuisine: { $nin: ["American ", "Chinees"] } },
				{ name: { $regex: "^Wil" } },
			],
		},
	},
	{ $project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1 } },
]);

db.restaurants.aggregate([
	{
		$match: {
			$or: [
				{
					$and: [
						{ cuisine: { $ne: "American " } },
						{ cuisine: { $ne: "Chinees" } },
					],
				},
				{ name: { $regex: "^Wil" } },
			],
		},
	},
	{ $count: "total" },
]);

db.restaurants.aggregate([
	{
		$match: {
			$or: [
				{ cuisine: { $nin: ["American ", "Chinees"] } },
				{ name: { $regex: "^Wil" } },
			],
		},
	},
	{ $count: "total" },
]);

db.restaurants.find(
	{
		$or: [
			{ name: /^Wil/ },
			{
				$and: [
					{ cuisine: { $ne: "American " } },
					{ cuisine: { $ne: "Chinees" } },
				],
			},
		],
	},
	{ restaurant_id: 1, name: 1, borough: 1, cuisine: 1 }
);

// 22. Write a MongoDB query to find the restaurant Id, name, and grades for those restaurants which achieved a grade of "A" and scored 11 on an ISODate "2014-08-11T00:00:00Z" among many of survey dates..
// WHEN FACING THESE QUERIES:
// ASK: DO WE WANT TO GET ONLY DOCUMENTS THAT MATCH THE QUERY CONDITION EXACTLY?
db.restaurants.aggregate([
	{
		$match: {
			grades: { $elemMatch: { grade: "A" } },
			grades: { $elemMatch: { score: 11 } },
			grades: { $elemMatch: { date: ISODate("2014-08-11T00:00:00Z") } },
		},
	},
	{
		$project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1, grades: 1 },
	},
]);

db.restaurants.aggregate([
	{
		$match: {
			$and: [
				{ grades: { $elemMatch: { grade: "A" } } },
				{ grades: { $elemMatch: { score: 11 } } },
				{ grades: { $elemMatch: { date: ISODate("2014-08-11T00:00:00Z") } } },
			],
		},
	},
	{
		$project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1, grades: 1 },
	},
]);

db.restaurants.aggregate([
	{
		$match: {
			$and: [
				{ grades: { $elemMatch: { grade: "A" } } },
				{ grades: { $elemMatch: { score: 11 } } },
				{ grades: { $elemMatch: { date: ISODate("2014-08-11T00:00:00Z") } } },
			],
		},
	},
	{ $count: "total" },
]);

db.restaurants.aggregate([
	{
		$match: {
			"grades.grade": "A",
			"grades.score": 11,
			"grades.date": ISODate("2014-08-11T00:00:00Z"),
		},
	},
	{
		$project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1, grades: 1 },
	},
]);

db.restaurants.aggregate([
	{
		$match: {
			"grades.grade": "A",
			"grades.score": 11,
			"grades.date": ISODate("2014-08-11T00:00:00Z"),
		},
	},
	{ $count: "total" },
]);

db.restaurants.find(
	{
		"grades.date": ISODate("2014-08-11T00:00:00Z"),
		"grades.grade": "A",
		"grades.score": 11,
	},
	{ restaurant_id: 1, name: 1, borough: 1, cuisine: 1, grades: 1 }
);

db.restaurants.aggregate([
	{
		$match: {
			grades: { $elemMatch: { grade: "A" } },
			grades: { $elemMatch: { score: 11 } },
			grades: { $elemMatch: { date: ISODate("2014-08-11T00:00:00Z") } },
		},
	},
	{
		$count: "total",
	},
]);

db.restaurants.find(
	{
		"grades.grade": "A",
		"grades.score": 11,
		"grades.date": ISODate("2014-08-11T00:00:00Z"),
	},
	{ restaurant_id: 1, name: 1, borough: 1, cuisine: 1, grades: 1 }
);

// 23. Write a MongoDB query to find the restaurant Id, name and grades for those restaurants where the 2nd element of grades array contains a grade of "A" and score 9 on an ISODate "2014-08-11T00:00:00Z".
db.restaurants.aggregate([
	{
		$match: {
			"grades.1.date": ISODate("2014-08-11T00:00:00Z"),
			"grades.1.grade": "A",
			"grades.1.score": 9,
		},
	},
	{
		$project: { restaurant_id: 1, name: 1, borough: 1, cuisine: 1, grades: 1 },
	},
]);

db.restaurants.aggregate([
	{
		$match: {
			"grades.1.date": ISODate("2014-08-11T00:00:00Z"),
			"grades.1.grade": "A",
			"grades.1.score": 9,
		},
	},
	{
		$count: "Total",
	},
]);

db.restaurants.find(
	{
		"grades.1.date": ISODate("2014-08-11T00:00:00Z"),
		"grades.1.grade": "A",
		"grades.1.score": 9,
	},
	{ restaurant_id: 1, name: 1, grades: 1 }
);

// 24. Write a MongoDB query to find the restaurant Id, name, address and geographical location for those restaurants where 2nd element of coord array contains a value which is more than 42 and upto 52..
db.restaurants.aggregate([
	{
		$match: {
			"address.coord.1": { $gt: 42, $lt: 52 },
		},
	},
	{ $project: { restaurant_id: 1, name: 1, address: 1 } },
]);

db.restaurants.aggregate([
	{
		$match: {
			"address.coord.1": { $gt: 42, $lt: 52 },
		},
	},
	{ $count: "Total" },
]);

db.restaurants.find(
	{
		"address.coord.1": { $gt: 42, $lte: 52 },
	},
	{ restaurant_id: 1, name: 1, address: 1, coord: 1 }
);
// 25. Write a MongoDB query to arrange the name of the restaurants in ascending order along with all the columns.
db.restaurants.aggregate([{ $sort: { name: 1 } }]);
db.restaurants.find().sort({ name: 1 });

// 26. Write a MongoDB query to arrange the name of the restaurants in descending along with all the columns.
db.restaurants.aggregate([{ $sort: { name: -1 } }]);
db.restaurants.find().sort({ name: -1 });

// 27. Write a MongoDB query to arranged the name of the cuisine in ascending order and for that same cuisine borough should be in descending order.
db.restaurants.aggregate([{ $sort: { cuisine: 1, borough: -1 } }]);
db.restaurants.find().sort({ cuisine: 1, borough: -1 });

// 28. Write a MongoDB query to know whether all the addresses contains the street or not.
db.restaurants.aggregate([{ $match: { "address.street": { $exists: true } } }]);

db.restaurants.aggregate([
	{ $match: { "address.street": { $exists: true } } },
	{ $count: "total" },
]);

db.restaurants.find({ "address.street": { $exists: true } });

// 29. Write a MongoDB query which will select all documents in the restaurants collection where the coord field value is Double.
db.restaurants.aggregate([{ $match: { "address.coord": { $type: 1 } } }]);

db.restaurants.aggregate([
	{ $match: { "address.coord": { $type: 1 } } },
	{ $count: "Total" },
]);

db.restaurants.find({ "address.coord": { $type: 1 } });
// 30. Write a MongoDB query which will select the restaurant Id, name and grades for those restaurants which returns 0 as a remainder after dividing the score by 7.
db.restaurants.aggregate([
	{ $match: { "grades.score": { $mod: [7, 0] } } },
	{ $project: { restaurant_id: 1, name: 1, grades: 1 } },
]);

// LOOK IN TO ACCESS EACH ELEMENT IN THE ARRAY AND DOING SOMETHING WITH THAT VALUE
db.restaurants.aggregate([
	{ $match: { "grades.score": { $mod: [7, 0] } } },
	{ $count: "Total" },
]);

db.restaurants.find(
	{ "grades.score": { $mod: [7, 0] } },
	{ restaurant_id: 1, name: 1, grades: 1 }
);
// 31. Write a MongoDB query to find the restaurant name, borough, longitude and attitude and cuisine for those restaurants which contains 'mon' as three letters somewhere in its name.

// 32. Write a MongoDB query to find the restaurant name, borough, longitude and latitude and cuisine for those restaurants which contain 'Mad' as first three letters of its name.
