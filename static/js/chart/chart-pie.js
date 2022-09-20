
  var birdsCanvas = document.getElementById("birdsChart");

new Chart(birdsCanvas, {
    type: 'polarArea',
    data: {
      labels: ["Llaveros","Atrapasueños","Masetas","Manillas"],
      datasets: [{
        data: $('#data-area-VentasCategoria').html().slice(1,-1).split(','),
        backgroundColor: [
          "rgba(255, 111, 89, 0.2)",
          "rgba(107, 77, 87, 0.2)",
          "rgba(239, 48, 84, 0.2)",
          "rgba(59, 13, 17, 0.2)"
        ],
        borderColor: [
          'rgba(255, 111, 89, 1)',
          'rgba(107, 77, 87, 1)',
          'rgba(239, 48, 84, 1)',
          "rgba(59, 13, 17, 1)"
      ],
      borderWidth:1,
      }]
    }
  });
  