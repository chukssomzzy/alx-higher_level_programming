#!/usr/bin/node

const request = require('request');
try {
  const url = `https://swapi-api.alx-tools.com/api/films/${Number(process.argv[2])}`;
  request(url, (err, res, body) => {
    if (err) throw err;

    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;
    recursivePrint(characterUrls);
  });
} catch (e) {
  console.log(e);
}

const recursivePrint = async (characterUrls, index = 0) => {
  try {
    if (index === characterUrls.length) { return; }
    request(characterUrls[index], (err, resp, body) => {
      if (err) throw err;

      const characterName = JSON.parse(body).name;
      console.log(characterName);
      recursivePrint(characterUrls, index + 1);
    });
  } catch (e) {
    console.log(e);
  }
};
