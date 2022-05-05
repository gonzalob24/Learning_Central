/*
 * Amit Phaltankar
 * 16/08/2020
 *
 * Packt MongoDB For Begginers.
 * Chapter 6
 */

// Activity code for Packt MongoDB For Begginers.
// Activity 6.03 Update Directors name

/**
 * Your task for this activity
 * 1. Prepare and execute an update command
 * 2. Filter all the movies where H. C. Potter is a director
 * 3. Create an identifier for elements of directors array where value of the element is H. C. Potter
 * 3. Use the idenfier to write an update expression and change the element value to Henry Codman Potter
 *
 */
db.movies.updateMany(
	{ directors: "H.C. Potter" },
	{
		$set: {
			"directors.$[hcPotter]": "Henry Codman Potter",
		},
	},
	{
		arrayFilters: [{ hcPotter: "H.C. Potter" }],
	}
);
/**
 * set is the update operator
 * use .$[name] to to change specific elements only
 *
 * arrayFilters define the identifier
 */
db.movies.updateMany(
	{ directors: { $in: ["H.C. Potter"] } },
	{ $set: { "directors.$[hcPotter]": "H.C. Potter (Henry Codman Potter)" } },
	{ returnNewDocument: true, arrayFilters: [{ hcPotter: "H.C. Potter" }] }
);

db.items.findOneAndUpdate(
	{ _id: 11 },
	{
		$set: {
			"items.$[markerField]": { name: "Big Marker", price: 2.19, quantity: 11 },
		},
	},
	{ returnNewDocument: true, arrayFilters: [{ markerField: "Big Market" }] }
);

// replace each item inside of the array with "Action"
db.movies.findOneAndUpdate(
	{ _id: 111 },
	{ $set: { "genre.$[]": "Action" } },
	{ returnNewDocument: true }
);

// replace a value in genres array
db.movies.findOneAndUpdate(
	{ _id: 111 },
	{ $set: { "genres.$[foreign]": "Latino" } },
	{
		returnNewDocument: true,
		arrayFilters: [{ foreign: "Foreign" }],
	}
);
