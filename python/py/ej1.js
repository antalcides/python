var x = [];
for (var i = 0; i < 500; i ++) {
	x[i] = Math.random();
}

var data = [
  {
    x: x,
    type: 'histogram'
  }
];
Plotly.newPlot('myDiv', data);
