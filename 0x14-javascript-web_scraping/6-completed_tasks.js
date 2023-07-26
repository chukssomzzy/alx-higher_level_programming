#!/usr/bin/node

const request = require('request');
try {
  request(process.argv[2], (err, res, body) => {
    if (err) throw err;

    const tasks = JSON.parse(body);
    const completedTask = {};
    for (const task of tasks) {
      if (task.completed) {
        if (completedTask[task.userId]) {
          completedTask[task.userId]++;
        } else {
          completedTask[task.userId] = 1;
        }
      }
    }
    console.log(completedTask);
  });
} catch (e) {
  console.log(e);
}
