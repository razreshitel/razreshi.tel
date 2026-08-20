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
        "self-hosted, privacy-first tools": "локальные инструменты под собственным управлением",
        ": AI workspaces, browser tooling, firmware bridges, and autonomous control systems.": ": рабочие пространства, браузерные инструменты, мосты для устройств и автономные системы управления.",
        "A selection of my projects is below.": "Ниже собраны основные проекты.",
        "Mostly": "В основном",
        "or": "или",
        ", built on open-source tools. I favor software that runs on my own machines and does not depend on outside infrastructure.": ", на основе открытых инструментов. Я предпочитаю программы, которые работают на моих устройствах и не зависят от внешней инфраструктуры.",
        "Selected work": "Избранные проекты",
        "06 projects": "06 проектов",
        "Telegram bot bridge for Flipper Zero": "Мост Telegram для Flipper Zero",
        "Read and send Telegram messages from a Flipper Zero's screen. A self-hosted FastAPI server on a Raspberry Pi talks to a custom FAP application over an ESP32 Wi-Fi bridge, with Cyrillic transliteration, paginated chats, an on-device keyboard, and encrypted transport.": "Чтение и отправка сообщений Telegram с экрана Flipper Zero. Сервер FastAPI на Raspberry Pi связывается с приложением FAP через Wi-Fi-мост на ESP32, поддерживает транслитерацию кириллицы, постраничные чаты, экранную клавиатуру и шифрование.",
        "An Android map application that keeps a record of where you have actually walked. Draw an area and it fills with hexagons that clear as you physically pass through them. Supports track recording, GPX import and export, and Google Timeline import.": "Android-карта, которая сохраняет места, где вы действительно прошли. Выделенная область покрывается шестиугольниками, которые исчезают по мере движения. Поддерживаются запись маршрутов, импорт и экспорт GPX, а также импорт Google Timeline.",
        "A Chrome extension that detects and downloads video from the current page: YouTube, HLS and MPEG-DASH streams, or direct files. Processing is fully local and nothing is uploaded.": "Расширение Chrome находит и скачивает видео с текущей страницы: YouTube, потоки HLS и MPEG-DASH или прямые файлы. Вся обработка выполняется локально, загрузки на сторонние серверы нет.",
        "A Windows instant replay and continuous recorder that keeps recent footage in RAM and saves it on a global hotkey. Screen capture, hardware encoding, and audio processing stay on the local machine.": "Приложение Windows для мгновенных повторов и непрерывной записи. Последние минуты хранятся в оперативной памяти и сохраняются глобальной горячей клавишей. Захват экрана, аппаратное кодирование и обработка звука выполняются локально.",
        "A self-hosted visual workspace for notes, tasks, files, diagrams, tables, and nested boards. It runs on Node.js with SQLite and keeps accounts, sharing, uploads, and backups on your own server.": "Визуальное рабочее пространство для заметок, задач, файлов, диаграмм, таблиц и вложенных досок. Оно работает на Node.js и SQLite, а учетные записи, общий доступ, загрузки и резервные копии остаются на вашем сервере.",
        "Autonomous rockets in KSP": "Автономные ракеты в KSP",
        "Python scripts that fly rockets in Kerbal Space Program without human input: one launches a vessel to a permanent orbit, the other returns the booster to a soft upright landing while the upper stage continues to orbit.": "Скрипты Python управляют ракетами в Kerbal Space Program без участия человека: один выводит аппарат на устойчивую орбиту, второй возвращает ускоритель к мягкой вертикальной посадке, пока верхняя ступень продолжает выход на орбиту.",
        "Guidance runs on onboard telemetry only, never on the game's map view.": "Наведение использует только бортовую телеметрию и не обращается к данным карты игры.",
        "Certifications": "Признание",
        "01 recognition": "01 упоминание",
        "NASA VDP letter, July 9 2026. Click to open full size.": "Письмо NASA VDP от 9 июля 2026 года. Нажмите, чтобы открыть полный размер.",
        "Letter of recognition and Hall of Fame": "Благодарственное письмо и Hall of Fame",
        "In June 2026 I reported multiple": "В июне 2026 года я сообщил NASA о нескольких уязвимостях уровня",
        "(their highest severity rating) vulnerabilities to NASA through their Vulnerability Disclosure Program. Including, a": "(максимальная категория критичности в их системе) через программу раскрытия уязвимостей. Среди них была",
        "CGI command injection on a *.nasa.gov host": "командная инъекция CGI на узле *.nasa.gov",
        ", For that finding NASA sent me the letter of recognition shown here and added me to their Hall of Fame.": ". За эту находку NASA направило представленное здесь благодарственное письмо и добавило меня в Hall of Fame.",
    },
    "canvas-tool-local.html": {
        "A self-hosted visual workspace for notes, tasks, files, diagrams, tables, charts, and nested boards. Accounts, workspace data, sharing, and uploads stay on your own server.": "Визуальное рабочее пространство для заметок, задач, файлов, диаграмм, таблиц, графиков и вложенных досок. Учетные записи, данные, общий доступ и загрузки остаются на вашем сервере.",
        "Try it out ↗": "Попробовать ↗",
        "self-hosted workspace": "рабочее пространство на своем сервере",
        "A visual workspace on your own server": "Визуальное пространство на своем сервере",
        "Canvas combines an infinite board with structured cards, nested workspaces, search, history, and private sharing.": "Canvas объединяет бесконечную доску, структурированные карточки, вложенные пространства, поиск, историю изменений и закрытый общий доступ.",
        "Workspace": "Рабочее пространство",
        "notes, tasks, files, tables, charts, and diagrams": "заметки, задачи, файлы, таблицы, графики и диаграммы",
        "nested boards, indexed search, and revision restore": "вложенные доски, индексированный поиск и восстановление версий",
        "per-board sharing with live updates": "отдельный доступ к каждой доске и обновления в реальном времени",
        "Host": "Сервер",
        "Node.js service with SQLite and local uploads": "служба Node.js с SQLite и локальным хранением файлов",
        "Caddy HTTPS and authenticated file access": "HTTPS через Caddy и доступ к файлам после авторизации",
        "atomic updates, rollback, and verified backups": "атомарные обновления, откат и проверяемые резервные копии",
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
        "Read and send Telegram messages directly from a Flipper Zero's screen. A self-hosted FastAPI server on a Raspberry Pi talks to a custom FAP application over an ESP32 Wi-Fi bridge, with Cyrillic transliteration, paginated chats, and an on-device keyboard.": "Чтение и отправка сообщений Telegram прямо с экрана Flipper Zero. Сервер FastAPI на Raspberry Pi связывается с приложением FAP через Wi-Fi-мост на ESP32, поддерживает транслитерацию кириллицы, постраничные чаты и экранную клавиатуру.",
        "Every message the bot sees is stored in the server's database.": "Все сообщения, доступные боту, сохраняются в базе данных сервера.",
        "Traffic between the server and the Flipper is encrypted with a shared secret, and a web UI allows browsing and deleting stored messages from a browser.": "Трафик между сервером и Flipper шифруется общим секретом. Веб-интерфейс позволяет просматривать и удалять сохраненные сообщения.",
    },
    "hexploritel.html": {
        "An Android map application that keeps a record of where you have actually walked. Draw an area and it fills with hexagons that clear as you physically pass through them. Supports track recording, GPX import and export, and Google Timeline import.": "Android-карта, которая сохраняет места, где вы действительно прошли. Выделенная область покрывается шестиугольниками, которые исчезают по мере движения. Поддерживаются запись маршрутов, импорт и экспорт GPX, а также импорт Google Timeline.",
        "06 features": "06 функций",
        "Explore": "Исследование",
        "Uncover the map on foot": "Открывайте карту пешком",
        "Draw an area anywhere on the map and it fills with grey hexagons. They clear wherever you physically walk, so the map opens up only where you have actually been. You can redraw or delete an area later without losing the ground you have already covered.": "Выделите область на карте, и она заполнится серыми шестиугольниками. Они исчезают там, где вы физически прошли, поэтому карта открывается только в посещенных местах. Область можно изменить или удалить без потери уже пройденной территории.",
        "Record": "Запись",
        "Track walks": "Записывайте прогулки",
        "Record a route and get its distance, moving time, speed, ascent and stops, with a speed-coloured line on the map and elevation/speed charts for every walk.": "Записывайте маршрут с расстоянием, временем в движении, скоростью, набором высоты и остановками. Для каждой прогулки доступны линия с цветом по скорости и графики высоты и скорости.",
        "Offline": "Без сети",
        "Offline maps": "Офлайн-карты",
        "Download any region as a single file and the map keeps working fully offline, which helps where tiles are slow or blocked. When online it streams fast map tiles instantly, then falls back to the downloaded maps the moment the signal drops. The first 4 zoom levels of the world map are built in.": "Загрузите любой регион одним файлом, и карта продолжит работать без сети. При подключении приложение использует потоковые тайлы, а после потери сигнала переключается на сохраненные карты. Первые четыре уровня масштаба мировой карты встроены в приложение.",
        "Filter": "Фильтрация",
        "GPS spoof filtering": "Фильтрация подмены GPS",
        "A configurable filter chain rejects fake, mocked, and physically impossible position fixes, so distance, routes, and coverage stay accurate even in areas with heavy GPS spoofing.": "Настраиваемая цепочка фильтров отбрасывает поддельные и физически невозможные координаты, чтобы расстояния, маршруты и покрытие оставались точными даже при активной подмене GPS.",
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
        "daily driver on my own device": "ежедневно используется на моем устройстве",
        "Map data © OpenStreetMap contributors, basemap by Protomaps": "Данные карты © участники OpenStreetMap, базовая карта Protomaps",
    },
    "ksp-autopilot.html": {
        "Autonomous rockets in KSP": "Автономные ракеты в KSP",
        "Autonomous rockets in Kerbal Space Program": "Автономные ракеты в Kerbal Space Program",
        "Python autopilot scripts that fly rockets in Kerbal Space Program without human input, driving the game live over the kRPC mod: telemetry streams out, control commands stream in, over TCP. Two scripts do the work: one launches a vessel to a permanent, stable orbit; the other flies a booster back to a soft upright landing near the pad while the upper stage reaches orbit on the same flight. Verified in-game across 25 autonomous flights. A hobby project, not a product.": "Скрипты автопилота на Python управляют ракетами в Kerbal Space Program без участия человека через мод kRPC: телеметрия и команды управления передаются по TCP. Один скрипт выводит аппарат на устойчивую орбиту, второй возвращает ускоритель к мягкой вертикальной посадке возле площадки, пока верхняя ступень выходит на орбиту. Работа проверена в игре в 25 автономных полетах. Это личный проект, а не продукт.",
        "guidance &amp; control": "наведение и управление",
        "no computer vision": "без компьютерного зрения",
        "sensor-only": "только телеметрия",
        "02 scripts": "02 скрипта",
        "Orbit": "Орбита",
        "Launch to a permanent orbit": "Выход на устойчивую орбиту",
        "flies the active vessel through a gravity-turn ascent and circularizes at apoapsis into a stable orbit that will not decay, 70 to 80 km by default. It handles single-stage and two-stage rockets: a two-stage craft stages automatically, dropping the first stage once its fuel runs out and finishing the orbit on the second.": "проводит активный аппарат через гравитационный разворот и выполняет циркуляризацию в апоцентре, формируя устойчивую орбиту высотой 70-80 км. Поддерживаются одно- и двухступенчатые ракеты. Для двухступенчатой схемы первая ступень отделяется после выработки топлива, а вторая завершает выход на орбиту.",
        "Target altitude, gravity-turn end, the first-stage fuel reserve, and an optional physics time-warp to run the ascent faster are all tunable from the command line.": "Целевая высота, завершение гравитационного разворота, запас топлива первой ступени и ускорение физики настраиваются через командную строку.",
        "Recover": "Возврат",
        "Launch and fly the booster back": "Запуск и возврат ускорителя",
        "runs a Falcon-9-style profile on a two-stage rocket: launch, then separate the first stage once it burns down to a set fuel limit (30% by default). From there both stages are flown at once in a single control loop: the booster turns around, burns back toward the pad, deploys airbrakes on descent, and brakes to a soft upright touchdown, while the second stage carries on to orbit.": "выполняет профиль двухступенчатой ракеты по типу Falcon 9: запуск и отделение первой ступени после достижения заданного остатка топлива, по умолчанию 30%. Затем обе ступени одновременно управляются в одном цикле. Ускоритель разворачивается, выполняет возвратный импульс, выпускает аэродинамические тормоза и мягко садится вертикально, пока вторая ступень продолжает выход на орбиту.",
        "Best run to date: the booster landed undamaged, 0.3° off vertical, descending at 2.85 m/s at touchdown, with the upper stage in a stable 70.5 × 84 km orbit on the same flight.": "Лучший результат: ускоритель приземлился без повреждений с отклонением 0,3° от вертикали и скоростью снижения 2,85 м/с. В том же полете верхняя ступень вышла на устойчивую орбиту 70,5 × 84 км.",
        "Flight footage": "Запись полета",
        "second run / full mission": "второй запуск / полная миссия",
        "Your browser doesn't support embedded video - the file is at": "Браузер не поддерживает встроенное видео. Файл находится по адресу",
        "end to end: launch, stage separation, and the booster flying itself back to a powered vertical landing, with an inset of the second stage reaching orbit at the same moment.": "полная миссия: запуск, разделение ступеней и автономный возврат ускорителя к вертикальной посадке. Во вставке показан одновременный выход второй ступени на орбиту.",
        "The constraint": "Ограничение",
        "Sensor-only flight": "Полет только по бортовым данным",
        "The autopilot reads only what a real flight computer could, then derives the rest itself: orbital elements, time to apoapsis, the landing burn, and a drag-aware prediction of where the booster will fall, the way real avionics would.": "Автопилот получает только данные, доступные реальному бортовому компьютеру, а остальные значения рассчитывает сам: параметры орбиты, время до апоцентра, момент посадочного импульса и прогноз точки падения с учетом сопротивления воздуха.",
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
        "~93 pytest tests": "около 93 тестов pytest",
        "over the pure-math guidance layer": "для математического слоя наведения",
        "Verified in-game": "Проверено в игре",
        "booster recovered upright and intact": "ускоритель вернулся вертикально и без повреждений",
    },
    "povtoritel.html": {
        "A Windows application for instant replay and continuous screen recording. It keeps recent footage in RAM, saves it to MP4 on demand, and runs locally from the system tray.": "Приложение Windows для мгновенных повторов и непрерывной записи экрана. Последние минуты хранятся в оперативной памяти, сохраняются в MP4 по запросу, а управление доступно из системного трея.",
        "hardware encoding": "аппаратное кодирование",
        "local capture": "локальный захват",
        "Replay and recording from one capture pipeline": "Повтор и запись из одного конвейера захвата",
        "Povtoritel keeps the last one to ten minutes in RAM and saves the buffer to MP4 with a global hotkey. The same pipeline can record continuously when needed.": "Povtoritel хранит последние 1-10 минут в оперативной памяти и сохраняет буфер в MP4 глобальной горячей клавишей. При необходимости тот же конвейер ведет непрерывную запись.",
        "Instant replay": "Мгновенный повтор",
        "one to ten minute RAM buffer": "буфер на 1-10 минут в оперативной памяти",
        "save after the moment has happened": "сохранение уже произошедшего момента",
        "NVIDIA or AMD hardware encoding": "аппаратное кодирование NVIDIA или AMD",
        "Continuous recording": "Непрерывная запись",
        "start and stop with a global hotkey": "запуск и остановка глобальной горячей клавишей",
        "desktop, microphone, and per-app audio": "звук рабочего стола, микрофона и отдельных приложений",
        "local MP4 output from the system tray": "локальная запись MP4 с управлением из системного трея",
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
        "An open-source, fully local in-browser video downloader. It detects media on YouTube, in HLS and DASH streams, and on roughly 1800 other sites, then downloads and converts it on your own machine with yt-dlp and ffmpeg. No servers, no uploads, nothing leaves your computer.": "Полностью локальный загрузчик видео с открытым исходным кодом. Он находит медиа на YouTube, в потоках HLS и DASH, а также примерно на 1800 других сайтах, затем скачивает и преобразует их на вашем компьютере с помощью yt-dlp и ffmpeg. Серверы и внешние загрузки не используются.",
        "Node native host": "Локальный модуль Node",
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
