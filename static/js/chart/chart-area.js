// Obtener una referencia al elemento canvas del DOM
const $grafica = document.querySelector("#grafica");
// Las etiquetas son las que van en el eje X. 


const MONTHS = [
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
      value = MONTHS[Math.ceil(i) % 12];
      values.push(value.substring(0, section));
    }
  
    return values;
  }
  
// Podemos tener varios conjuntos de datos. Comencemos con uno
const zapatos = document.getElementById('grafica')


new Chart(zapatos, {
    type: 'line',// Tipo de gráfica
    data: {
        labels:  months({count: dt.getMonth()+1}),
        datasets: [
            {
                label: "Ventas",
                data: $('#data-area-total').html().slice(1,-1).split(','), // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
                backgroundColor: 'rgba(230, 57, 70, 0.1)', // Color de fondo
                borderColor: 'rgba(230, 57, 70)', // Color del borde
                borderWidth: 1.5,// Ancho del borde
                pointBackgroundColor: 'rgba(230, 57, 70, 0.3)',
                pointRadius: 5,
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
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }],
        },
    }
});