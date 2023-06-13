#!/usr/bin/node

const argv_v = process.argv;

if (argv_v) { console.log('Argument found'); } else if (argv_v.length > 3) { console.log('Arguments found'); } else { console.log('No argument'); }
