#!/usr/bin/node
// Display the status code of a GET request

// Import the 'request' module
const request = require('request');

// Use the 'request' module for an HTTP GET request to the URL
request.get(process.argv[2])

// Set up an event listener for the 'response' event emitted by the HTTP request.
// Log the HTTP status code of the response to the console.
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
