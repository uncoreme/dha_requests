from .config import api_version

base_url = f'https://discord.com/api/v{api_version}/'

discord_token_url = 'https://discord.com/api/oauth2/token'
get_user_url = f'{base_url}users/@me'
list_guilds_url = f'{base_url}users/@me/guilds?with_count=true'


def guild_url(guild_id):
    return f'https://discord.com/api/v{api_version}/guilds/{guild_id}?with_counts=true'


def list_channels(guild_id):
    return f'https://discord.com/api/v10/guilds/{guild_id}/channels'


def get_channel(channel_id):
    return f'https://discord.com/api/v10/channels/{channel_id}'


def get_guild_member(guild_id, member_id):
    return f'https://discord.com/api/v10/guilds/{guild_id}/members/{member_id}'


def list_guild_members(guild_id, limit):
    if limit > 10:
        limit = 10
    return f'https://discord.com/api/v10/guilds/{guild_id}/members?limit={limit}'


def list_guild_roles(guild_id):
    return f'https://discord.com/api/v10/guilds/{guild_id}/roles'
