# YaTrack

![YaTrack Workflow](https://github.com/YaTrack1/YaTrack-backend/actions/workflows/main-push_workflow.yml/badge.svg)

## Описание проекта
### Внутренний сервис найма студентов.

#### Предоставляет возможность партнерам работать с базой заинтересованных кандидатов и отбирать не только текущих студентов, но и выпускников уровня `middle` и выше.

Сервис с открытой базой из кандидатов для трудоустройства в компании-портнеры Практикума.
Интерфейс помогает более качественно презентовать и рекомендовать студентов Практикума на вакантные, партнерские позиции в IT-компании России, а так же помочь быстрее отбирать кандидатов на специфические позиции с дополнительными требованиями.

## Стек технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)

<details><summary><h2>Адрес проекта</h2></summary>

*(запускается локально)*

    http://127.0.0.1:8000/

*(запуск на сервере)*

    https://51.250.74.42:8000/

> /admin/ # Адрес админки проекта

> /swagger/ # Документация

**Handlers**

```sh
auth/users/  # регистрация пользователя
auth/token/login/  # вход из системы
auth/token/logout/  # выход в систему

api/employer/  # Профиль нанимателя(HR)
api/employer/vacancy/  # Описание вакансии
api/employer/create/step-1/ # Первый шаг создания вакансии
api/employer/create/step-2/ # Второй шаг создания вакансии

api/resume/  # Резюме кандидата

api/tracker/  # Трекер вакансий
api/tracker/<vacancy_id>/comparison/  # Сравнение подходящих вакансий
api/tracker/<vacancy_id>/favorite/  # Избранные вакансии кандидатов
api/tracker/<vacancy_id>/invitation/  # Приглашенные кандидаты
```
</details>

---

<details><summary><h2>Подготовка проекта к запуску</h2></summary>

### `3` и `4` пункты для локального запуска. `5` пункт для ведения разработки

1. *Склонируйте репозиторий и перейдите в него*:

    ```sh
    git clone https://github.com/YaTrack1/YaTrack-backend.git
    ```
    ```sh
    cd YaTrack-backend/
    ```
---
2. *Для работы с PostgreSQL*:

    * Создайте в директории `infra/` файл `.env` командой:

        ```sh
        touch infra/.env
        ```
        > Заполните переменные по примеру файла `.env.example`
---
3. *Создайте и активируйте виртуальное окружение*:

    ```sh
    python -m venv venv
    ```
    - Если у вас Linux/macOS
        ```sh
        source venv/bin/activate
        ```

    - Если у вас windows
        ```sh
        source venv/scripts/activate
        ```
---
4. *Обновите pip и установите зависимости*:

    ```sh
    python -m pip install --upgrade pip
    ```
    ```sh
    pip install -r src/backend/requirements.txt
    ```

5. *Установите pre-commit*:
   ```sh
   pre-commit install
   ```
</details>

---

<details><summary><h2>Для запуска в Docker-контейнере используйте инструкцию</h2></summary>

1. *Запустите сборку контейнеров*:

    ```sh
    docker compose -f infra/docker-compose.yaml up -d --build
    ```
2. *Для остановки контейнеров*:
    ```sh
    docker compose -f infra/docker-compose.yaml stop
    ```
3. *Для удаления контейнеров*:
    ```sh
    docker compose -f infra/docker-compose.yaml down (-v опционально, удалит связи)
    ```
</details>

---

<details><summary><h2>Для локального запуска используйте инструкцию</h2></summary>

1. *Выполните миграции*:

    * Инициализируйте миграции (опционально)
        ```sh
        python src/backend/manage.py migrate
        ```

    * Создайте миграции
        ```sh
        python src/backend/manage.py makemigrations user
        ```
        ```sh
        python src/backend/manage.py makemigrations tracker
        ```

    * Примените миграции
        ```sh
        python src/backend/manage.py migrate
        ```
---
2. *Создайте суперюзера*:

    ```sh
    python src/backend/manage.py createsuperuser
    ```

    > Для примера, данные суперюзера:

        username: admin
        mail: admin@admin.ru
        password: admin
        password (again): admin

    > При входе логин указывать с большой буквы `Admin`

---

3. *Соберите статику*:
    ```sh
    python src/backend/manage.py collectstatic --noinput
    ```
---
4. *Локальный запуск*:

    ```sh
    python src/backend/manage.py runserver
    ```
</details>

---

### Команда проекта

**Backend-разработчики**:
- Оскалов Лев (*Telegram*: [@oskalov](https://t.me/oskalov), **Github**: [Oskalovlev](https://github.com/Oskalovlev))
- Зюзин Андрей (*Telegram*: [@andrey_bpz](https://t.me/andrey_bpz), **Github**: [AndreyZyuzin](https://github.com/AndreyZyuzin))
