#!/usr/bin/node
// Prints all characters of a Star Wars movie

// Import the 'request' module
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Function to fetch data from the Star Wars API
// Make an HTTP GET request to the provided URL
function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

// Function to print all characters of a Star Wars movie
async function printCharacters (movieId) {
  try {
    const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    const movieData = await fetchData(apiUrl);
    const movie = JSON.parse(movieData);

    // Display one character name by line
    for (const characterUrl of movie.characters) {
      const characterData = await fetchData(characterUrl);
      const character = JSON.parse(characterData);
      console.log(character.name);
    }
  } catch (error) {
    console.error(`Error: ${error}`);
  }
}

// Call the function with the provided movie ID
printCharacters(movieId);
