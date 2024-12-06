import os.path
import requests
from pathlib import Path

day = 6
year = 2024
url = f'https://adventofcode.com/{year}/day/{day}/input'
cookie = '''
53616c7465645f5f2e3a177a6852cd9f7e9aac4f2a1b213c992b004abfe606eed7be028b60c3af39d8e34ff55c17813a12e45f573446ece958abd203ed35aac6j
'''
s = requests.Session()
s.cookies.set('session', cookie.strip())
r = s.get(url)

if r.status_code != 200:
    raise ConnectionRefusedError(r.text)

path = Path(f'0{day}')
if not os.path.exists(path):
    os.makedirs(path)

file = path / 'input'
with open(file, 'a+') as f:
    f.write(r.text)

files = ['input-training', f'puzzle0{day}.py']
for file in files:
    with open(path / file, 'w') as f:
        pass
