#!/usr/bin/node

const fs = require('fs');

// Obtener el argumento de la ruta del archivo y la cadena a escribir
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Escribir la cadena en el archivo
fs.writeFile(filePath, stringToWrite, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`El archivo ${filePath} ha sido actualizado.`);
  }
});
