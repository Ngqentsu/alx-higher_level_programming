$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const movieList = $('UL#list_movies');

  data.results.forEach(function (movie) {
    $('<li>').text(movie.title).appendTo(movieList);
  });
});
