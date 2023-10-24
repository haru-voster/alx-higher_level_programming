#!/usr/bin/node
//100-starwars_characters.js 
const request = require('request');

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = baseUrl.concat(movieId);
request(fullUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    // Create a variable to store the number of characters 
    // Create an empty array
    let charactersProcessed = 0;
    
    const characterNames = [];
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const charName = JSON.parse(body).name;
          // Add the character name to the array
          characterNames.push(charName);
        }
        // Increment the charactersProcessed variable
        charactersProcessed++;
        // Check if all characters have been processed
        if (charactersProcessed === characters.length) {
          characterNames.forEach((actor) => {
            console.log(actor);
          });
        }
      });
    });
  } else {
    console.log(error);
  }
});
