# Easily way to get info by Discord HTTP API
## How to start
1. For start you have to go to config file and set `api_version`, `redirect_uri`, `client_id`, and `client_secret` values.
2. Import `DHAUser` class and `get_token`, `get_user_by_code` functions from src/main.py.

## DHAUser class
DHAUser class takes one argument - `authorization_token`
DHAUser functions:
1. `DHAUser('user_token').user_info` - returns an array with user info.
2. `DHAUser('user_token').guilds` - returns an array with user guilds info.
3. `DHAUser('user_token').guilds_owner` - returns an array with user guild which owner is user.
4. `DHAUser('user_token').avatar` - returns a url of user avatar
