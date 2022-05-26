db.friends.aggregate([
    { $project: { _id: 0, examScore: { $slice: ["$examScores", 2, 1] } } }
  ]).pretty();


// slice [arrayIwantToSlice, 1], fist exam score
db.friends.aggregate([
    {$project: { _id: 0, examScore: {$slice: ['$examScores', 1] } } }
])

// slice the last 2
db.friends.aggregate([
    {$project: { _id: 0, examScore: {$slice: ['$examScores', -2] } } }
])

//slice one element starting at the second element
db.friends.aggregate([
    {$project: { _id: 0, examScore: {$slice: ['$examScores', 2, 1] } } }
])
