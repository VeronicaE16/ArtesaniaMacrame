// Obtener una referencia al elemento canvas del DOM
const $graficas = document.querySelector("#graficas");
// Las etiquetas son las que van en el eje X. 


const etiquetas = [
  'Enero',
  'Febrero',
  'Marzo',
  'Abril',
  'Mayo',
  'Junio',
  'Julio',
  'Agosto',
  'Septiembre',
  'Octubre',
  'Noviembre',
  'Diciembre'
];
var dt = new Date();
function months(config) {
  var cfg = config || {};
  var count = cfg.count || 12;
  var section = cfg.section;
  var values = [];
  var i, value;

  for (i = 0; i < count; ++i) {
    value = etiquetas[Math.ceil(i) % 12];
    values.push(value.substring(0, section));
  }

  return values;
}

// Podemos tener varios conjuntos de datos. Comencemos con uno

const mesess = document.getElementById('graficas')

let delayed;
new Chart(mesess, {
  type: 'bar',// Tipo de gráfica
  data: {
      labels: months({count: dt.getMonth()+1}),
      datasets: [
        {
          label: "Llaveros",
          data: $('#data-area-Llaveros').html().slice(1,-1).split(','),
          backgroundColor: 'rgba(255, 111, 89, 0.4)',
          borderColor: 'rgba(255, 111, 89, 1)',
          borderWidth:1.5,
        },
        {
          label: "Atrapasueños",
          data: $('#data-area-Atrapasueños').html().slice(1,-1).split(','),
          backgroundColor: 'rgba(107, 77, 87, 0.4)',
          borderColor: 'rgba(107, 77, 87, 1)',
          borderWidth:1.5,
        },
        {
          label: "Masetas",
          data: $('#data-area-Masetas').html().slice(1,-1).split(','),
          backgroundColor: 'rgba(239, 48, 84, 0.4)',
          borderColor: 'rgba(239, 48, 84, 1)',
          borderWidth:1.5,
        },
        {
          label: "Manillas",
          data:$('#data-area-Manillas').html().slice(1,-1).split(','), // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
          backgroundColor: 'rgba(59, 13, 17, 0.4)', // Color de fondo
          borderColor: 'rgba(59, 13, 17, 1)', // Color del borde
          borderWidth: 1.5,// Ancho del borde
        },
          // Aquí más datos...
      ]
  },
  
    options: { 
      plugins: {
          title: {
            display: true,
            text: 'Ventas por categoría al mes'
          },
      },
      responsive: true,
      scales: {
        // xAxes: [{
        //   stacked: true
        // }],
          yAxes: [{
            // stacked: true,
            ticks: {
              beginAtZero: true
            }
        }],
      },
  }
});

