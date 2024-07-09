#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movie = process.argv[2];

  const URL = `https://swapi-api.alx-tools.com/api/films/${movie}/`;

  request(URL, (_, __, body) => {
    const charsApis = JSON.parse(body).characters;
    const charNames = charsApis.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, _, body) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(body).name);
        });
      })
    );
    Promise.all(charNames)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  });
}
