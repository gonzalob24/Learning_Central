const findMoviesByGenre = function (genre, pageNumber, pageSize) {
	const results = db.movies
		.find({ genres: genre })
		.sort({ "imdb.rating": -1 })
		.limit(pageSize)
		.skip(pageSize * pageNumber - pageSize);

	results.forEach((movie) => {
		console.log(movie.title);
	});
};

const findMoviesByGenre = (genre, pageNumber, pageSize) => {
	//
};
