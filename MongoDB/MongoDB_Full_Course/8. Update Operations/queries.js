// this will replace the hobbies array
db.users.updateOne({ _id: ObjectId('655b72e89c0aaf019f804e42') }, { $set: { hobbies: [{ title: 'Gaming', frequency: 4 }] } });

db.users.updateMany({ 'hobbies.title': 'Sports' }, { $set: { isSporty: true } });

//
db.users.updateOne({ name: 'Max' }, { $inc: { age: 1 } });

// remove a field
db.users.updateOne({ _id: ObjectId('655b72e89c0aaf019f804e42') }, { $unset: { isSporty: '' } });

// set
db.users.updateOne({ _id: ObjectId('655b72e89c0aaf019f804e42') }, { $set: { isSporty: true } });

//rename
db.users.updateOne({ _id: ObjectId('655b72e89c0aaf019f804e42') }, { $rename: { isSporty: 'sporty' } });

// upsert: without upset nothing will be added
db.users.updateOne(
	{ name: 'Alison' },
	{
		$set: {
			age: 5,
			hobbies: [
				{ title: 'Sporty', frequency: 5 },
				{ title: 'Eating', frequency: 2 },
			],
			isSporty: true,
		},
	},
	{ upsert: true }
);

// update all with hobbies = Sports and Frequency >= 3
// this query does not work it will get documents with sports and documents with frequency gte 3
db.users.find({ $and: [{ 'hobbies.title': 'Sports' }, { 'hobbies.frequency': { $gte: 3 } }] });
// use
db.users.find({ hobbies: { $elemMatch: { title: 'Sports', frequency: { $gte: 3 } } } });
// update exactly the document in array that I found, hobbies.$' will match the element(s) I found inside hobbies
// this will replace the frequency for all items in hobbies array
db.users.updateMany({ hobbies: { $elemMatch: { title: 'Sports', frequency: { $gte: 3 } } } }, { $set: { 'hobbies.$': { title: 'Sports', frequency: 5 } } });
// this will add a new field in the document I found
db.users.updateMany({ hobbies: { $elemMatch: { title: 'Sports', frequency: { $gte: 3 } } } }, { $set: { 'hobbies.$.highFrequency': true } });

// update all elements who have a frequency higher than 2
// this only updates the first matching document
db.users.updateMany({ 'hobbies.frequency': { $gt: 2 } }, { $set: { 'hobbies.$.goodFrequency': true } });

// to update all of the matching documents. add a new field to every document inside of hobbies
// this will not work, hobbies is an array
db.users.updateMany({ age: { $gt: 30 } }, { $inc: { 'hobbies.frequency': -1 } });
// I need to select all elements in the array
db.users.updateMany({ age: { $gt: 30 } }, { $inc: { 'hobbies.$[].frequency': -1 } });

// all hobbies have frequency > 3 and change the elements
db.users.find({ 'hobbies.frequency': { $gt: 2 } });

// I can add an identifier here
db.users.updateMany({ 'hobbies.frequency': { $gt: 2 } }, { $set: { 'hobbies.$[el].goodFrequency': true } }, { arrayFilters: [{ 'el.frequency': { $gt: 2 } }] });

// add elements to an array
db.users.updateOne({ name: 'Matt' }, { $push: { hobbies: { title: 'Gaming', frequency: 10 } } });

db.users.updateOne(
	{ name: 'Matt' },
	{
		$push: {
			hobbies: {
				$each: [
					{ title: 'Sleep', frequency: 8 },
					{ title: 'Running', frequency: 3 },
				],
				$sort: { frequency: -1 },
			},
		},
	}
);
