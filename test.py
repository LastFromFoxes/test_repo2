import random
import subprocess

for i in range(1):
    rand_num = random.randint(1, 1000000)
    with open('test1.py', 'w', encoding='utf-8') as f:
        f.write(f'a = {rand_num}\n')
    subprocess.run(['git', 'add', 'test1.py'])
    subprocess.run(['git', 'commit', '-m', f'Добавлено рандомное число {rand_num} на шаге {i}'])
    subprocess.run(['git', 'push'])
