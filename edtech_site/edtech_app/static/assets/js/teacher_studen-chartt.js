$(function(){
var data1 = {
    labels: ["match1", "match2", "match3", "match4", "match5"],
    datasets: [
      {
        label: "TeamA Score",
        data: [10, 50, 25, 70, 40],
        backgroundColor: [
          "#DEB887",
          "#A9A9A9",
          "#DC143C",
          "#F4A460",
          "#2E8B57"
        ],
        borderColor: [
          "#CDA776",
          "#989898",
          "#CB252B",
          "#E39371",
          "#1D7A46"
        ],
        borderWidth: [1, 1, 1, 1, 1]
      }
    ]
  };
  

var ctst = document.getElementById("student_inscription");
var myLineChart2 = new Chart(ctst, {
  type: 'bar',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'inscrit',
                backgroundColor: 'rgb(0, 197, 106)',
                data: [1,10,5]
            }, {
                label: 'sortie',
                backgroundColor: 'rgb(255, 114, 107)',
                data: [1,15,20]
            }]
        },
        options: {
           
            tooltips: {
                mode: 'index',
                intersect: false
            },
            responsive: true,
           
        }

});


var ctnb = document.getElementById("student_number");
var chart1 = new Chart(ctnb, {
    type: "pie",
    data: data1,
    options:{
        responsive:true,
        legend: {
            display: true,
            position: "bottom",
            labels: {
              fontColor: "#333",
              fontSize: 10
            }
          }
    }
  
  });
});