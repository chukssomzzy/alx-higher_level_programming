#!/usr/bin/node

const logMe = function (item) {
  if (!this.i) this.i = 0;
  console.log(`${this.i++}: ${item}`);
};

module.exports = {
  logMe
};
