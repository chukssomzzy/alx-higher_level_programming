#!/usr/bin/node

const request = require('request')

request(process.argv[2], (err, res) => {
  if (err) {
    console.log(err)
    process.exit(1)
  }
  console.log(`code: ${res && res.statusCode}`)
})
process.exit(0)
