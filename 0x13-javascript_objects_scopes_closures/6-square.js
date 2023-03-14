#!/usr/bin/node

const SquareIn = require('./5-square');

class Square extends SquareIn {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = 'X';
    if (c) char = c;
    for (let i = 0; i < this.height; i++) {
      let charFmt = '';
      for (let j = 0; j < this.width; j++) charFmt += char;
      console.log(charFmt);
    }
  }
}
module.exports = Square;
