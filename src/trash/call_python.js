const { PythonShell } = require('python-shell');

PythonShell.run('./py/script.py', null, function(err, data) {
if (err) throw err;
console.log(data);
});