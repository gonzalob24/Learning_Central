db.friends.aggregate([
    { $unwind: "$hobbies" }, 
    { $group: { _id: { age: "$age" }, allHobbies: { $push: "$hobbies" } } }
  ]).pretty();

// group by age and add hobbies array to allHobies array
db.friends.aggregate([
    {$group: { _id: { age: '$age'}, allHobbies: { $push: '$hobbies'}}}
])


// unwind allows me to pull data, this flattens the array
// spits out multiple documents
// this will have duplicate values to use an alternative to push addToSet
db.friends.aggregate([
    {$unwind: '$hobbies'},
    {$group: { _id: { age: '$age'}, allHobbies: { $push: '$hobbies'}}}
])
