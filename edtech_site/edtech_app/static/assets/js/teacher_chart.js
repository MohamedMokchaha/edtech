var ctt = document.getElementById("working_activity");
var myLineChart_tech = new Chart(ctt, {
  type: 'line',
  data: {
    labels: ["lundi", "mardi", "Mercredi", "jeudi", "vendredi", "samedi", "damanche"],
    datasets: [{
      label: "Earnings",
      lineTension: 0.3,
      backgroundColor: "#2ed8b6",
      borderColor: "#2ed8b6",
      pointRadius: 3,
      pointBackgroundColor: "rgba(0,128,0,1)",
      pointBorderColor: "rgba(0,120,0, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [0, 10000, 5000, 15000, 10000, 2000,90000],
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 5,
        top: 5,
        bottom: 15
      }
    },
    
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + ': $' + number_format(tooltipItem.yLabel);
        }
      }
    }
  }
});

