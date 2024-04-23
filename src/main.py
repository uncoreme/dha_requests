from config import redirect_uri, client_id, client_secret
from urls import discord_token_url, get_user_url, list_guilds_url
import requests


class DHAUser:
    def __init__(self, auth_token: str):
        self.user = requests.get(get_user_url, headers={'Authorization': f'Bearer {auth_token}'}).json()
        self.auth_token = auth_token

    async def user_info(self):
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
