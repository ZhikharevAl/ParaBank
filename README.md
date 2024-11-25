# Проект автоматизированного тестирования Parabank

[![Ruff Linter](https://github.com/ZhikharevAl/ParaBank/actions/workflows/ruff_check.yml/badge.svg)](https://github.com/ZhikharevAl/ParaBank/actions/workflows/ruff_check.yml)
[![Playwright Tests](https://github.com/ZhikharevAl/ParaBank/actions/workflows/auto_tests.yml/badge.svg)](https://github.com/ZhikharevAl/ParaBank/actions/workflows/auto_tests.yml)

## Оглавление

- [Описание проекта](#описание-проекта)
- [Структура проекта](#структура-проекта)
- [Диаграмма состояний](#диаграмма-состояний)
- [Основные функции](#основные-функции)
- [Технологии и инструменты](#технологии-и-инструменты)
- [Настройка окружения](#настройка-окружения)
- [Запуск тестов](#запуск-тестов)
- [Структура отчетов](#структура-отчетов)
- [Особенности проекта](#особенности-проекта)

## Описание проекта

Данный проект представляет собой набор автоматизированных тестов для веб-приложения Parabank. Тесты покрывают основные функции, такие как регистрация пользователя, авторизация, просмотр счета и транзакций, а также другие действия, поддерживаемые сайтом.

## Структура проекта

```bash
parabank/
│
├── .github/               # Конфигурации GitHub Actions
│   ├── workflows/
│       ├── auto_tests.yml
│       ├── ruff_check.yml
├── config/                # Настройки конфигурации
├── data/                  # Модули для работы с тестовыми данными
│   ├── __init__.py
│   ├── user_data.py
├── docs/                  # Документация
├── pages/                 # Page Object модели для страниц сайта Parabank
│   ├── __init__.py
│   ├── base_page.py
│   ├── main_page.py
│   ├── overview_page.py
│   ├── register_page.py
├── tests/                 # Тестовые модули
│   ├── base/
│       ├── __init__.py
│       ├── base_test.py
│   ├── ui/
│       ├── __init__.py
│       ├── test_ui_elements.py
│       ├── test_login.py
│       ├── test_main_parabank.py
│       ├── test_register.py
├── .gitignore
├── conftest.py            # Конфигурация PyTest
├── pyproject.toml         # Конфигурация для Ruff
├── pytest.ini             # Конфигурация PyTest
├── README.md
├── requirements.txt       # Зависимости проекта
```

## [Диаграмма состояний](./attachment/Untitled%20diagram-2024-10-19-004955.svg)

![Full diagram](./attachment/Untitled%20diagram-2024-10-19-004955.svg)
![State diagram](./attachment/2024-10-19_05-02-30.png)

## Основные функции

- Регистрация нового пользователя с различными валидными и невалидными данными
- Авторизация зарегистрированного пользователя
- Просмотр баланса счета, истории транзакций и информации о пользователе
- Проверка корректности отображения элементов интерфейса

## Технологии и инструменты

- Python
- Pytest
- Allure для отчетов
- Playwright для взаимодействия с UI
- Page Object Model для структурирования тестов
- GitHub Actions для CI/CD

## Настройка окружения

1. Убедитесь, что установлен Python 3.10+
2. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ZhikharevAl/ParaBank.git
   cd ParaBank
   ```

3. Создайте виртуальное окружение и активируйте его:

   ```bash
   uv venv .venv
   source .venv/bin/activate  # Для Linux/Mac
   .venv\Scripts\activate    # Для Windows
   ```

4. Установите зависимости:

   ```bash
   uv pip install --upgrade -r requirements.txt
   ```

## Запуск тестов

Для запуска всех тестов:

```bash
pytest
```

Для запуска конкретного теста:

```bash
pytest tests/ui/test_ui_elements.py
```

Для создания Allure-отчета:

```bash
pytest --alluredir=./allure-results
allure serve ./allure-results
```

![Allure Report](/attachment/Screenshot%202024-11-23%20011852.png)

## Структура отчетов

Проект использует Allure для генерации отчетов. Каждый тест включает:

- Подробное описание шагов
- Скриншоты при сбоях
- Уровень приоритета теста

## Особенности проекта

- Использование Page Object Model для структурирования кода
- Параметризация тестов для охвата разных сценариев
- Поддержка CI/CD через GitHub Actions для автоматического запуска тестов
- Разделение тестов по категориям для лучшего покрытия
