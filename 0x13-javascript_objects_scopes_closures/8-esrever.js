#!/usr/bin/node

exports.esrever = function (list) {
  let Rlist = [];
  let len = list.length - 1;
  for (let i = len; i >= 0; i--) {
    Rlist.push(list[i]);
  }
  return Rlist;
};
