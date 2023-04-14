#!/usr/bin/node
let argsCount = 0;

exports.logMe = function (item) {
  console.log(`${argsCount}: ${item}`);
  argsCount++;
};
