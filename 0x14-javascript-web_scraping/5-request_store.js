#!/usr/bin/node
const r = require('r');
const request = require('request');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = body;

  r.writeFile(fileName, data, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
