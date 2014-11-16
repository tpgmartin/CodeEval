var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
    var nums = line.split(','), n = parseInt(nums[0]), m = parseInt(nums[1]);
    while (n > m) {
      n -= m;
    }
    console.log(n);
  }
});