#!/usr/bin/node

const nbOccurences = (list, searchElement) => {
  let n = 0;
  let i;
  while ((i = list.indexOf(searchElement) + 1) && ++n) list = list.slice(i);
  return (n);
};

module.exports = {
  nbOccurences
};
