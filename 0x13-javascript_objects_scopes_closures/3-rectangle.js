#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const char = 'X';
    for (let i = 0; i < this.height; i++) {
      let charFmt = '';
      for (let j = 0; j < this.width; j++) charFmt += char;
      console.log(charFmt);
    }
  }
}

module.exports = Rectangle;
