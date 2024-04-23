from .config import api_version

base_url = f'https://discord.com/api/v{api_version}/'

discord_token_url = 'https://discord.com/api/oauth2/token'
get_user_url = f'{base_url}users/@me'
list_guilds_url = f'{base_url}users/@me/guilds?with_count=true'


def guild_url(guild_id):
    return f'https://discord.com/api/v{api_version}/guilds/{guild_id}?with_counts=true'
