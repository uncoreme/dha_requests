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

```py
guild = DHAGuild('guild_id', 'bot_token')
```

DHAGuild methods:
```py
guild.info()
>>> {
	"id": "<string>",
	"name": "<string>",
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
	"owner_id": "<string>",
	"region": "<string>",
	"afk_timeout": {
		"title": "ONE_MINUTE",
		"const": 60
	},
	"system_channel_flags": "<integer>",
	"widget_enabled": "<boolean>",
	"verification_level": {
		"title": "NONE",
		"description": "unrestricted",
		"const": 0
	},
	"roles": [
		{
			"id": "<string>",
			"name": "<string>",
			"permissions": "<string>",
			"position": "<integer>",
			"color": "<integer>",
			"hoist": "<boolean>",
			"managed": "<boolean>",
			"mentionable": "<boolean>",
			"description": "<string,null>",
			"icon": "<string,null>",
			"unicode_emoji": "<string,null>",
			"tags": "<null>"
		},
		{
			"id": "<string>",
			"name": "<string>",
			"permissions": "<string>",
			"position": "<integer>",
			"color": "<integer>",
			"hoist": "<boolean>",
			"managed": "<boolean>",
			"mentionable": "<boolean>",
			"description": "<string,null>",
			"icon": "<string,null>",
			"unicode_emoji": "<string,null>",
			"tags": "<null>"
		}
	],
	"default_message_notifications": {
		"title": "ALL_MESSAGES",
		"description": "members will receive notifications for all messages by default",
		"const": 0
	},
	"mfa_level": {
		"title": "NONE",
		"description": "Guild has no MFA/2FA requirement for moderation actions",
		"const": 0
	},
	"explicit_content_filter": {
		"title": "DISABLED",
		"description": "media content will not be scanned",
		"const": 0
	},
	"premium_tier": {
		"title": "NONE",
		"description": "Guild has not unlocked any Server Boost perks",
		"const": 0
	},
	"premium_subscription_count": "<integer>",
	"preferred_locale": {
		"title": "ar",
		"description": "The ar locale",
		"const": "ar"
	},
	"premium_progress_bar_enabled": "<boolean>",
	"nsfw": "<boolean>",
	"nsfw_level": {
		"title": "DEFAULT",
		"const": 0
	},
	"emojis": [
		{
			"id": "<string>",
			"name": "<string>",
			"roles": [
				"<string>",
				"<string>"
			],
			"require_colons": "<boolean>",
			"managed": "<boolean>",
			"animated": "<boolean>",
			"available": "<boolean>",
			"user": "<null>"
		},
		{
			"id": "<string>",
			"name": "<string>",
			"roles": [
				"<string>",
				"<string>"
			],
			"require_colons": "<boolean>",
			"managed": "<boolean>",
			"animated": "<boolean>",
			"available": "<boolean>",
			"user": "<null>"
		}
	],
	"stickers": [
		{
			"id": "<string>",
			"name": "<string>",
			"tags": "<string>",
			"type": 2,
			"available": "<boolean>",
			"guild_id": "<string>",
			"format_type": "<null>",
			"description": "<string,null>",
			"user": "<null>"
		},
		{
			"id": "<string>",
			"name": "<string>",
			"tags": "<string>",
			"type": 2,
			"available": "<boolean>",
			"guild_id": "<string>",
			"format_type": "<null>",
			"description": "<string,null>",
			"user": "<null>"
		}
	],
	"icon": "<string,null>",
	"description": "<string,null>",
	"home_header": "<string,null>",
	"splash": "<string,null>",
	"discovery_splash": "<string,null>",
	"banner": "<string,null>",
	"application_id": "<string,null>",
	"afk_channel_id": "<string,null>",
	"system_channel_id": "<string,null>",
	"widget_channel_id": "<string,null>",
	"max_presences": "<integer,null>",
	"max_members": "<integer,null>",
	"max_stage_video_channel_users": "<integer,null>",
	"max_video_channel_users": "<integer,null>",
	"vanity_url_code": "<string,null>",
	"rules_channel_id": "<string,null>",
	"safety_alerts_channel_id": "<string,null>",
	"public_updates_channel_id": "<string,null>",
	"approximate_member_count": "<integer,null>",
	"approximate_presence_count": "<integer,null>"
}


guild.icon()
>>> 'https://cdn.discordapp.com/icons/<guild_id>/<guild_icon>.png'


guild.name()
>>> '<guild_name>'


guild.list_channels()
>>> [{
  'id': '<channel_id>',
  'type': 4,
  'flags': 0,
  'guild_id': '<guild_id>',
  'name': '<channel_id>',
  'parent_id': None,
  'position': 0,
  'permission_overwrites': []
}]


guild.channel('channel_id')
>>> {
  'id': '<channel_id>',
  'type': 0,
  'last_message_id': '<message_id>',
  'flags': 0,
  'guild_id': '<guild_id>',
  'name': '<channel_name>',
  'parent_id': '<channel_id>',
  'rate_limit_per_user': 0,
  'topic': None,
  'position': 0,
  'permission_overwrites': [],
  'nsfw': False,
  'icon_emoji': {
    'id': None,
    'name': '👋'
  },
  'theme_color': None
}


guild.list_members()  # limit (default 5) can take int value from 1 to 10
>>> [{
  'avatar': None,
  'communication_disabled_until': None,
  'flags': 0,
  'joined_at': '2024-04-11T18:08:58.641000+00:00',
  'nick': None,
  'pending': False,
  'premium_since': None,
  'roles': ['<role_id>'],
  'unusual_dm_activity_until': None,
  'user': {
    'id': '451379187031343104',
    'username': 'LunaBot 🌙',
    'avatar': '71be5dabc3f593d47adbdc523b451118',
    'discriminator': '9997',
    'public_flags': 65536,
    'flags': 65536,
    'bot': True,
    'banner': None,
    'accent_color': None,
    'global_name': None,
    'avatar_decoration_data': None,
    'banner_color': None,
    'clan': None
  },
  'mute': False,
  'deaf': False
}]


guild.list_roles()
>>> [{
  'id': '<role_id>',
  'name': '@everyone',
  'description': None,
  'permissions': '<permissions>',
  'position': 0,
  'color': 0,
  'hoist': False,
  'managed': False,
  'mentionable': False,
  'icon': None,
  'unicode_emoji': None,
  'flags': 0
},]
```

## Get token function
```py
get_token('user_code')
>>> '<auth_token>'
```

## Get user by code
```py
get_user_by_code('user_code')
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
```


# Быстрый способ получения информации с помощью Discord HTTP API / RU
версия: 0.2 (устаревшая, новая на английском языке)

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
