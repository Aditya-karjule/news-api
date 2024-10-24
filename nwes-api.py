import requests

# API Endpoint
url = "https://newsdata.io/api/1/latest"

# Parameters for the API request (without sentiment filter)
params = {
    'apikey': 'pub_57142e2647bbf9af9ca85c949453359ff24de',  # Your API key
    'q': 'mental health'   # Search query
}

# Fetching the data
response = requests.get(url, params=params)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    news_data = response.json()

    # Checking if there are articles in the response
    if 'results' in news_data:
        articles = news_data['results']
        if articles:
            print("News on Mental Health:\n")
            for i, article in enumerate(articles, start=1):
                print(f"Article {i}:")
                print(f"Title: {article['title']}")
                print(f"Description: {article['description']}")
                print(f"Published: {article['pubDate']}")
                print(f"Link: {article['link']}")
                print("-" * 40)
        else:
            print("No articles found on mental health.")
    else:
        print("Error: Unexpected response format.")
else:
    print(f"Failed to fetch news. HTTP Status code: {response.status_code}")
