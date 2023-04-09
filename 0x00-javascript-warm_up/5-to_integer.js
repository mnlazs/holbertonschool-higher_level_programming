#!/usr/bin/node
// Prints messages depending...

const arg = process.argv[2];

if (Number.isInteger(Number(arg))) {
  console.log(`My number: ${parseInt(arg, 10)}`);
} else {
  console.log("Not a number");
}


