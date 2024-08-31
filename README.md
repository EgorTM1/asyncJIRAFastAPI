### Запуск приложения
1. Создать виртуальное окружение и установить зависимости командой `pip install -r requirements.txt`
2. Вызвать в терминале `python -m src.main`

### Настройка Alembic для асинхронного драйвера
1. Находясь в корневой директории, запустить  
`alembic init -t async migrations`
2. Перенести папку `migrations` внутрь папки `src`.
3. Заменить `prepend_sys_path` на `. src` и `script_location` на `src/migrations` внутри `alembic.ini`


### Документация к API
![Alt text](docs/github/openapi.png)
