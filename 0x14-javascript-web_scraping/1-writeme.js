#!/usr/bin/node
// writes a string to a file

// Import the 'fs' module
const fs = require('fs');

// Use fs.writeFile() to write data to the file specified at process.argv[2].
// The data to be written is 4th cmd line argument process.argv[3].
// 'utf8' specifies the encoding of the file being read
// Check if an error occurred during reading
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
