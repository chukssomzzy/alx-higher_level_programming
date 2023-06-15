#!/usr/bin/node

function callMeMoby (numTimes, func) {
  while (numTimes--) { func(); }
}

module.exports = {
  callMeMoby
};
