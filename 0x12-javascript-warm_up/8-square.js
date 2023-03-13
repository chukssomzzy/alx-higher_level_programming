#!/usr/bin/node

const printSqr = () => {
  const size = Number(process.argv[2]);

  if (!size) console.log('Missing size');
  for (let i = 0; i < size; i++) {
    let strFmt = '';
    for (let j = 0; j < size; j++) strFmt += 'X';
    console.log(strFmt);
  }
};

printSqr();
