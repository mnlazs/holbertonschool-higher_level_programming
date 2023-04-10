#!/usr/bin/node
// Write a class Rectangle that
module.exports = class Rectangle {
    constructor (width, height) {
      if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
        this.width = width;
        this.height = height;
      }
    }
    print() {
        if (!this.width || !this.height) {
          console.log('Empty rectangle');
        } else {
          let row = '';
          for (let i = 0; i < this.width; i++) {
            row += 'X';
          }
          for (let i = 0; i < this.height; i++) {
            console.log(row);
          }
        }
      }
  }
