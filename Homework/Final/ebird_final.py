from ebird.api import get_observations

api_token = 'vev5bd57v7ou.'

obs = get_observations(api_token, 'US', back=10)

print(obs)
