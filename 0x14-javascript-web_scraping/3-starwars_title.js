#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer

// Import the 'request' module
const request = require('request');

// URL for the Star Wars film
const url = 'https://swapi-api.alx-tools.com/api/films/';

// Use the 'request' module to perform an HTTP GET request to the constructed URL.
// Log title if successful, log error if not.
request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
