#!/usr/bin/node

const request = require('request');
try {
  const url = `https://swapi-api.alx-tools.com/api/films/${Number(process.argv[2])}/`;
  request(url, (err, res, body) => {
    if (err) throw err;

    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;
    for (let i = 0; i < characterUrls.length; i++) {
      request(characterUrls[i], (err, res, body) => {
        if (err) throw err;

        const data = JSON.parse(body);
        console.log(data.name);
      });
    }
  });
} catch (e) {
  console.log(e);
}
