db.friends.aggregate([
    { $project: { _id: 0, numScores: { $size: "$examScores" } } }
  ]).pretty();


// length of the array
db.friends.aggregate([
    {$project: { _id: 0, numScores: {$size: '$examScores' } } }
])

