#!/usr/bin/node

function facto (numInput) {
  if (!numInput) { return (1); }
  return (numInput * facto(numInput - 1));
}
console.log(facto(Number(process.argv[2])));
