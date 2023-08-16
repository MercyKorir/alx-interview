#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/';

function printName (charUrl) {
  request.get(charUrl, (err, res, body) => {
    if (!err && res.statusCode === 200) {
      const data = JSON.parse(body);
      console.log(data.name);
    } else {
      console.error('An error occured: ', err);
    }
  });
}

function printMovie (movieId) {
  const movieUrl = `${url}films/${movieId}/`;
  request.get(movieUrl, (err, res, body) => {
    if (!err && res.statusCode === 200) {
      const data = JSON.parse(body);
      const charList = data.characters;
      for (const char of charList) {
        printName(char);
      }
    } else {
      console.error('An error occured: ', err);
    }
  });
}

printMovie(movieId);
