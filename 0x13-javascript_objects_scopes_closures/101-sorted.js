#!/usr/bin/node
// Import the dictionary from the file
const { occurrencesByUserId } = require('./101-data');

// Initialize an empty object to store results
let userIdsByOccurrences = {};

// Iterate through each user id and its occurrence count
for (let userId in occurrencesByUserId) {
    let occurrenceCount = occurrencesByUserId[userId];

    // If the occurrence count is not yet a key in the new dictionary, initialize it with an empty array
    if (!userIdsByOccurrences[occurrenceCount]) {
        userIdsByOccurrences[occurrenceCount] = [];
    }

    // Push the user id into the array corresponding to its occurrence count
    userIdsByOccurrences[occurrenceCount].push(userId);
}

// Print the new dictionary
console.log(userIdsByOccurrences);
