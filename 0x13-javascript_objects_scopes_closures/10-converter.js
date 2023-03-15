#!/usr/bin/node

function converter (base) {
  this.base = base;
  return (converter.convert);
}

converter.convert = function (base) {
  return (base.toString(this.base));
};

module.exports = {
  converter
};
