#!/usr/bin/node

const list = process.argv.splice(2);

const secondLargest = (list) => {
  if (!list.length || list.length === 1) { return (0); }
  const sortedList = list.sort((a, b) => (b - a));
  return (sortedList[1]);
};

console.log(secondLargest(list));
