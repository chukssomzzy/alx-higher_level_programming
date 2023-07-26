#!/usr/bin/node

const request = require('request')

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err)
  }
  const tasks = JSON.parse(body)
  const completedTask = {}
  for (const task of tasks) {
    if (task.completed) {
      if (completedTask[task.userId]) {
        completedTask[task.userId]++
      } else {
        completedTask[task.userId] = 1
      }
    }
  }
  console.log(completedTask)
})
