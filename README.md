# Генератор опросных листов для размещения заказа с помощью Mistral AI на Django

Это веб-приложение на Django, которое помогает пользователям создавать опросные листы для заказа различных устройств. Пользователь вводит название изделия, а модель Mistral AI генерирует список характеристик, которые нужно указать для размещения заказа. Приложение также позволяет скачать сгенерированный опросный лист в виде документа Word (.docx).

## Особенности

- Отправка запросов в Mistral AI и получение списка характеристик для заказа устройства.
- Ответы форматируются в Markdown и отображаются на странице.
- Конвертация ответа в формате Markdown в документ Word и предоставление ссылки для скачивания.
- Удобный интерфейс с анимацией загрузки во время ожидания ответа.
- Возможность отправки запроса нажатием клавиши `Enter` для удобства.
- Адаптивная цветовая схема, которая подстраивается под тему операционной системы (дневной или ночной режим).
- Тематическое оформление с поддержкой дневного и ночного режима.
- Модальные окна для разделов "О проекте" и "Помощь".

## Требования

- Python 3.x
- Django 3.x или выше
- Пакет Python `mistralai`
- `python-docx` для генерации документов Word
- `beautifulsoup4` для парсинга HTML (если понадобится в будущем)
- API-ключ от Mistral AI

## Установка

1. Клонируйте репозиторий:

   ```sh
   git clone https://github.com/yourusername/mistral-django-app.git
   cd mistral-django-app
   ```

2. Создайте виртуальное окружение и активируйте его:

   ```sh
   python -m venv venv
   source venv/bin/activate  # В Windows используйте `venv\Scripts\activate`
   ```

3. Установите необходимые пакеты:

   ```sh
   pip install -r requirements.txt
   ```

4. Установите API-ключ Mistral в качестве переменной окружения:

   ```sh
   export MISTRAL_API_KEY='your_api_key_here'  # В Windows используйте `set MISTRAL_API_KEY=your_api_key_here`
   ```

5. Запустите сервер разработки Django:

   ```sh
   python manage.py runserver
   ```

6. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/` для доступа к приложению.

## Использование

- Введите название изделия в текстовое поле и нажмите "Отправить" или `Enter`, чтобы отправить запрос.
- Во время ожидания ответа от Mistral AI будет отображаться анимация загрузки.
- После получения ответа он будет отображен на странице, и появится кнопка "Скачать файл Word" для загрузки ответа в виде документа Word.

## Структура проекта

- `views.py`: Содержит Django views для обработки пользовательских запросов и взаимодействия с Mistral AI.
- `urls.py`: Определяет маршруты URL для приложения.
- `index.html`: Основной HTML-шаблон для пользовательского интерфейса.
- `static/`: Директория для хранения статических файлов (например, CSS, JavaScript).

## Основные особенности кода

1. **Отправка запросов в Mistral**

   - Представление `home()` обрабатывает ввод пользователя и отправляет его в Mistral API с помощью функции `get_mistral_response()`.

2. **Конвертация Markdown в Word**

   - Функция `markdown_to_word()` конвертирует ответ из Markdown в формат документа Word.
   - Обрабатывает заголовки, жирный текст, курсив, подчеркивание, цитаты и списки.
   - Документ Word затем генерируется и скачивается с помощью представления `download_docx()`.

3. **Улучшения пользовательского интерфейса**

   - Добавлен индикатор загрузки во время ожидания ответа.
   - Пользователи могут отправлять форму с помощью клавиши `Enter` для удобства.
   - Тематическое оформление с поддержкой дневного и ночного режима, адаптирующееся к системным настройкам.
   - Модальные окна для разделов "О проекте" и "Помощь" для улучшения взаимодействия с пользователем.

## Примеры запросов

- "Определи параметры, которые нужно указать при заказе холодильника."
- "Составь список характеристик для заказа 3D принтера."

## Лицензия

Этот проект лицензирован по лицензии MIT. Подробнее см. в файле `LICENSE`.

## Вклад в проект

Если у вас есть предложения или улучшения, не стесняйтесь отправлять issues или pull requests!

## Благодарности

- [Mistral AI](https://www.mistral.ai/) за предоставление языковой модели.
- [Django](https://www.djangoproject.com/) за веб-фреймворк.

