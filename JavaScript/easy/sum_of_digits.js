var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
    sum = 0
    line = line.split('').map(function(num) {
      sum += parseInt(num);
    });
    console.log(sum);
  }
});