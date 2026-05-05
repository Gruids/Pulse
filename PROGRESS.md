# Прогресс разработки мессенджера Pulse

## Что сделано (04.05.2026)

### 1. Настройка окружения
- Установлен **Node.js v24.15.0** и **npm 11.12.1**
- Установлен **Git** (путь: `C:\Program Files\Git\bin\git.exe`)
- Создан репозиторий на GitHub: **Gruids/Pulse**
  - URL: https://github.com/Gruids/Pulse
  - Основная ветка: `main`
  - GitHub Pages: https://gruids.github.io/Pulse/

### 2. Firebase проект
- Проект: **Pulse** (ID: `pulse-f91f7`)
- Создана Web-аппликация, получен конфиг:
  ```javascript
  const firebaseConfig = {
    apiKey: "AIzaSyCyKQ5hrVFikcnL2Z_dnlHYt6G0ZgqZZoQ",
    authDomain: "pulse-f91f7.firebaseapp.com",
    databaseURL: "https://pulse-f91f7-default-rtdb.firebaseio.com",
    projectId: "pulse-f91f7",
    storageBucket: "pulse-f91f7.firebasestorage.app",
    messagingSenderId: "385531673294",
    appId: "1:385531673294:web:11ca96153d2b07ccb2ae9f",
    measurementId: "G-X61NV7817J"
  };
  ```
- Включена **Email/Password** аутентификация
- Создана **Realtime Database** с правилами:
  ```json
  {
    "rules": {
      "users": { ".read": "auth != null", ".write": "auth != null" },
      "messages": { ".read": "auth != null", ".write": "auth != null" }
    }
  }
  ```

### 3. Функционал мессенджера (файл `index.html`)
- Регистрация и вход через Email/Password
- Сохранение пользователей в базу данных (`users/{uid}`)
- Общий чат (сообщения в `messages/general`)
- Список пользователей (вкладка "Люди")
- Приватные чаты между пользователями (ID чата формируется из UID)
- Кнопка выхода
- Поиск по пользователям и чатам

### 4. Структура проекта
```
D:\месенджер\
├── index.html          # Основной файл (Firebase версия)
├── server.js           # Серверная часть (Node.js, НЕ используется сейчас)
├── server.py          # Альтернативный сервер (Python, НЕ используется)
├── package.json       # Зависимости (для будущего сервера)
├── README.md          # Описание проекта
├── PROGRESS.md        # Этот файл
├── docs\              # Документация
├── public\            # Статика (CSS, JS) — пока пусто
├── src\               # Исходный код (пока пусто)
└── templates\         # Шаблоны (старый код)
```

### 5. Доступ к файлам и ресурсам
- **Локальная папка**: `D:\месенджер\`
- **GitHub**: https://github.com/Gruids/Pulse
- **Сайт**: https://gruids.github.io/Pulse/
- **Firebase Console**: https://console.firebase.google.com/project/pulse-f91f7/overview
- **Firebase Realtime Database**: https://console.firebase.google.com/project/pulse-f91f7/database/pulse-f91f7-default-rtdb/data/
- **Firebase Authentication**: https://console.firebase.google.com/project/pulse-f91f7/authentication/users

### 6. Следующие шаги (план)
1. **Группы и каналы** — создание групповых чатов, администрирование.
2. **Музыкальные плейлисты** — добавление музыки из интернета, копирование из других платформ.
3. **Профиль пользователя** — аватар, статус, настройки.
4. **Мобильная версия (APK)** — конвертация в Android приложение.
5. **Публикация в магазинах** — Google Play, Apple Store (опционально).
6. **Платный хостинг** — для поддержки большого числа пользователей.

### 7. Важные команды (PowerShell)
```powershell
# Переменная для Git
$git = "C:\Program Files\Git\bin\git.exe"

# Проверка статуса
cd "D:\месенджер"; & $git status

# Добавление и коммит
& $git add .; & $git commit -m "Commit message"

# Отправка на GitHub
& $git push origin main
```

### 8. Текущий статус
- ✅ Регистрация и вход работают
- ✅ Пользователи сохраняются в Firebase
- ✅ Общий чат работает
- ✅ Поиск пользователей и приватные чаты работают
- ✅ Выход из аккаунта работает
- ⏳ GitHub Pages иногда требует очистки кеша (Ctrl+F5)

---
**Для продолжения работы в новой сессии:**
1. Открой папку `D:\месенджер\`
2. Проверь, что Git настроен: `& $git config --list`
3. Открой сайт https://gruids.github.io/Pulse/ с Ctrl+F5
4. Продолжай реализацию следующих шагов из раздела 6.
