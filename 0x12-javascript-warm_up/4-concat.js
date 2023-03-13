#!/usr/bin/node

const printConcatArg = () => {
  const argv = process.argv;
  const newSec = [];
  newSec[0] = argv[2] ? argv[2] : 'undefined';
  newSec[1] = 'is';
  newSec[2] = argv[3] ? argv[3] : 'undefined';
  console.log(newSec.join(' '));
};

printConcatArg();
