import json
import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}

query = input("Enter a search query: ")

expanded_term_suffixes = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
expanded_term_prefixes = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

url = f"https://www.fiverr.com/search/layout/omnibox?callback=autocompleteCallback&from_medusa_header=true&locale=en-US&pro_only=false&query={query}"

response = requests.get(url, headers=headers)

json_data = response.text.strip('autocompleteCallback(').strip(');')

data = json.loads(json_data)

suggestions = [suggestion['value'] for suggestion in data['suggestions']]
users_suggestions = [
    user_suggestion['value'] for user_suggestion in data['users_suggestions']
]

all_values = suggestions + users_suggestions

# Expand query suffix
for suffix in expanded_term_suffixes:
  expanded_query = query + suffix
  url = f"https://www.fiverr.com/search/layout/omnibox?callback=autocompleteCallback&from_medusa_header=true&locale=en-US&pro_only=false&query={expanded_query}"
  response = requests.get(url, headers=headers)
  json_data = response.text.strip('autocompleteCallback(').strip(');')
  data = json.loads(json_data)
  suggestions = [suggestion['value'] for suggestion in data['suggestions']]
  users_suggestions = [
      user_suggestion['value'] for user_suggestion in data['users_suggestions']
  ]
  all_values += suggestions + users_suggestions

# Expand query prefix
for prefix in expanded_term_prefixes:
  expanded_query = prefix + " " + query
  url = f"https://www.fiverr.com/search/layout/omnibox?callback=autocompleteCallback&from_medusa_header=true&locale=en-US&pro_only=false&query={expanded_query}"
  response = requests.get(url, headers=headers)
  json_data = response.text.strip('autocompleteCallback(').strip(');')
  data = json.loads(json_data)
  suggestions = [suggestion['value'] for suggestion in data['suggestions']]
  users_suggestions = [
      user_suggestion['value'] for user_suggestion in data['users_suggestions']
  ]
  all_values += suggestions + users_suggestions

print(all_values)
