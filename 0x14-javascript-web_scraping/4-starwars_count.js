#!/usr/bin/node

const request = require('request');

try {
  request(process.argv[2], (err, res, body) => {
    if (err) throw err;

    const movies = JSON.parse(body);
    let count = 0;
    const characterId = '18';
    for (const movie of movies.results) {
      for (const character of movie.characters) {
        if (character.slice(-3, -1) === characterId) { count++; }
      }
    }
    console.log(count);
  });
} catch (e) {
  console.log(e);
}
