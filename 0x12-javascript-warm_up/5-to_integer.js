#!/usr/bin/node
//script to convert an argv to number

const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
