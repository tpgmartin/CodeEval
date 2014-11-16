var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
    var words = line.split(" ");
    var penultimate = words[words.length - 2];
    if (penultimate) {
      console.log(penultimate);
    } 
  }
});