import json

with open("news.json", 'r') as file:
    data = json.load(file)



for i in range(3):
    title = data['articles'][:3][i]['title']
    description = data['articles'][:3][i]['description']

    print(f'headline: {title}')
    print(f"brief: {description}\n\n")