db.flightData.insertOne({ departureAirport: 'MUC', arrivalAirport: 'SFO', aircraft: 'Airbus A380', distance: 12000, intercontinental: true });

db.flightData.deleteOne({ departureAirport: 'TXL' });

db.flightData.updateOne({ distance: 12000 }, { $set: { marker: 'delete' } });

// updates all and inserts market element
db.flightData.updateMany({}, { $set: { marker: 'toDelete' } });

db.flightData.insertMany([
	{
		departureAirport: 'MUC',
		arrivalAirport: 'SFO',
		aircraft: 'Airbus A380',
		distance: 12000,
		intercontinental: true,
	},
	{
		departureAirport: 'LHR',
		arrivalAirport: 'TXL',
		aircraft: 'Airbus A320',
		distance: 950,
		intercontinental: false,
	},
	{
		departureAirport: 'SEA',
		arrivalAirport: 'TXL',
		aircraft: 'Airbus A442',
		distance: 10000,
		intercontinental: true,
	},
]);

db.flightData.find({ intercontinental: true });

db.flightData.find({ distance: { $gt: 10000 } });

db.flightData.updateOne({ _id: ObjectId('654e54b93d2bb176b9811ffd') }, { $set: { delayed: true } });

// embedded document
db.flight.updateMany({}, { $set: { status: { description: 'on-time', lastUpdated: '1 hour ago' } } });

// adding an array
db.passengers.updateOne({ name: 'Albert Twostone' }, { $set: { hobbies: ['sports', 'cooking'] } });
s;

// access / filer embedded documents
db.flightData.find({ 'status.description': 'on-time' });

// Patient example
db.patients.insertMany([
	{ firstName: 'Gonzalo', lastName: 'Bet', age: 38, history: [{ disease: 'Cold' }, { disease: 'Diarrhea' }] },
	{ firstName: 'Mary', lastName: 'Car', age: 38, history: [{ disease: 'Cold' }] },
	{ firstName: 'Alexa', lastName: 'Car', age: 17, history: [{ disease: 'Cold' }] },
]);

// find patients older than 30
db.patients.find({ age: { $gt: 30 } });
// update a patient
db.patients.updateOne({ firstName: 'Mary' }, { $set: { age: 35, lastName: 'Carrillo', history: [] } });

// find patients with disease of cold
db.patients.find({ history: { $elemMatch: { disease: 'Cold' } } });

// delete patient that have a cold, can use one of these queries
db.patients.deleteMany({ history: { $elemMatch: { disease: 'Cold' } } });
db.patients.deleteMany({ 'history.disease': 'Cold' });
