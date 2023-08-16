#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const data = JSON.parse(body);
    const chars = data.characters;

    chars.forEach((charUrl) => {
      request(charUrl, (err, res, body) => {
        if (!err && res.statusCode === 200) {
          const charData = JSON.parse(body);
          console.log(charData.name);
        } else {
          console.err('An error occured: ', err);
        }
      });
    });
  } else {
    console.error('An error occured: ', err);
  }
});
