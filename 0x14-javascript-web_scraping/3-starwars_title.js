#!/usr/bin/node

const request = require("request")

url = `https://swapi-api.alx-tools.com/api/films/${Number(process.argv[2])}`
request(url, (err, res, body) => {
    data = JSON.parse(body)
    console.log(data.title)
})
