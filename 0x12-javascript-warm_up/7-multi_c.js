#!/usr/bin/node

const printLoveC = () => {
  const numC = process.argv[2];

  if (!numC) { console.log('Missing number of occurrences'); }
  for (let i = 0; i < numC; i++) { console.log('C is fun'); }
};

printLoveC();
