// findOne() finds the first document where condition is met
db.movies.findOne({});

// find gives back a courser
// find gives back all documents
db.movies.find();

// find queries on equality
db.movies.find({ name: "The Last Ship" });
db.movies.find({ runtime: 60 });

// Comparison operators
db.movies.find({ runtime: { $eq: 60 } }); // this is the same as the one above
// because mongo queries on equality by default
db.movies.find({ runtime: { $ne: 60 } });

db.movies.find({ runtime: { $lte: 42 } });

// embedded documents
// query a path using dot notation
db.movies.find({ "rating.average": { $gt: 7 } });

// query a field that is an array
// searching like this checks to see if drama is in the array
db.movies.find({ genres: "Drama" });
// Drama like this mongo looks to see if genres is the only one in the array
db.movies.find({ genres: ["Drama"] });

db.sales.find({
	$expr: {
		$gt: [
			{
				$cond: {
					if: { $gte: ["$volume", 190] },
					then: { $subtract: ["$volume", 10] },
					else: "$volume",
				},
			},
			"$target",
		],
	},
});
