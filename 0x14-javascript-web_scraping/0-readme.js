#!/usr/bin/node
// reads and prints the content of a file.

// Import the 'fs' module
const fs = require('fs');

// Use fs.readFile() to read the contents of the file specified as argument
// 'utf8' specifies the encoding of the file being read
// Check if an error occurred during reading
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
