#!/usr/bin/node

const esrever = function (list) {
  const listRev = [];

  for (let i = list.length - 1; i >= 0; i--) listRev[list.length - (i + 1)] = list[i];
  return (listRev);
};

module.exports = {
  esrever
};
