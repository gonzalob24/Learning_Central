db.friends.aggregate([
    { $unwind: "$examScores" },
    { $project: { _id: 1, name: 1, age: 1, score: "$examScores.score" } },
    { $sort: { score: -1 } },
    { $group: { _id: "$_id", name: { $first: "$name" }, maxScore: { $max: "$score" } } },
    { $sort: { maxScore: -1 } }
  ]).pretty();


// outpyt the highest exam for every person
// unwind flattens out the array and gives many documents with exam score as a top level document not an array
db.friends.aggregate([
    {$unwind: '$examScores'},
])

// sort lowest to highest
// sort by examScores.score
db.friends.aggregate([
    {$unwind: '$examScores'},
    {$sort: {'examScores.score': -1}} // no $ needed since I refer to the field I don't want to get the value
])

// I can also add a projection state and then sort
db.friends.aggregate([
    {$unwind: '$examScores'},
    {$project: { _id: 0, name: 1, age: 1, score: '$examScores.score'}},
    {$sort: {score: -1}},
])

// I can group to reverse the unwind
db.friends.aggregate([
    {$unwind: '$examScores'},
    {$project: { _id: 1, name: 1, age: 1, score: '$examScores.score'}},
    {$sort: {score: -1}},
    {$group: {_id: '$_id', name: {$first: '$name'}, maxScore: {$max: '$score'}}} //use $ since I want the max value of this field
])

// I can sort again
db.friends.aggregate([
    {$unwind: '$examScores'},
    {$project: { _id: 1, name: 1, age: 1, score: '$examScores.score'}},
    {$sort: {score: -1}},
    {$group: {_id: '$_id', name: {$first: '$name'}, maxScore: {$max: '$score'}}},
    {$sort: {maxScore: -1}}
])
