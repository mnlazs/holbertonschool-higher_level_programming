#!/usr/bin/node

const arg = process.argv[2];

if (!Number.isInteger(parseInt(arg))) {
  console.log('Missing size');
} else {
  const n = parseInt(arg);
  let square = "";

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      square += 'X';
    }
    square += '\n';
  }

  console.log(square);
}
