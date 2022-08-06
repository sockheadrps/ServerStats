// Open Websocket connection
var socket = new WebSocket("ws://localhost:8080/ws/stats");

// On open function
socket.onopen = function(event) {
    socket.send(JSON.stringify({event: "DATAREQUEST"}));
};


// Setting up HTML Elements
let cpu_count = document.getElementById("cpu_count")
let cpu_usage = document.getElementById("cpu_usage")
let cpu_frequency = document.getElementById("cpu_frequency")
let core_temperature = document.getElementById("core_temperature")
let ram_total = document.getElementById("ram_total")
let ram_availble = document.getElementById("ram_available")
let ram_percentage = document.getElementById("ram_percentage")
let disk_total = document.getElementById("disk_total")
let disk_free = document.getElementById("disk_free")
let disk_used = document.getElementById("disk_used")
let disk_percentage = document.getElementById("disk_percentage")


// Main Websocket Communication
socket.onmessage = function(event) {
    let data = JSON.parse(event.data);
    if (data.data){
        updateData(data.data)
    }
};

// Interval Timer to request Stats
setInterval(requestTimer, 1000);
function requestTimer() {
  socket.send(JSON.stringify({event: "DATAREQUEST"}));
}


// Chart configs
let updateInterval = 1000 //in ms
let numberElements = 120;

//Globals
let updateCount = 0;


// Chart Objects
let cpuUsageChart = document.getElementById("cpuUsage");
let ramUsageChart = document.getElementById("ramUsage");
let diskUsageChart = document.getElementById("diskUsage");


// Common Chart Options (Line)
let commonOptions = {
    responsive: true,
    maintainAspectRatio: false,
    backgroundColor: "rgba(33,31,51,0.5)",
    borderColor: "rgba(33,31,51,1)",
    fill: true,
    scales: {
      x: {
        color: "black",
        grid: {
            display: false
        },
        ticks: {
            color: "black"
        },
      },
      y: {
        beginAtZero: true,
        max: 100,
        grid: {
            color: "rgba(33,31,51,0.2)"
        },
        ticks: {
            color: "black"
        },
      }
    },
    legend: {display: false},
    tooltips:{
      enabled: false
    }
};


// cpuUsageChart Instance
var cpuUsageChartInstance = new Chart(cpuUsageChart, {
    type: 'line',
    data: {
      datasets: [{
          label: "CPU Usage",
          data: 0,
          borderWidth: 1
      }]
    },
    options: Object.assign({}, commonOptions, {
    responsive: true,
      title:{
        display: true,
        text: "CPU Usage",
        fontSize: 18
      }
    })
});

// ramUsageChart Instance
var ramUsageChartInstance = new Chart(ramUsageChart, {
    type: 'line',
    data: {
      datasets: [{
          label: "RAM Usage",
          data: 0,
          borderWidth: 1
      }]
    },
    options: Object.assign({}, commonOptions, {
      title:{
        display: true,
        text: "RAM Usage",
        fontSize: 18
      }
    })
});

// diskUsageChart Instance
var diskUsageChartInstance = new Chart(diskUsageChart, {
    type: 'doughnut',
    responsive: false,
    maintainAspectRatio: false,
    labels: [
        'free',
        'Used'
    ],
    data: {
      datasets: [{
          label: "Disk Usage",
          data: [1, 1],
          backgroundColor: [
            'rgba(189, 27, 15, .8)',
            'rgba(33, 31, 81, .9)',
          ],
          hoverOffset: 4
      }]
    },
    options: Object.assign({}, {
      title:{
        display: true,
        text: "Disk Usage",
        fontSize: 18
      }
    })
});
function shift(arr) {
  return arr.map((_, i, a) => a[(i + a.length - 1) % a.length]);
}
// Function to push data to chart object instances
function addData(data) {
    if(data){
        let today = new Date();
        let time
        if (today.getMinutes < 10){
            time = today.getHours() + ":0" + today.getMinutes();
        }else{
            time = today.getHours() + ":" + today.getMinutes();
        }
        // CPU Usage
        cpuUsageChartInstance.data.labels.push(time);
        cpuUsageChartInstance.data.datasets.forEach((dataset) =>{dataset.data.push(data.cpu_usage)});
        // RAM Usage
        ramUsageChartInstance.data.labels.push(time);
        ramUsageChartInstance.data.datasets.forEach((dataset) =>{dataset.data.push(data.ram_percentage)});
        // Disk Usage
        diskUsageChartInstance.data.datasets[0].data[0] = data.disk_used;
        diskUsageChartInstance.data.datasets[0].data[1] = data.disk_free;


      if(updateCount > numberElements){
        // For shifting the x axis markers
        // CPU Usage
        cpuUsageChartInstance.data.labels.shift();
        cpuUsageChartInstance.data.datasets[0].data.shift();
        // RAM Usage
        ramUsageChartInstance.data.labels.shift();
        ramUsageChartInstance.data.datasets[0].data.shift();
        location.reload();
      }
      else updateCount++;
      console.log(cpuUsageChartInstance.data.datasets[0].data)
      cpuUsageChartInstance.update();
      ramUsageChartInstance.update();
      diskUsageChartInstance.update();
      

    }
  };

  // Update HTML elements
function updateData(data) {
    addData(data)
    console.log(data)
    cpu_count.innerHTML = "Core count: " + data.cpu_count.toString()
    cpu_usage.innerHTML = "CPU usage: " + data.cpu_usage.toString() + "%"
    cpu_frequency.innerHTML = "CPU Frequency: " + data.cpu_frequency.current_frequency.toString() + " GHz"
    ram_total.innerHTML = "RAM total: " +  data.ram_total.toString() + " GB"
    ram_available.innerHTML = "RAM Available: " + data.ram_available.toString() + " GB"
    ram_percentage.innerHTML = "Percentage of RAM used: " + data.ram_percentage.toString() + "%"
    disk_total.innerHTML = "Disk space total: " + data.disk_total.toString() + " GB"
    disk_free.innerHTML = "Disk Space Free: " + data.disk_free.toString() + " GB"
    disk_used.innerHTML = "Disk Space used: " + data.disk_used.toString() + " GB"
    disk_percentage = "Disk Space Used: "+ data.disk_percentage.toString() + "%"


}
updateData()
