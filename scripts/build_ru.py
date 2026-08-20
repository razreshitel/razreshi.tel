from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_NODE = re.compile(r"(?<=>)([^<>]+)(?=<)")


COMMON = {
    "EN": "RU",
    "Back to all work": "Ко всем проектам",
    "PROJECT / canvas-tool-local": "ПРОЕКТ / canvas-tool-local",
    "PROJECT / flipper-tg": "ПРОЕКТ / flipper-tg",
    "PROJECT / hexploritel": "ПРОЕКТ / hexploritel",
    "PROJECT / ksp-autopilot": "ПРОЕКТ / ksp-autopilot",
    "PROJECT / povtoritel": "ПРОЕКТ / povtoritel",
    "PROJECT / videograbitel": "ПРОЕКТ / videograbitel",
    "Open project": "Открыть проект",
    "View on GitHub ↗": "Открыть на GitHub ↗",
    "Features": "Функции",
    "Components": "Компоненты",
    "What it does": "Что делает",
    "Datasheet": "Характеристики",
    "Platform": "Платформа",
    "Storage": "Хранение",
    "Status": "Статус",
    "self-hosted": "свой сервер",
    "offline-first": "автономная работа",
    "local-only": "только локально",
    "privacy-first": "конфиденциальность",
}


PAGES = {
    "index.html": {
        "Philippov A.": "Александр Филиппов",
        "I build": "Я создаю",
        "local tools with a focus on security": "локальные инструменты с фокусом на безопасность",
        ": workspaces, browser tooling, device bridges, and autonomous control systems.": ": рабочие пространства, браузерные инструменты, мосты для устройств и автономные системы управления.",
        "Below is a selection of my projects.": "Ниже собрана выборка из нескольких проектов.",
        "I mostly use Python and often extend open-source tools. I favor software built first around my own needs and capable of running entirely locally.": "В основном использую Python, часто дорабатываю open-source инструменты. Я предпочитаю программы, которые в первую очередь удобны для меня и могут быть полностю локализованы.",
        "Selected work": "Избранные проекты",
        "06 projects": "06 projects",
        "Telegram bot bridge for Flipper Zero": "Мост Telegram для Flipper Zero",
        "Read and send Telegram messages from a Flipper Zero's screen. A FastAPI server on a Raspberry Pi communicates with the device application over Wi-Fi, with Cyrillic transliteration, an on-device keyboard, paginated chats, and end-to-end encryption.": "Чтение и отправка сообщений Telegram с экрана Flipper Zero. Сервер с FastAPI на Raspberry Pi связывается с приложением через Wi-Fi, поддерживает транслитерацию кириллицы, экранную клавиатуру, постраничные чаты и end-to-end шифрование.",
        "An Android map that records where you have been. A selected area fills with hexagons that disappear as you move, adding a": "Android-приложение, карта, которая сохраняет места, где вы прошли. Выделенная область покрывается шестиугольниками, которые исчезают по мере движения добавляя элемент",
        "progressive exploration": "прогрессивного исследования",
        "layer. Key features include": ". Ключевыми функциями является",
        "GPS spoofing resistance, Google Timeline import, and offline maps from arbitrary sources": "обход GPS-спуфинга, экспорт Google Timeline, оффлайн-карты из любых источников",
        "A Chrome extension for downloading video from the current page. It supports 99% of video types encountered in practice. Processing stays local, with no uploads to external services.": "Расширение Chrome для скачивания видео с текущей страницы. Позволяет скачать 99% типов существующих видео. Вся обработка выполняется локально, загрузки на сторонние ресурсы нет.",
        "An application for instant replay or continuous recording. Recent footage stays in RAM and is saved with a global hotkey. Key features include": "Приложение для мгновенных повторов или непрерывной записи. Последние минуты хранятся в оперативной памяти и сохраняются глобальной горячей клавишей. Ключевые функции -",
        "separate audio tracks, a focused feature set, and flexible configuration": "разделение потоков аудио, отсутствие лишних функций, гибкая настройка",
        "An interactive board for notes, images, files, drawings, tables, and nested boards. Accounts, sharing, uploads, and backups run entirely locally on a personal server.": "Интерактвная доска для заметок, картинок, файлов, рисунков, таблиц и вложенных досок. Учетные записи, общий доступ, загрузки и резервные копии реализованы полностью локально для личного сервера.",
        "Automated rocket landing in KSP": "Авто-посадка ракет в KSP",
        "Python scripts that control a rocket in Kerbal Space Program without human input: one sends the vehicle into a stable orbit, while the other also returns the booster to a soft upright landing as the upper stage continues to orbit.": "Скрипты Python для управления ракетой в Kerbal Space Program без участия человека: один выводит аппарат на устойчивую орбиту, второй еще и возвращает ускоритель к мягкой вертикальной посадке, пока верхняя ступень продолжает выход на орбиту.",
        "Acknowledgements": "Благодарности",
        "01 recognition": "01 упоминание",
        "NASA VDP letter, July 9 2026. Click to open full size.": "Письмо NASA VDP от 9 июля 2026 года. Нажмите, чтобы открыть полный размер.",
        "Letter of recognition from": "Благодарственное письмо от",
        "In June 2026 I reported several": "В июне 2026 года я сообщил NASA о нескольких уязвимостях уровня",
        "vulnerabilities (NASA's highest priority category) through its Vulnerability Disclosure Program. One was a": "(категория наивысшего приоритета) через программу раскрытия уязвимостей. Среди них была",
        "CGI command injection on a *.nasa.gov host": "command injection CGI на узле *.nasa.gov",
        ". NASA sent the letter shown here and added me to its Hall of Fame.": ". За эту находку NASA направило представленное здесь благодарственное письмо и добавило меня в зал славы.",
    },
    "canvas-tool-local.html": {
        "An interactive board for notes, images, files, drawings, tables, and nested boards. Accounts, sharing, uploads, and backups run entirely locally on a personal server.": "Интерактвная доска для заметок, картинок, файлов, рисунков, таблиц и вложенных досок. Учетные записи, общий доступ, загрузки и резервные копии реализованы полностью локально для личного сервера.",
        "Its main advantages over popular existing tools are fully local operation, unique note types, and API access to notes.": "Основные преимущества перед существующими популярными проектами - полностью локальная реализация, уникальные виды заметок, возможность подключится по api к заметкам.",
        "Try it out ↗": "Попробовать ↗",
        "self-hosted workspace": "рабочее пространство на своем сервере",
        "A fully local interactive board": "Полностью локальная интерактвная доска",
        "The project combines an infinite board with structured cards, nested workspaces, search, history, and private sharing.": "Проект объединяет бесконечную доску, структурированные карточки, вложенные пространства, поиск, историю изменений и закрытый общий доступ.",
        "Workspace": "Рабочее пространство",
        "notes, tasks, files, tables, charts, diagrams, drawings, and images": "заметки, задачи, файлы, таблицы, графики, диаграммы, рисунки, картинки",
        "nested boards, indexed search, and revision restore": "вложенные доски, индексированный поиск и восстановление версий",
        "per-board sharing with live updates": "отдельный доступ к каждой доске и обновления в реальном времени",
        "Host": "Сервер",
        "Node.js service with SQLite and local uploads": "служба Node.js с SQLite и локальным хранением файлов",
        "Caddy HTTPS and authenticated file access": "HTTPS через Caddy и доступ к файлам после авторизации",
        "automatic updates from GitHub, rollback, and verified backups": "авто-обновления с github, откат и проверяемые резервные копии",
        "Frontend": "Интерфейс",
        "Runtime": "Среда",
        ", standalone systemd service": ", автономная служба systemd",
        "SQLite and local uploads": "SQLite и локальные файлы",
        ", per-account quotas and file reconciliation": ", квоты учетных записей и сверка файлов",
        "Access": "Доступ",
        "Private accounts and per-board sharing": "Закрытые учетные записи и доступ к отдельным доскам",
        ", live cross-session updates": ", синхронизация между сессиями в реальном времени",
        "Files": "Файлы",
        "Resumable uploads and rich previews": "Возобновляемые загрузки и предпросмотр файлов",
        ", authenticated download routes": ", скачивание только после авторизации",
        "Operations": "Эксплуатация",
        "Backups": "Резервные копии",
        "Daily verified archives": "Ежедневные проверяемые архивы",
        ", SQLite integrity, foreign key, checksum, and upload checks": ", проверка целостности SQLite, внешних ключей, контрольных сумм и загруженных файлов",
    },
    "flipper-tg.html": {
        "Telegram bot bridge for Flipper Zero": "Мост Telegram для Flipper Zero",
        "Telegram bot bridge for Flipper&nbsp;Zero": "Мост Telegram для Flipper&nbsp;Zero",
        "Read and send Telegram messages directly from a Flipper Zero's screen. A FastAPI server on a Raspberry Pi connects to the FAP application through an ESP32 Wi-Fi bridge.": "Чтение и отправка сообщений Telegram прямо с экрана Flipper Zero. Сервер с FastAPI на Raspberry Pi связывается с приложением FAP через Wi-Fi-мост на ESP32.",
        "The Flipper application includes an on-device keyboard, Cyrillic transliteration, paginated chats, and full end-to-end message encryption.": "Приложение на Flipper поддерживает экранную клавиатуру, транслитерацию кириллицы, постраничные чаты и имеет полное end-to-end шифрование сообщений.",
        "Every message available to the bot is stored in the server database.": "Все сообщения, доступные боту, сохраняются в базе данных сервера.",
        "Traffic between the server and the Flipper is encrypted with a shared secret, and a web UI allows browsing and deleting stored messages from a browser.": "Трафик между сервером и Flipper шифруется общим секретом. Веб-интерфейс позволяет просматривать и удалять сохраненные сообщения.",
        "If Telegram access is normally blocked, only the server needs a VPN.": "Если доступ к Telegram обычно заблокирован, VPN будет нужен только на сервере.",
    },
    "hexploritel.html": {
        "An Android map that records where you have been. A selected area fills with hexagons that disappear as you move, adding a": "Android-приложение, карта, которая сохраняет места, где вы прошли. Выделенная область покрывается шестиугольниками, которые исчезают по мере движения добавляя элемент",
        "progressive exploration": "прогрессивного исследования",
        "layer. Key features include": ". Ключевыми функциями является",
        "GPS spoofing resistance, Google Timeline import, and offline maps from arbitrary sources.": "обход GPS-спуфинга, экспорт Google Timeline, оффлайн-карты из любых источников.",
        "Track recording and GPX import and export are also supported.": "Так же поддерживается запись маршрутов, импорт и экспорт GPX.",
        "06 features": "06 функций",
        "Explore": "Исследование",
        "Uncover the map on foot": "Открывайте карту пешком",
        "Draw an area anywhere on the map and it fills with grey hexagons. They clear wherever you have physically been, so the map opens only in visited locations. You can redraw or delete an area later without losing the ground you have already covered.": "Выделите область на карте, и она заполнится серыми шестиугольниками. Они исчезают там, где вы физически были, поэтому карта открывается только в посещенных местах. Область можно изменить или удалить без потери уже пройденной территории.",
        "Record": "Запись",
        "Track walks": "Записывайте прогулки",
        "Record a route and get its distance, moving time, speed, ascent and stops, with a speed-coloured line on the map and elevation/speed charts for every walk.": "Записывайте маршрут с расстоянием, временем в движении, скоростью, набором высоты и остановками. Для каждой прогулки доступны линия с цветом по скорости и графики высоты и скорости.",
        "Offline": "Без сети",
        "Offline maps": "Офлайн-карты",
        "Download any region as a single file and the map keeps working fully offline, which helps where tiles are slow or blocked. When online it streams fast map tiles instantly, then falls back to the downloaded maps the moment the signal drops. The first 4 zoom levels of the world map are built in.": "Загрузите любой регион одним файлом, и карта продолжит работать без сети. При подключении приложение использует потоковые тайлы, а после потери сигнала переключается на сохраненные карты. Первые четыре уровня масштаба мировой карты встроены в приложение.",
        "Filter": "Фильтрация",
        "GPS spoof filtering": "Фильтрация подмены GPS",
        "A configurable filter chain rejects fake, mocked, and physically impossible position fixes, so distance, routes, and coverage stay accurate even in areas with heavy GPS spoofing. It remains active while a track is being recorded.": "Настраиваемая цепочка фильтров отбрасывает поддельные и физически невозможные координаты, чтобы расстояния, маршруты и покрытие оставались точными даже при активной подмене GPS. Работает во время записи трека.",
        "Data": "Данные",
        "Import, export, back up": "Импорт, экспорт и резервные копии",
        "Import tracks from other apps or export them as GPX, and save everything (tracks, areas, coverage, settings) to a single backup file.": "Импортируйте маршруты из других приложений или экспортируйте их в GPX. Маршруты, области, покрытие и настройки можно сохранить в одном резервном файле.",
        "Import accepts GPX and Google Timeline JSON, and short tracks can be filtered out after import.": "Импорт поддерживает GPX и JSON из Google Timeline. Короткие маршруты можно отфильтровать после импорта.",
        "Tune": "Настройка",
        "Themes and settings": "Темы и параметры",
        "Switch between light and dark themes, pick the hexagon colour, adjust how much each step clears and how strictly fixes are filtered, and choose the online and offline map sources: a preset or your own tile URL.": "Переключайте светлую и темную темы, выбирайте цвет шестиугольников, радиус очистки и строгость фильтра координат. Для онлайн- и офлайн-карт можно использовать готовый источник или собственный URL тайлов.",
        "Screenshots": "Скриншоты",
        "07 captures, on device": "07 снимков с устройства",
        "Stack": "Стек",
        "Maps": "Карты",
        "Coverage": "Покрытие",
        "local-only, excluded from cloud and adb backup": "только локально, исключено из облачных и adb-копий",
        "res-11 visited cells, zoom-driven display resolution": "посещенные ячейки res-11 и детализация по масштабу карты",
        "Interchange": "Обмен данными",
        "import and export, full zip backup and restore": "импорт и экспорт, полное резервное копирование и восстановление из zip",
        "Beta": "Бета",
        "currently distributed privately": "в данный момент распространяется приватно",
        "Map data © OpenStreetMap contributors, basemap by Protomaps": "Map data © OpenStreetMap contributors, basemap by Protomaps",
    },
    "ksp-autopilot.html": {
        "Automated rocket landing in KSP": "Автономные ракеты в KSP",
        "Automated rocket landing in Kerbal Space Program": "Авто-посадка ракет в Kerbal Space Program",
        "Python autopilot scripts that fly rockets in Kerbal Space Program without human input, driving the game live over the kRPC mod: telemetry streams out, control commands stream in, over TCP. One script launches a vessel into a permanent, stable orbit. The second includes the first and also returns the booster to a soft upright landing near the pad while the upper stage reaches orbit. Verified in-game across 25 autonomous flights. It is currently a personal project rather than a public product.": "Скрипты автопилота на Python управляют ракетами в Kerbal Space Program без участия человека через мод kRPC: телеметрия и команды управления передаются по TCP. Один скрипт выводит аппарат на устойчивую орбиту, второй включает в себя первый, но дополнительно возвращает ускоритель к мягкой вертикальной посадке возле площадки, пока верхняя ступень выходит на орбиту. Работа проверена в игре в 25 автономных полетах. В данный моент является личным проектом, а не публичным продуктом.",
        "guidance &amp; control": "наведение и управление",
        "no computer vision": "без компьютерного зрения",
        "sensor-only": "только телеметрия",
        "02 scripts": "02 скрипта",
        "Scripts": "Скрипты",
        "Launch to orbit": "Запуск на орбиту",
        "Launch to a permanent orbit": "Выход на устойчивую орбиту",
        "flies the active vessel through a gravity-turn ascent and circularizes at apoapsis into a stable orbit that will not decay, 70 to 80 km by default. It handles single-stage and two-stage rockets: a two-stage craft stages automatically, dropping the first stage once its fuel runs out and finishing the orbit on the second.": "проводит активный аппарат через гравитационный разворот и выполняет циркуляризацию в апоцентре, формируя устойчивую орбиту высотой 70-80 км. Поддерживаются одно- и двухступенчатые ракеты. Для двухступенчатой схемы первая ступень отделяется после выработки топлива, а вторая завершает выход на орбиту.",
        "Target altitude, gravity-turn end, the first-stage fuel reserve, and an optional physics time-warp to run the ascent faster are all tunable from the command line.": "Целевая высота, завершение гравитационного разворота, запас топлива первой ступени и ускорение физики настраиваются через командную строку.",
        "Launch and recover": "Запуск и возврат",
        "Launch and fly the booster back": "Запуск и возврат ускорителя",
        "runs a Falcon-9-style profile on a two-stage rocket: launch, then separate the first stage once it burns down to a set fuel limit (30% by default). From there both stages are flown at once in a single control loop: the booster turns around, burns back toward the pad, deploys airbrakes on descent, and brakes to a soft upright touchdown, while the second stage carries on to orbit.": "выполняет профиль двухступенчатой ракеты по типу Falcon 9: запуск и отделение первой ступени после достижения заданного остатка топлива, по умолчанию 30%. Затем обе ступени одновременно управляются в одном цикле. Ускоритель разворачивается, выполняет возвратный импульс, выпускает аэродинамические тормоза и мягко садится вертикально, пока вторая ступень продолжает выход на орбиту.",
        "Best run to date: the booster landed undamaged, 0.3° off vertical, descending at 2.85 m/s at touchdown, with the upper stage in a stable 70.5 × 84 km orbit on the same flight.": "Лучший результат: ускоритель приземлился без повреждений с отклонением 0,3° от вертикали и скоростью снижения 2,85 м/с. В том же полете верхняя ступень вышла на устойчивую орбиту 70,5 × 84 км.",
        "Full flight footage": "Запись полного полета",
        "second script / full mission": "второй скрипт / полная миссия",
        "Your browser doesn't support embedded video - the file is at": "Браузер не поддерживает встроенное видео. Файл находится по адресу",
        "end to end: launch, stage separation, and the booster flying itself back to a powered vertical landing, with an inset of the second stage reaching orbit at the same moment.": "полная миссия: запуск, разделение ступеней и автономный возврат ускорителя к вертикальной посадке. Во вставке показан одновременный выход второй ступени на орбиту.",
        "Constraints": "Ограничения",
        "Sensor-only flight": "Полет только по бортовым данным",
        "The autopilot reads": "Автопилот получает",
        "only": "только",
        "what a real flight computer could, then derives the rest itself: orbital elements, time to apoapsis, the landing burn, and a drag-aware prediction of where the booster will fall, the way real avionics would.": "данные, доступные реальному бортовому компьютеру, а остальные значения рассчитывает сам: параметры орбиты, время до апоцентра, момент посадочного импульса и прогноз точки падения с учетом сопротивления воздуха.",
        "Used: onboard sensing": "Используются бортовые данные",
        "position &amp; velocity (GPS / INS)": "положение и скорость (GPS / INS)",
        "altitude &amp; radar altitude": "высота и радиовысота",
        "vertical speed &amp; speed": "вертикальная и полная скорость",
        "mass, thrust, remaining fuel": "масса, тяга и остаток топлива",
        "attitude": "ориентация",
        "an onboard atmosphere / drag model": "бортовая модель атмосферы и сопротивления",
        "Not used: game metadata": "Не используются данные игры",
        "map-view apoapsis / periapsis": "апоцентр и перицентр с карты",
        "the game's predicted impact point": "расчетная точка падения из игры",
        "maneuver-node Δv": "Δv узла маневра",
        "anything a real booster could not sense": "данные, недоступные реальному ускорителю",
        "classical guidance": "классическое наведение",
        "Interface": "Интерфейс",
        "over TCP, RPC and telemetry streams": "через TCP, RPC и потоки телеметрии",
        "Guidance": "Наведение",
        "vis-viva equation": "vis-viva формула",
        "gravity-turn pitch program, suicide-burn solver": "программа гравитационного разворота и расчет посадочного импульса",
        "Control": "Управление",
        "PID loops": "ПИД-регуляторы",
        "slew-rate-limited attitude on reaction wheels (no gimbal)": "ограничение скорости поворота и маховики без управления вектором тяги",
        "Sensing": "Датчики",
        "Onboard state only": "Только бортовое состояние",
        "position, velocity, mass, thrust, fuel, attitude, radar altitude, in-house drag model": "положение, скорость, масса, тяга, топливо, ориентация, радиовысота и собственная модель сопротивления",
        "Mods": "Моды",
        "plus Physics Range Extender (keeps both stages simulated apart)": "и Physics Range Extender для одновременной симуляции разделенных ступеней",
        "Tests": "Тесты",
        "93 pytest tests": "93 теста pytest",
        "over the pure-math guidance layer": "для математического слоя наведения",
        "Verified across &gt;25 flights": "Проверено на >25 полетах",
        "booster returns upright and intact": "ускоритель возвращается вертикально и без повреждений",
    },
    "povtoritel.html": {
        "An application for instant replay or continuous recording. Recent footage stays in RAM and is saved with a global hotkey. Key features include": "Приложение для мгновенных повторов или непрерывной записи. Последние минуты хранятся в оперативной памяти и сохраняются глобальной горячей клавишей. Ключевые функции -",
        "separate audio tracks, a focused feature set, and flexible configuration.": "разделение потоков аудио, отсутствие лишних функций, гибкая настройка.",
        "The current implementation is Windows-only.": "Текущая реализация только для Windows",
        "Hardware encoding": "Аппаратное кодирование",
        "Fully local": "Полностью локально",
        "local capture": "локальный захват",
        "Replay and recording from one capture pipeline": "Повтор и запись из одного конвейера захвата",
        "Povtoritel keeps the last one to ten minutes in RAM and saves the buffer to MP4 with a global hotkey. The same pipeline can record continuously when needed.": "Povtoritel хранит последние 1-10 минут в оперативной памяти и сохраняет буфер в MP4 глобальной горячей клавишей. При необходимости тот же конвейер ведет непрерывную запись.",
        "Instant replay": "Мгновенный повтор",
        "one to ten minute replay buffer": "сохранение 1-10 минут в буфер для быстрого повтора",
        "adjustable system resource usage": "регулировка системных ресурсов",
        "selectable bitrate": "возможность выбора битрейта",
        "separate audio channels for every source": "раздельные каналы аудио для кажого источника",
        "Continuous recording": "Непрерывная запись",
        "start and stop with a global hotkey": "запуск и остановка глобальной горячей клавишей",
        "desktop, microphone, and per-app audio": "звук рабочего стола, микрофона и отдельных приложений",
        "local MP4 output from the system tray": "локальная запись MP4 с управлением из системного трея",
        "Settings": "Настройки",
        "Windows desktop": "приложение Windows",
        ", Python 3.12 or newer": ", Python 3.12 или новее",
        "Capture": "Захват",
        ", one selected display": ", один выбранный дисплей",
        "Encoding": "Кодирование",
        ", H.264 hardware encoding": ", аппаратное кодирование H.264",
        "Replay": "Повтор",
        "1 to 10 minutes in RAM": "1-10 минут в оперативной памяти",
        ", MP4 output on demand": ", сохранение MP4 по запросу",
        "Frame rate": "Частота кадров",
        "30, 60, 120, or 144 FPS": "30, 60, 120 или 144 FPS",
        "Audio": "Звук",
        "Desktop mix, microphone, and per-application tracks": "микс рабочего стола, микрофон и дорожки отдельных приложений",
        "Operation": "Управление",
        "System tray, global hotkeys, autostart": "системный трей, глобальные горячие клавиши и автозапуск",
        ", automatic recovery after display sleep": ", автоматическое восстановление после отключения дисплея",
    },
    "videograbitel.html": {
        "An open-source, fully local in-browser video downloader. It detects media in HLS and DASH streams, on YouTube, and on roughly 1800 other sites, then downloads and converts it on your own machine with yt-dlp and ffmpeg. No servers, no uploads, nothing leaves your computer.": "Полностью локальный загрузчик видео с открытым исходным кодом. Он находит медиа в потоках HLS и DASH, на Youtube или примерно на 1800 других сайтах, затем скачивает и преобразует их на вашем компьютере с помощью yt-dlp и ffmpeg. Серверы и внешние загрузки не используются.",
        "Local Node host": "Node Local",
    },
}


ATTRS = {
    "index.html": {
        '<meta property="og:url" content="https://razreshi.tel/" />': '<meta property="og:url" content="https://razreshi.tel/ru/" />',
        '<meta property="og:locale" content="en_US" />': '<meta property="og:locale" content="ru_RU" />',
        '<meta property="og:locale:alternate" content="ru_RU" />': '<meta property="og:locale:alternate" content="en_US" />',
        '<meta property="og:site_name" content="Alexander Philippov" />': '<meta property="og:site_name" content="Александр Филиппов" />',
        '<meta property="og:title" content="Alexander Philippov" />': '<meta property="og:title" content="Александр Филиппов" />',
        '<meta property="og:description" content="Portfolio of self-hosted software and hardware projects" />': '<meta property="og:description" content="Портфолио локальных программных и аппаратных проектов" />',
        '<meta name="twitter:description" content="Portfolio of self-hosted software and hardware projects" />': '<meta name="twitter:description" content="Портфолио локальных программных и аппаратных проектов" />',
        '<meta name="twitter:title" content="Alexander Philippov" />': '<meta name="twitter:title" content="Александр Филиппов" />',
        '<meta name="description" content="Alexander Philippov. Portfolio of self-hosted software and hardware projects." />': '<meta name="description" content="Александр Филиппов. Портфолио локальных программных и аппаратных проектов." />',
        '<link rel="canonical" href="https://razreshi.tel/" />': '<link rel="canonical" href="https://razreshi.tel/ru/" />',
        'href="favicon.svg"': 'href="../favicon.svg"',
        'href="apple-touch-icon.png"': 'href="../apple-touch-icon.png"',
        'href="styles.css"': 'href="../styles.css"',
        'href="assets/': 'href="../assets/',
        'src="assets/': 'src="../assets/',
        'src="name-selection.js"': 'src="../name-selection.js"',
        'aria-label="Social links"': 'aria-label="Социальные ссылки"',
        'alt="NASA Vulnerability Disclosure Program letter of recognition addressed to Razreshitel, dated July 9 2026"': 'alt="Благодарственное письмо программы раскрытия уязвимостей NASA для Razreshitel от 9 июля 2026 года"',
    },
    "canvas-tool-local.html": {
        '<meta name="description" content="Canvas, a self-hosted visual workspace for notes, tasks, files, diagrams, tables, and nested boards." />': '<meta name="description" content="Canvas, визуальное рабочее пространство для заметок, задач, файлов, диаграмм, таблиц и вложенных досок." />',
    },
    "flipper-tg.html": {
        '<meta name="description" content="A self-hosted Telegram bridge for reading and sending messages from a Flipper Zero." />': '<meta name="description" content="Локальный мост Telegram для чтения и отправки сообщений с Flipper Zero." />',
    },
    "hexploritel.html": {
        '<meta name="description" content="HexPlor\'itel, an offline-first Android map that records where you have actually walked." />': '<meta name="description" content="HexPlor\'itel, автономная Android-карта, которая сохраняет места, где вы действительно прошли." />',
        'alt="Cleared hexagons seen zoomed out across the US West coast"': 'alt="Открытые шестиугольники на западном побережье США"',
        'alt="Grey hexagons cleared into an L-shape along a walked route"': 'alt="Серые шестиугольники, открытые вдоль пройденного маршрута"',
        'alt="A purple polyline tracing a recorded walk in real time"': 'alt="Фиолетовая линия записываемой прогулки"',
        'alt="Track detail with speed-coloured route and per-track statistics and charts"': 'alt="Маршрут с цветом по скорости, статистикой и графиками"',
        'alt="Settings showing offline auto-cache and the GPS spoof-rejection controls"': 'alt="Настройки офлайн-кэша и фильтрации подмены GPS"',
        'alt="The same settings with GPS filtering switched off and the controls greyed out"': 'alt="Настройки с отключенной фильтрацией GPS"',
        'alt="Settings for coverage padding, hex colour, track smoothing and the map source URL"': 'alt="Настройки покрытия, цвета шестиугольников, сглаживания маршрута и источника карты"',
    },
    "ksp-autopilot.html": {
        '<meta name="description" content="Python autopilots for autonomous launch, orbit insertion, and booster recovery in Kerbal Space Program." />': '<meta name="description" content="Автопилоты на Python для автономного запуска, выхода на орбиту и возврата ускорителя в Kerbal Space Program." />',
    },
    "povtoritel.html": {
        '<meta name="description" content="Povtoritel, a local Windows application for instant replay and continuous screen recording." />': '<meta name="description" content="Povtoritel, локальное приложение Windows для мгновенных повторов и непрерывной записи экрана." />',
    },
    "videograbitel.html": {
        '<meta name="description" content="VideoGrab\'itel, a fully local browser video downloader for YouTube, HLS, DASH, and direct media files." />': '<meta name="description" content="VideoGrab\'itel, полностью локальный загрузчик видео из YouTube, HLS, DASH и прямых медиафайлов." />',
    },
}


def replace_text(html: str, translations: dict[str, str]) -> str:
    def substitute(match: re.Match[str]) -> str:
        raw = match.group(1)
        normalized = " ".join(raw.split())
        translated = translations.get(normalized)
        if translated is None:
            return raw
        leading = raw[: len(raw) - len(raw.lstrip())]
        trailing = raw[len(raw.rstrip()) :]
        return f"{leading}{translated}{trailing}"

    return TEXT_NODE.sub(substitute, html)


def build_page(source: Path) -> None:
    name = source.name
    html = source.read_text(encoding="utf-8").replace("\r\n", "\n")
    html = html.replace('<html lang="en">', '<html lang="ru">')
    for old, new in ATTRS.get(name, {}).items():
        if old not in html:
            raise RuntimeError(f"Missing attribute in {name}: {old}")
        html = html.replace(old, new)

    if source.parent.name == "projects":
        slug = source.stem
        html = html.replace(
            f'<link rel="canonical" href="https://razreshi.tel/projects/{slug}" />',
            f'<link rel="canonical" href="https://razreshi.tel/ru/projects/{slug}" />',
        )
        html = html.replace('href="../favicon.svg"', 'href="../../favicon.svg"')
        html = html.replace('href="../apple-touch-icon.png"', 'href="../../apple-touch-icon.png"')
        html = html.replace('href="../styles.css"', 'href="../../styles.css"')
        html = html.replace('src="../assets/', 'src="../../assets/')
        html = html.replace('poster="../assets/', 'poster="../../assets/')
        html = html.replace('src="../lightbox.js"', 'src="../../lightbox.js"')

    html = html.replace('aria-label="Choose language">EN', 'aria-label="Выбрать язык">RU')
    html = html.replace('aria-label="Language"', 'aria-label="Язык"')
    html = html.replace(' hreflang="en" aria-current="page">English', ' hreflang="en">English')
    html = html.replace(' hreflang="ru">Русский', ' hreflang="ru" aria-current="page">Русский')
    html = replace_text(html, COMMON | PAGES[name])

    target = ROOT / "ru" / ("projects" if source.parent.name == "projects" else "") / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8", newline="\n")


def main() -> None:
    build_page(ROOT / "index.html")
    for source in sorted((ROOT / "projects").glob("*.html")):
        build_page(source)


if __name__ == "__main__":
    main()
