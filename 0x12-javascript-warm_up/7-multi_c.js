#!/usr/bin/node

const printLove = (x) => {
  for (let i = 0; i < x; i++) { console.log('C is fun'); }
};
printLove(process.argv[2]);
