db.persons.aggregate([
    { $match: { gender: 'female' } },
    { $group: { _id: { state: "$location.state" }, totalPersons: { $sum: 1 } } }
]).pretty();

// my examples
/*
match: is just a filtering phase. This is like using find
group:
 */
db.persons.aggregate([
    {$match: {gender: 'female'}}
])
