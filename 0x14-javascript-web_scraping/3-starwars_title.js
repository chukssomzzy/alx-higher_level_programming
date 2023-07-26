#!/usr/bin/node

const request = require('request')

try {

const url = `https://swapi-api.alx-tools.com/api/films/${Number(process.argv[2])}`
request(url, (err, res, body) => {
  if (err) throw err

  const data = JSON.parse(body)
  console.log(data.title)
})
} catch (e) {
    console.loge(e)
}
