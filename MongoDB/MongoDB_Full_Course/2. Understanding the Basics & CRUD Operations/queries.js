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
