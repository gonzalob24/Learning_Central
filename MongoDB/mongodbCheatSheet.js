///////////////////////////////////////////////////////////////////////
/**
 * QUERIES
 */
// CRUD
//CREATE
db.movies.insertOne(data, options);
db.movies.insertMany(data, options);

// READ:
// this one returns a cursor
// I can use projection here
db.movies.find(filter, options);
// returns first matching document
db.movies.findOne(filter, options);

// UPDATE: done use update as it replaces the entire document
// when update use {$set: {data}}
db.movies.updateOne(filter, data, options);
db.movies.updateMany(filter, data, options);
db.movies.replaceOne(filter, data, options);

// DELETE
db.movies.deleteOne(filter, options);
db.movies.deleteMany(filter, options);

// get different values for a field
db.movies.distinct("genres", { cast: "Leonardo DiCaprio" });
// all all documents
db.movies.count();

// AGGREGATE FRAMEWORK
// Joining collections
db.movies.aggregate([{ $lookup }]);

///////////////////////////////////////////////////////////////////////
/**
 * MAINTENANCE
 */

// view details about the current db
db.stats();

///////////////////////////////////////////////////////////////////////
/**
 * SCHEMA DESIGN
 *
 * 1-1: embedded documents
 *    use embedded documents for strong relations
 *
 * 1-1: references
 *    lets say we don't always need car data or person data
 *    i can use person data to do some analytics and car data for other things
 *    if there is an application need use references.
 *
 * 1-Many: embedded documents
 *    - embedding makes sense if embedded document is bound -> has a limit
 *
 * 1-Many: References
 *    - if document does not have bound use references.
 *    - having references limits the amount of data being transferred
 *    - recall the 16MB limit per document
 *
 * Many-Many: Embedded
 *    - I can embed a document and store the details of an item instead of reference id
 *    - this approach can lead to data duplication
 *    - may need to update in more than one place
 *    - Embed and Reference
 *        - I can embed a document and reference the items with an id
 *
 * Many-Many: Reference
 *    - a field in my document references anothe collection
 */

// add $jsonSchema object to declare type, required fields
// properties object defines an object for every field and declare how it looks like
db.createCollection("postswithvalidation", {
	validator: {
		$jsonSchema: {
			bsonType: "object",
			required: ["title", "text", "creator", "comments"],
			properties: {
				title: {
					bsonType: "string",
					description: "must be a string and is required",
				},
				text: {
					bsonType: "string",
					description: "must be a string and is required",
				},
				creator: {
					bsonType: "objectId",
					description: "must be an objectId and is required",
				},
				comments: {
					bsonType: "array",
					description: "must be an array and is required",
					items: {
						bsonType: "array",
						required: ["text", "author"],
						properties: {
							text: {
								bsonType: "string",
								description: "must be a string and is required",
							},
							author: {
								bsonType: "objectId",
								description: "must be an objectId and is required",
							},
						},
					},
				},
			},
		},
	},
});
