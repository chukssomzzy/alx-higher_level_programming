#!/usr/bin/node

const fs = require('fs')
const request = require('request')

try {
  request(process.argv[2], (err, res, body) => {
    if (err) { throw err }
    fs.writeFileSync(process.argv[3], body, 'utf-8')
  })
  process.exit(0)
} catch (e) {
  console.log(e)
  process.exit(1)
}
