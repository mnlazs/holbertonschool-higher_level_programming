#!/usr/bin/node
// Write a class Rectangle that
class Rectangle {
    constructor(w, h) {
      if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
        // Si w o h no son números enteros positivos, crea un objeto vacío.
        return {};
      } else {
        // Si w y h son números enteros positivos, inicializa los atributos de instancia.
        this.width = w;
        this.height = h;
      }
    }
  }
  