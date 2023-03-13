#!/usr/bin/node

const secondBiggest = () => {
  const argv = process.argv.slice(2).map(num => Number(num)).filter(num => num);

  if (!argv.length || argv.length === 1) console.log(0);
  else if (argv.length === 2) console.log(argv[0] > argv[1] ? argv[1] : argv[0]);
  else console.log((argv.sort())[argv.length - 2]);
};
secondBiggest();
