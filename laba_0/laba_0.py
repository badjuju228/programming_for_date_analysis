import pandas as pd

music = [
    ['mnogoznaal', 'Много Лиц'],
    ['loqiemean', 'Одинокий канибал'],
    ['nirvana', 'Smells Like teen spirit'],
    ['mnogoznaal', 'Гостиница Космос'],
    ['Грязь', 'Ау']
]

entries = ['artist', 'track']

playlist = pd.DataFrame(data=music, columns=entries)

print(playlist)