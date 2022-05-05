/**_
 * pg: 244
 * pipeline:
 * stage 1: $set
 * stage 2: $set
 * stage 3: $project
 */
db.users.updateMany({}, [
	{ $set: { name_array: { $split: ["$name", " "] } } },
	{
		$set: {
			first_name: { $arrayElemAt: ["$name_array", 0] },
			last_name: { $arrayElemAt: ["$name_array", 1] },
		},
	},
	{
		$project: {
			first_name: 1,
			last_name: 1,
			name: { $concat: [{ $toUpper: "$first_name" }, " ", "$last_name"] },
		},
	},
]);

db.items.insert({
	_id: 11,
	items: [
		{ name: "backpack", price: 127.59, quantity: 3 },
		{ name: "notepad", price: 17.6, quantity: 4 },
		{ name: "binder", price: 18.17, quantity: 2 },
		{ name: "pens", price: 60.56, quantity: 3 },
	],
});

// replace all items in the array one by one with Action
db.movies.findOneAndUpdate(
	{ _id: 111 },
	{ $set: { "genres.$[]": "Action" } },
	{ returnNewDocument: true }
);

// arrayFilters is the query condition and will update the document
// that meets the criteria
db.items.findOneAndUpdate(
	{ _id: 11 },
	{
		$set: {
			"items.$[myElements]": { quantity: 7, price: 4.5, name: "Marker" },
		},
	},
	{ returnNewDocument: true, arrayFilters: [{ "myElements.quantity": null }] }
);
