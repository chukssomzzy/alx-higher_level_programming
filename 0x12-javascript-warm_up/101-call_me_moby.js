#!/usr/bin/node

const callMeMoby = function (x, theFunction) {
  while (x--) { theFunction(); }
};

module.exports = {
  callMeMoby
};
