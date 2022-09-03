/**
 * Problem: Now that you have been introduced to $graphLookup, let's use it to solve an interesting need. 
 * You are working for a travel agency and would like to find routes for a client! For this exercise, 
 * we'll be using the air_airlines, air_alliances, and air_routes collections in the aggregations database.

Determine the approach that satisfies the following question in the most efficient manner:

Find the list of all possible distinct destinations, with at most one layover, departing from the base airports of airlines from Germany, Spain or Canada that are part of the "OneWorld" alliance. Include both the destination and which airline services that location. As a small hint, you should find 158 destinations.

 */

db.air_airlines.aggregate([
	{
		$match: { country: { $in: ["Germany", "Spain", "Canada"] } },
	},
]);

db.air_alliances.aggregate([
	{
		$match: { name: "OneWorld" },
	},
]);

// first
db.air_airlines.aggregate([
	{ $match: { country: { $in: ["Spain", "Germany", "Canada"] } } },
	{
		$lookup: {
			from: "air_alliances",
			foreignField: "airlines",
			localField: "name",
			as: "alliance",
		},
	},
	{ $match: { "alliance.name": "OneWorld" } },
	{
		$graphLookup: {
			startWith: "$base",
			from: "air_routes",
			connectFromField: "dst_airport",
			connectToField: "src_airport",
			as: "connections",
			maxDepth: 1,
		},
	},
	{ $project: { "connections.dst_airport": 1 } },
	{ $unwind: "$connections" },
	{ $group: { _id: "$connections.dst_airport" } },
]);

db.air_airlines.aggregate([
	{ $match: { country: { $in: ["Spain", "Germany", "Canada"] } } },
	{
		$lookup: {
			from: "air_alliances",
			foreignField: "airlines",
			localField: "name",
			as: "alliance",
		},
	},
	{ $match: { "alliance.name": "OneWorld" } },
	{
		$graphLookup: {
			startWith: "$base",
			from: "air_routes",
			connectFromField: "dst_airport",
			connectToField: "src_airport",
			as: "connections",
			maxDepth: 1,
		},
	},
	{ $project: { "connections.dst_airport": 1 } },
	{ $unwind: "$connections" },
	{ $group: { _id: "$connections.dst_airport" } },
]);

// second
var airlines = [];
db.air_alliances.find({ name: "OneWorld" }).forEach(function (doc) {
	airlines = doc.airlines;
});
var oneWorldAirlines = db.air_airlines.find({ name: { $in: airlines } });

oneWorldAirlines.forEach(function (airline) {
	db.air_alliances.aggregate([
		{
			$graphLookup: {
				startWith: airline.base,
				from: "air_routes",
				connectFromField: "dst_airport",
				connectToField: "src_airport",
				as: "connections",
				maxDepth: 1,
			},
		},
	]);
});

// third
db.air_alliances.aggregate([
	{
		$match: { name: "OneWorld" },
	},
	{
		$graphLookup: {
			startWith: "$airlines",
			from: "air_airlines",
			connectFromField: "name",
			connectToField: "name",
			as: "airlines",
			maxDepth: 0,
			restrictSearchWithMatch: {
				country: { $in: ["Germany", "Spain", "Canada"] },
			},
		},
	},
	{
		$graphLookup: {
			startWith: "$airlines.base",
			from: "air_routes",
			connectFromField: "dst_airport",
			connectToField: "src_airport",
			as: "connections",
			maxDepth: 1,
		},
	},
	{
		$project: {
			validAirlines: "$airlines.name",
			"connections.dst_airport": 1,
			"connections.airline.name": 1,
		},
	},
	{ $unwind: "$connections" },
	{
		$project: {
			isValid: { $in: ["$connections.airline.name", "$validAirlines"] },
			"connections.dst_airport": 1,
		},
	},
	{ $match: { isValid: true } },
	{ $group: { _id: "$connections.dst_airport" } },
]);

// fourth
db.air_routes.aggregate([
	{
		$lookup: {
			from: "air_alliances",
			foreignField: "airlines",
			localField: "airline.name",
			as: "alliance",
		},
	},
	{ $match: { "alliance.name": "OneWorld" } },
	{
		$lookup: {
			from: "air_airlines",
			foreignField: "name",
			localField: "airline.name",
			as: "airline",
		},
	},
	{
		$graphLookup: {
			startWith: "$airline.base",
			from: "air_routes",
			connectFromField: "dst_airport",
			connectToField: "src_airport",
			as: "connections",
			maxDepth: 1,
		},
	},
	{ $project: { "connections.dst_airport": 1 } },
	{ $unwind: "$connections" },
	{ $group: { _id: "$connections.dst_airport" } },
]);

/// third steps
// returns one match
db.air_alliances.aggregate([
	{
		$match: { name: "OneWorld" },
	},
]);

// this will replace the airlines array with airlines2
db.air_airlines.aggregate([
	{
		$match: { country: { $in: ["Spain", "Germany", "Canada"] } },
	},
]);

// graphLookup:
// startWith: value in current collection field --> airlines
// connectFromField: initial value will be what is designated in the startWith. if it is an array it will iterate all of the values used to match with connectToField. First value is Air Berline this name "From" will be used to match to the "To" when searching in the air_airlines collection.
// connectToField: used to match the connectFromField
db.air_alliances.aggregate([
	{
		$match: { name: "OneWorld" },
	},
	{
		$graphLookup: {
			startWith: "$airlines",
			from: "air_airlines",
			connectFromField: "name",
			connectToField: "name",
			as: "airlines2",
			maxDepth: 0,
			restrictSearchWithMatch: {
				country: { $in: ["Germany", "Spain", "Canada"] },
			},
		},
	},
]);

db.air_alliances.aggregate([
	{
		$match: { name: "OneWorld" },
	},
	{
		$graphLookup: {
			startWith: "$airlines",
			from: "air_airlines",
			connectFromField: "name",
			connectToField: "name",
			as: "airlines2",
			maxDepth: 0,
			restrictSearchWithMatch: {
				country: { $in: ["Germany", "Spain", "Canada"] },
			},
		},
	},
	{
		$graphLookup: {
			startWith: "$airlines2.base",
			from: "air_routes",
			connectFromField: "dst_airport",
			connectToField: "src_airport",
			as: "connections",
			maxDepth: 1,
		},
	},
	{
		$project: {
			validAirlines: "$airlines2.name",
			"connections.dst_airport": 1,
			"connections.airline.name": 1,
		},
	},
	{ $unwind: "$connections" },
	{
		$project: {
			isValid: { $in: ["$connections.airline.name", "$validAirlines"] },
			"connections.dst_airport": 1,
		},
	},
	{ $match: { isValid: true } },
	{ $group: { _id: "$connections.dst_airport" } },
]);
