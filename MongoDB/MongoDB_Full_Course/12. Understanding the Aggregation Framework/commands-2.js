db.persons.aggregate([
    { $match: { gender: 'female' } },
    { $group: { _id: { state: "$location.state" }, totalPersons: { $sum: 1 } } },
    { $sort: { totalPersons: -1 } }
]).pretty();


/* $group: accumulated data
_id: field that I want to group by
$ --> refers to the field of the document

$sum: add 1 for each grouped document.
 */
db.persons.aggregate([
    {$match: {gender: 'female'}},
    {$group: {_id: {state: '$location.state'}, totalPersons: {$sum: 1}}},
    {$sort: {totalPersons: -1}}
])
