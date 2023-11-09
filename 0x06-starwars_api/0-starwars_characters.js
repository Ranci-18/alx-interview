#!/usr/bin/node
// a script that returns all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`, function (error, response, body) {
  if (response.statusCode === 200) {
    const parsedData = JSON.parse(body);
    const characterAPIList = parsedData.characters;
    /* for (const characterAPI of characterAPIList) {
      request(characterAPI, function (err, res, body) {
        if (res.statusCode === 200) {
          const characterParsedData = JSON.parse(body);
          console.log(characterParsedData.name); */
    printNames(characterAPIList, 0);
  } else {
    console.log(error);
  }
});

const printNames = (characterAPIList, index) => {
  if (index === characterAPIList.length) {
    return;
  }

  request(characterAPIList[index], function (err, res, body) {
    if (res.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printNames(characterAPIList, index + 1);
    } else {
      console.log(err);
    }
  });
};
