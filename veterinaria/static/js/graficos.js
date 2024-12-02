// graficos.js

const initChart = () => {
    const myChart = echarts.init(document.getElementById("chart"));

    // Obtener la serie desde la variable definida en el HTML
    const serie = seriesData; // Usa la variable directamente

    const option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                data: ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
                        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
                axisTick: {
                    alignWithLabel: true
                },
                axisLabel: {
                    rotate: 45,  // Rota las etiquetas 45 grados
                },
                boundaryGap: true  // Asegura que haya espacio entre las barras y el eje
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: 'Total Compras',
                type: 'bar',
                barWidth: '60%',
                data: serie, // Ahora usamos la serie correctamente
                itemStyle: {
                    color: 'lightblue'
                }
            }
        ]
    };

    myChart.setOption(option);
    myChart.resize();
};

const initPieChart = () => {
    const myChart = echarts.init(document.getElementById("donut-chart"));

    const option = {
        title: {
            text: 'Total de Compras por Mes',
            subtext: 'Distribución de Compras',
            left: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            left: 'left'
        },
        series: [
            {
                name: 'Mes',
                type: 'pie',
                radius: '50%',
                data: pieData,  // Usa los datos del gráfico de pastel
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };

    myChart.setOption(option);
    myChart.resize();
};


window.addEventListener("load", () => {
    initChart(); // Llama a la función de barras
    initPieChart(); // Llama a la función de pastel
});
