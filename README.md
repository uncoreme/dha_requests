# Easily way to get info by Discord HTTP API / ENG
version: 0.1

## How to start
1. For start you have to go to `config.py` file and set `api_version`, `redirect_uri`, `client_id`, and `client_secret` values.
2. Import `DHAUser` class and `get_token`, `get_user_by_code` functions from `src/main.py`.

## DHAUser class
DHAUser class takes one argument - `authorization_token`
DHAUser methods:
1. `DHAUser('user_token').user_info` - returns an array with user info.
2. `DHAUser('user_token').guilds` - returns an array with user guilds info.
3. `DHAUser('user_token').guilds_owner` - returns an array with user guild which owner is user.
4. `DHAUser('user_token').avatar` - returns a url of user avatar

## Get token function
`get_token('user_code')` - returns a user token.

## Get user by code
`get_user_by_code('user_code')` - returns a user by code.


# Быстрый способ получения информации с помощью Discord HTTP API / RU
версия: 0.1

## Как начать
1. Для начала вам необходимо перейти в файл `config.py` и установить значения для `api_version`, `redirect_uri`, `client_id`, и `client_secret`.
2. Затем импортируйте в нужный вам файл класс `DHAUser` и функции `get_token`, `get_user_by_code` из `src/main.py`.

## Класс DHAUser
Клас DHAUser принимает один аргумент - `authorization_token` (токен пользователя).
Методы класса DHAUser:
1. `DHAUser('user_token').user_info` - возрващает массив с информацией о пользователе.
2. `DHAUser('user_token').guilds` - возвращает массив с информацией о серверах, на которых присутствует пользователь.
3. `DHAUser('user_token').guilds_owner` - возвращает массив с информацией о серверах, чьим владельцем является пользователь.
4. `DHAUser('user_token').avatar` - возвращает ссылку на значок пользователя.

## Функция получения токена
`get_token('user_code')` - возвращает токен пользователя.

## Функция получения информации о пользователе по временному коду
`get_user_by_code` - возвращает информацию о пользователе по временному коду
