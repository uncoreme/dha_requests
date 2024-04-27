from .config import redirect_uri, client_id, client_secret
from .urls import (discord_token_url, get_user_url, list_guilds_url, guild_url, list_channels, get_channel,
                   get_guild_member, list_guild_members, list_guild_roles)
import requests
from typing import Dict, List


class DHAUser:
    def __init__(self, auth_token: str):
        self.auth_token = auth_token

    def info(self) -> Dict:
        return requests.get(get_user_url, headers={'Authorization': f'Bearer {self.auth_token}'}).json()

    def guilds(self) -> Dict:
        return requests.get(list_guilds_url, headers={'Authorization': f'Bearer {self.auth_token}'}).json()

    def guilds_owner(self) -> List:
        guilds_list = []
        for item in requests.get(list_guilds_url, headers={'Authorization': f'Bearer {self.auth_token}'}).json():
            if item['owner']:
                guilds_list.append(item)
        return guilds_list

    def avatar(self) -> str:
        return f'https://cdn.discordapp.com/avatars/{self.info()['id']}/{self.info()['avatar']}.png'

    def name(self, select='u') -> str:
        if select == 'u':
            return f'{self.info()['username']}'
        elif select == 'g':
            return f'{self.info()['global_name']}'

    def quick_info(self) -> Dict:
        user = self.info()
        data = {
            'id': user['id'],
            'username': user['username'],
            'global_name': user['global_name'],
            'avatar': f'https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.png',
        }
        return data


class DHAMember:
    def __init__(self, bot_token: str, member_id: int, guild_id: int):
        self.bot_token = bot_token
        self.member_id = member_id
        self.guild_id = guild_id

    def info(self) -> Dict:
        return requests.get(get_guild_member(self.guild_id, self.member_id),
                            headers={'Authorization': f'Bot {self.bot_token}'}).json()

    def user(self) -> Dict:
        return self.info()['user']

    def avatar(self) -> str:
        user = self.info()['user']
        return f'https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.png'

    def name(self, select='u') -> str:
        if select == 'u':
            return f'{self.info()['user']['username']}'
        elif select == 'g':
            return f'{self.info()['user']['global_name']}'

    def quick_info(self) -> Dict:
        user = self.user()
        data = {
            'id': user['id'],
            'username': user['username'],
            'global_name': user['global_name'],
            'avatar': f'https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.png',
        }
        return data

    def roles(self) -> Dict:
        return self.info()['roles']


class DHAGuild:
    def __init__(self, guild_id: int, bot_token: str):
        self.guild_id = guild_id
        self.bot_token = bot_token

    def info(self) -> Dict:
        return requests.get(guild_url(self.guild_id), headers={'Authorization': f'Bot {self.bot_token}'}).json()

    def icon(self) -> str:
        return f'https://cdn.discordapp.com/icons/{self.guild_id}/{self.info()['icon']}.png'

    def name(self) -> str:
        return f'{self.info()["name"]}'

    def list_channels(self) -> Dict:
        return requests.get(list_channels(self.guild_id), headers={'Authorization': f'Bot {self.bot_token}'}).json()

    def channel(self, channel_id: str) -> Dict:
        return requests.get(get_channel(channel_id), headers={'Authorization': f'Bot {self.bot_token}'}).json()

    def list_members(self, limit: int = 5) -> Dict:
        return requests.get(list_guild_members(self.guild_id, limit),
                            headers={'Authorization': f'Bot {self.bot_token}'}).json()

    def list_roles(self) -> Dict:
        return requests.get(list_guild_roles(self.guild_id), headers={'Authorization': f'Bot {self.bot_token}'}).json()

    def members_count(self) -> str:
        return self.info()['approximate_member_count']

    def quick_info(self) -> Dict:
        data = self.info()
        response = {
            'id': data['id'],
            'name': data['name'],
            'owner_id': data['owner_id'],
            'region': data['region'],
            'nsfw': data['nsfw'],
            'avatar': f'https://cdn.discordapp.com/icons/{self.guild_id}/{data['icon']}.png',
            'members_count': data['approximate_member_count']
        }
        return response


def get_token(code: str) -> str:
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


def get_user_by_code(auth_code: str) -> Dict:
    auth_token = get_token(auth_code)
    return requests.get(get_user_url, headers={'Authorization': f'Bearer {auth_token}'}).json()
