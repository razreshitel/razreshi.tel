const ctx = document.getElementById('uptimeChart').getContext('2d');

// Инициализация графика
const uptimeChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [], // Метки времени
        datasets: [
            {
                label: 'Local Server Uptime',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                data: [],
                fill: false,
            },
            {
                label: 'Remote Machine Uptime',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                data: [],
                fill: false,
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'minute'
                },
                title: {
                    display: true,
                    text: 'Time'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Uptime (minutes)'
                }
            }
        }
    }
});

// Функция для обновления данных uptime
async function fetchUptimeData() {
    try {
        const response = await fetch('uptime.php');
        const data = await response.json();

        const timestamp = new Date();
        const localUptime = parseUptime(data.local);
        const remoteUptime = parseUptime(data.remote);

        uptimeChart.data.labels.push(timestamp);
        uptimeChart.data.datasets[0].data.push(localUptime);
        uptimeChart.data.datasets[1].data.push(remoteUptime);

        // Ограничиваем количество точек на графике
        if (uptimeChart.data.labels.length > 20) {
            uptimeChart.data.labels.shift();
            uptimeChart.data.datasets[0].data.shift();
            uptimeChart.data.datasets[1].data.shift();
        }

        uptimeChart.update();
    } catch (error) {
        console.error("Ошибка при получении данных uptime:", error);
    }
}

// Функция для преобразования uptime в минуты
function parseUptime(uptimeString) {
    const timeParts = uptimeString.match(/\d+/g);
    let totalMinutes = 0;

    if (timeParts) {
        if (uptimeString.includes('day')) totalMinutes += parseInt(timeParts[0]) * 1440;
        if (uptimeString.includes('hour')) totalMinutes += parseInt(timeParts[1]) * 60;
        if (uptimeString.includes('minute')) totalMinutes += parseInt(timeParts[2]);
    }
    return totalMinutes;
}

// Запуск периодического обновления данных
setInterval(fetchUptimeData, 60000); // Обновление каждую минуту
fetchUptimeData();

document.getElementById('refreshUptimeButton').addEventListener('click', fetchUptimeData);