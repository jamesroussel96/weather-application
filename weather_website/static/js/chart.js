/* start of email functionality 

function sendMail(params) {
  var tempParams = {
      city: document.getElementById('Lancaster')
    }
    emailjs.send('service_v5cxn0t','template_dnkkaee',tempParams)
    .then(function(res){
    })
  } 
*/


var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Celsius'],
    datasets: [{
      label: 'Lancaster',
      data: [celsius_temp_lancaster],
      backgroundColor: "rgba(94, 103, 218, 0.8)"
    }, {
      label: 'Toronto',
      data: [celsius_temp_toronto],
      backgroundColor: "rgba(218, 94, 94, 0.8)"
    }]
  },
  options:{
    responsive: false,
    maintainAspectRatio: true,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }]
    }
  }
});