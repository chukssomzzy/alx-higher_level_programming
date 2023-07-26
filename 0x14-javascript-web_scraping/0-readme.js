#!/usr/bin/node
const fs = require('fs')

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err)
    process.exit(1)
  }

  console.log(data)
  process.exit(0)
})
