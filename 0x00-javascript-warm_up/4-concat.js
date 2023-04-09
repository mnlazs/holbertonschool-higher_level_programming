#!/usr/bin/node
// Prints messages depending..
const args = process.argv.slice(2);

if (args.length >= 2) {
  console.log(`${args[0]} is ${args[1]}`);
}
