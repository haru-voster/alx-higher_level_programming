#!/usr/bin/node
# 11 biggest
const listArg = process.argv.slice(2);
if (listArg.length === 0 || listArg.length === 1) {
  console.log(0);
} else {
  listArg.sort((a, b) => a - b);
  console.log(listArg[listArg.length - 2]);
}
