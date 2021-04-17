from decouple import config

API_KEY = config('API_KEY')
API_PRIVATE_KEY = config('API_PRIVATE_KEY')

print(API_KEY)
print(API_PRIVATE_KEY)
