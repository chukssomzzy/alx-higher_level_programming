#!/usr/bin/node

const add = (a, b) => {
  if (!b || !a) { return (NaN); }
  return (a + b);
};
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
