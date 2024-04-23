# Easily way to get info by Discord HTTP API / ENG
version: 0.2

## How to start
1. For start you have to go to `config.py` file and set `api_version`, `redirect_uri`, `client_id`, and `client_secret` values.
2. Import `DHAUser`, `DMAGuild` classes and `get_token`, `get_user_by_code` functions from `src/main.py`.

## DHAUser class
DHAUser class takes one argument - `authorization_token`.
DHAUser methods:
1. `DHAUser('user_token').info()` - returns an array with user info.
2. `DHAUser('user_token').guilds()` - returns an array with user guilds info.
3. `DHAUser('user_token').guilds_owner()` - returns an array with user guild which owner is user.
4. `DHAUser('user_token').avatar()` - returns a url of user avatar.
5. `DHAUser('user_token').name()` - returns a user name. Method `name` take one option argument - `select` (default='u'). Argument may be 'u' (username) or 'g' (global_name).

## DHAGuild class
DHAGuild class takes two arguments - `guild_id` and `bot_token`.
DHAGuild methods:
1. `DHAGuild('guild_id', 'bot_token').info()` - returns an array with information about guild.
2. `DHAGuild('guild_id', 'bot_token').icon()` - returns an url of guild icon.
3. `DHAGuild('guild_id', 'bot_token').name()` - returns a name of guild.

## Get token function
`get_token('user_code')` - returns a user token.

## Get user by code
`get_user_by_code('user_code')` - returns a user by code.


# Быстрый способ получения информации с помощью Discord HTTP API / RU
версия: 0.2

## Как начать
1. Для начала вам необходимо перейти в файл `config.py` и установить значения для `api_version`, `redirect_uri`, `client_id`, и `client_secret`.
2. Затем импортируйте в нужный вам файл классы `DHAUser`, `DHAGuild` и функции `get_token`, `get_user_by_code` из `src/main.py`.

## Класс DHAUser
Клас DHAUser принимает один аргумент - `authorization_token` (токен пользователя).
Методы класса DHAUser:
1. `DHAUser('user_token').info()` - возрващает массив с информацией о пользователе.
2. `DHAUser('user_token').guilds()` - возвращает массив с информацией о серверах, на которых присутствует пользователь.
3. `DHAUser('user_token').guilds_owner()` - возвращает массив с информацией о серверах, чьим владельцем является пользователь.
4. `DHAUser('user_token').avatar()` - возвращает ссылку на значок пользователя.
5. `DHAUser('user_token').name()` - возвращает имя пользователя. Метод `name` принимает необязательный аргумент - `select` (по умолчанию 'u'). Аргумент может быть равен 'u' (username) или 'g' (global_name).

## Класс DHAGuild
Класс DHAGuild принимает два аргумента - `guild_id` и `bot_token`.
Методы класса DHAGuild:
1. `DHAGuild('guild_id', 'bot_token').info()` - возвращает массив с информацией о сервере.
2. `DHAGuild('guild_id', 'bot_token').icon()` - возвращает ссылку на значок сервера.
3. `DHAGuild('guild_id', 'bot_token').name()` - возвращает название сервера

## Функция получения токена
`get_token('user_code')` - возвращает токен пользователя.

## Функция получения информации о пользователе по временному коду
`get_user_by_code('user_code')` - возвращает информацию о пользователе по временному коду
