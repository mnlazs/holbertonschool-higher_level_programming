#!/usr/bin/node
// Write a class Rectangle that

class Rectangle {
    constructor(w, h) {
      if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
        return {}; // devuelve un objeto vacío si las dimensiones no son válidas
      }
      this.width = w;
      this.height = h;
    }
  
    print() {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += 'X';
      }
      for (let i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  
    rotate() {
      let temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  
    double() {
      this.width *= 2;
      this.height *= 2;
    }
  }
  