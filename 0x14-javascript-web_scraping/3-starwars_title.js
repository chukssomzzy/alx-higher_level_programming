#!/usr/bin/node

const request = require('request')

const url = `https://swapi-api.alx-tools.com/api/films/${Number(process.argv[2])}`
request(url, (err, res, body) => {
  if (err) {
    console.log(err)
    process.exit(1)
  }
  const data = JSON.parse(body)
  console.log(data.title)
})
process.exit(0)
