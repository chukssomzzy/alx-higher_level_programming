#!/usr/bin/node

const secondBiggest = () => {
  const argv = process.argv.slice(2).map(num => Number(num));

  if (!argv.length || argv.length === 1) console.log(0);
  else console.log((argv.sort())[1]);
};
secondBiggest();
