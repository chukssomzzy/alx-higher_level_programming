#!/usr/bin/node

const request = require('request');

try {
  request(process.argv[2], (err, res) => {
    if (err) throw err;

    console.log(`code: ${res && res.statusCode}`);
  });
} catch (e) {
  console.log(e);
}
