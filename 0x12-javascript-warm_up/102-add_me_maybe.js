#!/usr/bin/node

function addMeMaybe (num, theFunc) {
  return theFunc(++num);
}

module.exports = {
  addMeMaybe
};
