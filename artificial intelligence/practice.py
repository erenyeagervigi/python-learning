smtg = {'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 18.65, 'met': 9.8, 'nf_calories': 213.23, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}, {'tag_id': 100, 'user_input': 'walked', 'duration_min': 37.28, 'met': 3.5, 'nf_calories': 152.23, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 17190, 'name': 'walking', 'description': None, 'benefits': None}]}
data = smtg["exercises"]
print(data)
for workout in data:
    print(workout['name'])
