#!/usr/bin/node
// Computes the number of tasks completed by user id

// Import the 'request' module
const request = require('request');

// Make an HTTP GET request to the provided URL
// Check for error during the HTTP request
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);

    // Iterate through tasks
    // Check if the user ID is already in the completed object
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }

    // Print the completed tasks by user ID
    console.log(completed);
  } else {
    console.error('An error occurred. Status code: ' + response.statusCode);
  }
});
