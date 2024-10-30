// Обработчик для кнопки
document.getElementById('updateButton').addEventListener('click', async () => {
    try {
        // Запросим первые 5 строк из log.txt
        const logResponse = await fetch('scripts/update_repo.php?getLog=true');
        const logText = await logResponse.text();

        // Добавляем 5 строк лога в запрос пароля
        const password = prompt("Первые 5 строк из log.txt:\n" + logText + "\n\nВведите пароль для обновления:");

        if (password) {
            // Отправляем запрос на сервер с паролем
            const response = await fetch('scripts/update_repo.php', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: 'password=' + encodeURIComponent(password)
            });

            const result = await response.text();
            alert(result);
        }
    } catch (error) {
        console.error("Ошибка при отправке запроса:", error);
        alert("Произошла ошибка. Попробуйте снова.");
    }
});
