from config import api_version

base_url = f'https://discord.com/api/v{api_version}/'

discord_token_url = f'{base_url}token'
get_user_url = f'{base_url}users/@me'
list_guilds_url = f'{base_url}users/@me/guilds?with_count=true'