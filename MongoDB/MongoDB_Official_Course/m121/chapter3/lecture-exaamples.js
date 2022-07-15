db.icecream_data.aggregate([{
    $project: {
        _id: 0,
        max_high: {
            $reduce: {
                input: "$trends",
                initialValue: -Infinity,
                in: {
                    $cond: [
                        {$gt: ["$$this.avg_high_tmp", "$$value"]},
                        "$$this.avg_high_tmp",
                        "$$value"
                    ]
                }
            }
        }
    }
}])

// another way to achieve the same results
db.icecream_data.aggregate([{
    $project: {
        _id: 0,
        max_high: { $max: "$trends.avg_high_tmp"}
    }
}])

db.icecream_data.aggregate([{
    $project: {
        _id: 0,
        max_low: { $min: "$trends.avg_low_tmp"}
    }
}]);

db.icecream_data.aggregate([{
    $project: {
        _id: 0,
        avg_cpi: {$avg: "$trends.icecream_cpi"},
        cpi_deviation: {$stdDevPop: "$trends.icecream_cpi"}
    }
}]);

db.icecream_data.aggregate([{
    $project: {
        _id: 0,
        "Yearly sales (millions)": {$sum: "$trends.icecream_sales_in_millions"}
    }
}])

// how many films have awards
db.movies.aggregate([
    {
        $match: {
            awards: { $exists: true}
        }
    },
    {
        $count: "awards"
    }
])