#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

// Import the 'fs' module
const fs = require('fs');

// Import the 'request' module
const request = require('request');

// Use the 'request' module for HTTP GET request to the URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
