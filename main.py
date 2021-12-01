#!/usr/bin/env python3
import requests, json, re
import webbrowser
api_url = f'https://animepahe.com/api'

def select_anime(querry):
    params = {
        'm': 'search',
        'l': '8',
        'q': f'{querry}',
    }
    resp = requests.get(api_url, params=params).json()

    for i in range(resp['total']):
        print(i+1)
        for key in resp['data'][i].keys():
            print(f"{key}: {resp['data'][i][key]}")
            print('')
    choice = int(input('Enter your selection: '))-1
    return {
        'id': resp['data'][choice]['id'],
        'session': resp['data'][choice]['session'],
        }

def select_episode(anime):
    params = {
        'm': 'release',
        'id': anime['id'],
        'sort': 'desc',
        'page': '1',
        }
    resp = requests.get(api_url, params=params).json()

    choice = input(f"Enter an episode between [1 & {resp['total']}]: ")
    return {
        'anime_id': anime['id'],
        'anime_session': anime['session'],
        'id' : resp['data'][0]['id'],
        'session': resp['data'][0]['session'],
    }

def get_link(episode):
    params = {
        'm': 'links',
        'id': episode['anime_id'],
        'session': episode['session'],
        'p': 'kwik',
    }
    resp = requests.get(api_url, params).json()

    return resp['data'][-1]['1080']['kwik_adfly']

def main():
    anime = select_anime(input('Search for anime: '))
    episode = select_episode(anime)
    link = get_link(episode)
    webbrowser.open(link)
    print(link)
    return link

if __name__ == '__main__':
    main()

# def get_token(link):
#     headers = {
#         'Referer': link,
#     }
#     resp = requests.get(link, headers=headers).text

#     params = {

#     }
#     token = re.search(r'name\|_token\|value\|(\w+)\|submit', resp).group(1)

#     return token
