#!/usr/bin/node
const fs = require('fs')

fs.readFile(process.argv[1], (err, data) => {
  if (err) {
    console.log(err)
    process.exit(1)
  }

  console.log(data)
  process.exit(0)
})
