db.friends.aggregate([
    {
      $project: {
        _id: 0,
        scores: { $filter: { input: '$examScores', as: 'sc', cond: { $gt: ["$$sc.score", 60] } } }
      }
    }
  ]).pretty();

// filter: allows me to filter elements in an array
// $$sc.score --> refers to this variable not field name
// $ one sign referes to a field na,e
db.friends.aggregate([
    { $project: { _id: 0, scores: { $filter: { input: '$examScores', as: 'sc', cond: {$gt: ['$$sc.score', 60] } } } }}
])
