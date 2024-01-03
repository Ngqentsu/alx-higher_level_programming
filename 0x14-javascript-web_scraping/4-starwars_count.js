#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present

// Import the 'request' module
const request = require('request');

// Use the 'request' module for HTTP GET request to the URL.
// Check for error during the HTTP request.
// parse the JSON data and extract the "results" array
// Use the 'reduce()' method to iterate through the movies in the 'results' array.
// check if there is a character with ID 18 ('/18/') in the 'characters' array.
// If a character with ID 18 is present, increment by 1, otherwise keep unchanged.
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((i, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? i + 1
        : i;
    }, 0));
  }
});
