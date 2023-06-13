#!/usr/bin/node

const printSquare = (size) => {
  let charC = '';

  size = Number(size);
  if (size) {
    for (let i = 0; i < size; i++) {
      for (let j = 0; j < size; j++) { charC += '#'; }
      if (i < size - 1) { charC += '\n'; }
    }
  }
  return (charC);
};
console.log(printSquare(process.argv[2]));
