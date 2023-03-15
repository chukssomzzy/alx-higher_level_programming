#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);
const filesR = argv.slice(0, 2);
const fileD = argv[2];

const concatFile = () => {
  for (let i = 0; i < filesR.length; i++) {
    fs.readFile(filesR[i], 'utf8', (err, buffer) => {
      if (err) throw err;
      fs.appendFile(fileD, buffer, 'utf8', (err) => {
        if (err) throw err;
      });
    });
  }
};
concatFile();
