db.persons.aggregate([
    {
      $project: {
        _id: 0,
        gender: 1,
        fullName: {
          $concat: [
            { $toUpper: { $substrCP: ['$name.first', 0, 1] } },
            {
              $substrCP: [
                '$name.first',
                1,
                { $subtract: [{ $strLenCP: '$name.first' }, 1] }
              ]
            },
            ' ',
            { $toUpper: { $substrCP: ['$name.last', 0, 1] } },
            {
              $substrCP: [
                '$name.last',
                1,
                { $subtract: [{ $strLenCP: '$name.last' }, 1] }
              ]
            }
          ]
        }
      }
    }
  ]).pretty();


/*
Diving deeper project works similar to find
$ --> tells mongodb this is not hardcoded but refers to field of incoming document
 */
db.persons.aggregate([
  {$project: {_id: 0, gender: 1, fullName: {$concat: ['$name.first', ' ', '$name.last']}}},
  {$sort: {fullName: 1}}
])

// make uppercase letters
db.persons.aggregate([
  {$project: {_id: 0, gender: 1, fullName: {$concat: [{$toUpper: '$name.first'}, ' ', {$toUpper: 'name.last'}]}}},
  {$sort: {fullName: 1}}
])

// upercase first letters
db.persons.aggregate([
    {
      $project: {
        _id: 0,
        gender: 1,
        fullName: {
          $concat:[
              { $toUpper: { $substrCP: [ '$name.first', 0, 1] } },
              { $substrCP: ['$name.first', 1, { $subtract: [{ $strLenCP: '$name.first'}, 1]}]},
              ' ',
            { $toUpper: { $substrCP: [ '$name.last', 0, 1] } },
            { $substrCP: ['$name.last', 1, { $subtract: [{ $strLenCP: '$name.last'}, 1]}]}
          ]
        }
      }
    }
  ])
