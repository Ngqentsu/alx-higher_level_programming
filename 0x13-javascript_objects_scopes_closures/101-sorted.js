#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = Object.entries(dict).reduce((acc, [userId, occurrences]) => {
  acc[occurrences] = (acc[occurrences] || []).concat(userId);
  return acc;
}, {});

console.log(newDict);
