#!/usr/bin/node
// Script that prints massage depending of the number of arguments passed
const count = process.argv.length -2; // this is because 1 and 2 are node and file path to be excuted respectively
if (count === 0) {
  console.log('No argument');
} else if (count === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
