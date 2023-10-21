# YaTrack

![yatrack_workflow](https://github.com/YaTrack1/YaTrack-backend/actions/workflows/yatrack_workflow.yml/badge.svg)

## Описание проекта
Внутренний сервис найма.

> тут будет подробное описание

## Стек технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)


<details><summary><h2>Адрес проекта</h2></summary>

*(запускается локально)*

    http://127.0.0.1:8000/

**Адрес админки проекта**

    http://127.0.0.1:8000/admin/

**Документация**

    http://127.0.0.1:8000/swagger/

**Handlers**

```sh
тут ендпойнты
```
</details>

---

<details><summary><h2>Подготовка проекта к запуску</h2></summary>

### `3` и `4` пункты для локального запуска

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
</details>

---

<details><summary><h2>Для запуска в Docker-контейнере используйте инструкцию</h2></summary>

1. *Запустите сборку контейнеров*:

    ```sh
    docker compose -f infra/docker-compose.yaml up -d --build
    ```
2. *Для остановки контейнера*:
    ```sh
    docker compose -f infra/docker-compose.yaml down
    ```
</details>

---

<details><summary><h2>Для локального запуска используйте инструкцию</h2></summary>

1. *Выполните миграции*:

    * Инициализируйте миграции
        ```sh
        python src/backend/manage.py migrate
        ```

    * Создайте миграции
        ```sh
        python src/backend/manage.py makemigrations
        ```
        ```sh
        python src/backend/manage.py makemigrations
        ```

         ```sh
        python src/backend/manage.py makemigrations
         ```

         ```sh
        python src/backend/manage.py makemigrations
         ```

         ```sh
        python src/backend/manage.py makemigrations
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

**Проджект**:
- Ефремов Андрей (*Telegram*: [@AndreyEfremoff](https://t.me/AndreyEfremoff))

**Дизайнеры**:
- Федорова Анастасия (*Telegram*: [@cccrayfish](https://t.me/cccrayfish))
- Бурганова Алина (*Telegram*: [@alikaburganova](https://t.me/alikaburganova))
- Пока неизвестно (*Telegram*: [@](https://t.me/))

**Backend-разработчики**:
- Оскалов Лев (*Telegram*: [@oskalov](https://t.me/oskalov), **Github**: [Oskalovlev](https://github.com/Oskalovlev))
- Зюзин Андрей (*Telegram*: [@andrey_bpz](https://t.me/andrey_bpz), **Github**: [AndreyZyuzin](https://github.com/AndreyZyuzin))

**Frontend-разработчики**:
- Меначо-Пахес Юлия (*Telegram*: [@yuliamenachopages](https://t.me/yuliamenachopages), **Github**: [YuliaMenachoPages](https://github.com/https://github.com/YuliaMenachoPages))
- Дук Юлия (*Telegram*: [@YuliaD1002](https://t.me/YuliaD1002), **Github**: [YuliaDuk](https://github.com/YuliaDuk))
- Бартош Константин (*Telegram*: [@k_bartosh](https://t.me/k_bartosh), **Github**: [KonstaBartosh](https://github.com/KonstaBartosh))
