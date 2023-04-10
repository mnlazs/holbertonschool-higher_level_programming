#!/usr/bin/node

// Creates a Square class that extends Rectangle class

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the Rectangle class with the size parameter twice (width and height)
    super(size, size);
  }

  double () {
    super.double();
  }
};
