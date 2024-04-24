# Easily way to get info by Discord HTTP API / ENG
version: 0.3

## How to start
1. For start you have to go to `config.py` file and set `api_version`, `redirect_uri`, `client_id`, and `client_secret` values.
2. Import `DHAUser`, `DHAMember`, `DHAGuild` classes and `get_token`, `get_user_by_code` functions from `src/main.py`.

## DHAUser class
DHAUser class takes one argument - `authorization_token`.

```py
user = DHAUser('user_token')
```

DHAUser methods:
```py
user.info()
>>> {
  'id': '<user_id>',
  'username': '<username>',
  'avatar': '<avatar>',
  'discriminator': '0',
  'public_flags': 0,
  'flags': 0,
  'banner': None,
  'accent_color': <accent_color>,
  'global_name': '<user_global_name>',
  'avatar_decoration_data': None,
  'banner_color': '<color>',
  'clan': None,
  'mfa_enabled': False,
  'locale': 'ru',
  'premium_type': 0
}


user.quick_info()
>>> {
  'id': '<user_id>',
  'username': '<username>',
  'global_name': '<user_global_name>',
  'avatar': 'https://cdn.discordapp.com/avatars/<user_id>/<user_avatar>.png'
}


user.guilds()
>>> [{
  "id": "<string>",
  "name": "<string>",
  "owner": "<boolean>",
  "permissions": "<string>",
  "features": [
    {
      "title": "ANIMATED_BANNER",
      "description": "guild has access to set an animated guild banner image",
      "const": "ANIMATED_BANNER"
    },
    {
      "title": "ANIMATED_BANNER",
      "description": "guild has access to set an animated guild banner image",
      "const": "ANIMATED_BANNER"
    }
  ],
  "icon": "<string,null>",
  "approximate_member_count": "<integer,null>",
  "approximate_presence_count": "<integer,null>"
},]


user.guilds_owner()
>>> [{
  'id': '<guild_id>',
  'name': '<guild_name>',
  'icon': None,
  'owner': True,
  'permissions': '1125899906842623',
  'features': []},
]


user.avatar()
>>> 'https://cdn.discordapp.com/avatars/<user_id>/<user_avatar>.png'


user.name()  # default 'u'
>>> '<username>'

user.name('g')
>>> '<user_global_name>'
```

## DHAMember class
DHAMember class takes three arguments - `bot_token`, `member_id` and `guild_id`.

```py
member = DHAMember('bot_token', 'member_id', 'guild_id')
```

DHAMember methods:
```py
member.info()
>>> {
  "flags": "<integer>",
  "joined_at": "<dateTime>",
  "pending": "<boolean>",
  "roles": [
    "<string>",
    "<string>"
  ],
  "user": {
    "id": "<string>",
    "username": "<string>",
    "discriminator": "<string>",
    "public_flags": "<integer>",
    "flags": "<integer>",
    "avatar": "<string,null>",
    "bot": "<boolean,null>",
    "system": "<boolean,null>",
    "banner": "<string,null>",
    "accent_color": "<integer,null>"
  },
  "mute": "<boolean>",
  "deaf": "<boolean>",
  "avatar": "<string,null>",
  "communication_disabled_until": "<string,null-date-time>",
  "nick": "<string,null>",
  "premium_since": "<string,null-date-time>"
}


member.quick_info()
>>> {
  'id': '<member_id>',
  'username': '<username>',
  'global_name': '<member_global_name>',
  'avatar': 'https://cdn.discordapp.com/avatars/<member_id>/<member_avatar>.png'
}


member.user()
>>> {
  'id': '<user_id>',
  'username': '<username>',
  'avatar': '<avatar>',
  'discriminator': '0',
  'public_flags': 0,
  'flags': 0,
  'banner': None,
  'accent_color': <accent_color>,
  'global_name': '<user_global_name>',
  'avatar_decoration_data': None,
  'banner_color': '<color>',
  'clan': None,
  'mfa_enabled': False,
  'locale': 'ru',
  'premium_type': 0
}


member.avatar()
>>> 'https://cdn.discordapp.com/avatars/<member_id>/<member_avatar>.png'


member.name()  # default 'u'
>>> '<username>'

member.name('g')
>>> '<member_global_name>'


member.roles()
>>> ['<role_id_1>', '<role_id_2>'...]
```


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
