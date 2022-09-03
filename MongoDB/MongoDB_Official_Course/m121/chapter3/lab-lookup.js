/**
 * Problem:
 * Which alliance from air_alliances flies the most routes with either
 * a Boeing 747 or an Airbus A380 (abbreviated 747 and 380 in air_routes)?
 */

// this was my solution!!!
db.air_alliances.aggregate(
	[
		{
			$match: {
				name: { $in: ["SkyTeam", "Star Alliance", "OneWorld"] },
			},
		},
		{
			$lookup: {
				from: "air_routes",
				localField: "airlines",
				foreignField: "airline.name",
				as: "airlines",
			},
		},
		{
			$unwind: "$airlines",
		},
		{
			$match: { "airlines.airplane": /747|380/ },
		},
		{
			$group: {
				_id: "$name",
				count: { $sum: 1 },
			},
		},
	],
	{ allowDiskUse: true }
);

db.air_alliances.aggregate(
	[
		{
			$match: {
				name: { $in: ["SkyTeam", "Star Alliance", "OneWorld"] },
			},
		},
		{
			$lookup: {
				from: "air_routes",
				localField: "airlines",
				foreignField: "airline.name",
				as: "alliance",
			},
		},
		{
			$match: { airlines: { airplane: /747|380/ } },
		},
	],
	{ allowDiskUse: true }
);

db.air_routes.aggregate([{}]);

db.air_routes.aggregate([
	{
		$match: { airplane: /747|380/ },
	},
	{
		$lookup: {
			from: "air_alliances",
			localField: "airline.name",
			foreignField: "airlines",
			as: "alliance",
		},
	},
	{
		$unwind: "$alliance",
	},
	{
		$group: {
			_id: "$alliance.name",
			count: { $sum: 1 },
		},
	},
]);
