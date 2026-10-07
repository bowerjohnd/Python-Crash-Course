import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

print("=" * 50)
if r.status_code != 200:
    print(r)
    exit()
else:
    print(f"Status code: {r.status_code}")

print("=" * 50)

# Convert the response object to a dictionary.
response_dict = r.json()

# Process results.
print(response_dict.keys())
print("=" * 50)
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for index, repo_dict in enumerate(repo_dicts):
    print(f"\n{index}\tName: {repo_dict['name']}")
    print(f"\tOwner: {repo_dict['owner']['login']}")
    print(f"\tStars: {repo_dict['stargazers_count']}")
    print(f"\tRepository: {repo_dict['html_url']}")
    print(f"\tDescription: {repo_dict['description']}")
