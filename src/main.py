from .config import redirect_uri, client_id, client_secret
from .urls import discord_token_url, get_user_url, list_guilds_url, guild_url
import requests


class DHAUser:
    def __init__(self, auth_token: str):
        self.user = requests.get(get_user_url, headers={'Authorization': f'Bearer {auth_token}'}).json()
        self.auth_token = auth_token

    async def info(self):
        return self.user

    async def guilds(self):
        return requests.get(list_guilds_url, headers={'Authorization': f'Bearer {self.auth_token}'}).json()

    async def guilds_owner(self):
        guilds_list = []
        for item in requests.get(list_guilds_url, headers={'Authorization': f'Bearer {self.auth_token}'}).json():
            if item['owner']:
                guilds_list.append(item)
        return guilds_list

    async def avatar(self):
        return f'https://cdn.discordapp.com/avatars/{self.user['id']}/{self.user['avatar']}.png'

    async def name(self, select='u'):
        if select == 'u':
            return f'{self.user['username']}'
        elif select == 'g':
            return f'{self.user['global_name']}'


class DHAGuild:
    def __init__(self, guild_id: str, bot_token: str):
        self.guild_id = guild_id
        self.guild = requests.get(guild_url(guild_id), headers={'Authorization': f'Bot {bot_token}'}).json()

    async def info(self):
        return self.guild

    async def icon(self):
        return f'https://cdn.discordapp.com/icons/{self.guild_id}/{self.guild['icon']}.png'

    async def name(self):
        return f'{self.guild["name"]}'


async def get_token(code: str) -> str:
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    return requests.post(discord_token_url, data=payload, headers=headers,
                         auth=(client_id, client_secret)).json()['access_token']


async def get_user_by_code(auth_code: str):
    auth_token = await get_token(auth_code)
    return requests.get(get_user_url, headers={'Authorization': f'Bearer {auth_token}'}).json()
