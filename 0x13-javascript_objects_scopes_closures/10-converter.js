#!/usr/bin/node

let baseG = 10;
const converter = function (base) {
  baseG = base;
  return (conv);
};

const conv = (base) => base.toString(baseG);

module.exports = {
  converter
};
