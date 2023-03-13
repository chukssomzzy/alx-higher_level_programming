#!/usr/bin/node

const printIfNum = () => {
  const argv = process.argv;
  if (!Number(argv[2])) { console.log('Not a number'); } else { console.log(`My number: ${Math.floor(Number(argv[2]))}`); }
};
printIfNum();
