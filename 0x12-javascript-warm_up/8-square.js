#!/usr/bin/node

if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let row = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
