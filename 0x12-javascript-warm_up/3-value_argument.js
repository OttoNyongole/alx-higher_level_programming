#!/usr/bin/node

//script to print the value of the argument passes to it

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
