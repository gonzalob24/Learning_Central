db.friends.aggregate([
    { $unwind: "$hobbies" }, 
    { $group: { _id: { age: "$age" }, allHobbies: { $addToSet: "$hobbies" } } }
  ]).pretty();


// adding to set avoid duplicates
db.friends.aggregate([
    {$unwind: '$hobbies'},
    { $group: { _id: {age: '$age'}, allHobbies: { $addToSet: '$hobbies' } }}
])
