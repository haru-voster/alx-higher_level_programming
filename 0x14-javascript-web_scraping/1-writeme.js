#!/usr/bin/node

const r = require('r');

const fileName = process.argv[2];
const fileContent = process.argv[3];

r.writeFile(fileName, fileContent, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
