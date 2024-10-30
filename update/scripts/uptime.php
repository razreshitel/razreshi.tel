<?php
function getUptime() {
    // Получаем uptime локального сервера
    $uptimeLocal = shell_exec("uptime -p");
    $uptimeRemote = null;

    // Получаем uptime удаленной машины по IP 192.168.0.2
    $pingResult = shell_exec("ping -c 1 192.168.0.2");

    if (strpos($pingResult, '1 received') !== false) {
        $uptimeRemote = shell_exec("ssh user@192.168.0.2 'uptime -p'");
    } else {
        $uptimeRemote = "Машина не доступна";
    }

    return [
        'local' => trim($uptimeLocal),
        'remote' => trim($uptimeRemote),
    ];
}

// Возвращаем данные в формате JSON
header('Content-Type: application/json');
echo json_encode(getUptime());
