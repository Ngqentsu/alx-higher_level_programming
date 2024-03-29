#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      return;
    }

    for (let i = 0; i < this.height; i++) {
      let string = '';
      for (let j = 0; j < this.width; j++) {
        string += 'X';
      }
      console.log(string);
    }
  }
}

module.exports = Rectangle;
