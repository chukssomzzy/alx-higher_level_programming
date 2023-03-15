#!/usr/bin/node

const {
  dict
} = require('./101-data');

const mapKeyToValue = () => {
  const newDict = {};
  Object.keys(dict).forEach((key) => {
    if (!newDict[dict[key]]) newDict[dict[key]] = [key];
    else newDict[dict[key]].push(key);
  });
  console.log(newDict);
};

mapKeyToValue();
