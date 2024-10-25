import requests
from django.shortcuts import render

def fetch_news(query, api_key):
    """
    Fetches news articles based on the query from the NewsData.io API.
    
    :param query: The search term for the news (e.g., "mental health")
    :param api_key: Your NewsData.io API key
    :return: A list of articles or an error message
    """
    url = "https://newsdata.io/api/1/latest"
    params = {
        'apikey': api_key,
        'q': query
    }

    # Fetching the data from the API
    response = requests.get(url, params=params)

    # Handling different response scenarios
    if response.status_code == 200:
        news_data = response.json()
        if 'results' in news_data:
            articles = news_data['results']
            return articles if articles else "No articles found for the given query."
        else:
            return "Error: Unexpected response format."
    elif response.status_code == 403:
        return "Error: Access Forbidden. Check your API key or permissions."
    else:
        return f"Failed to fetch news. HTTP Status code: {response.status_code}"


def news_view(request):
    """
    Django view to display news articles related to 'mental health'.
    """
    # Your NewsData.io API key
    api_key = 'pub_57142e2647bbf9af9ca85c949453359ff24de'  # <-- Ensure this is passed here
    
    # Call the function to fetch news with the query and the API key
    news_articles = fetch_news('mental health', api_key)
    
    # If it's an error message, pass it as context; otherwise, pass the news data
    if isinstance(news_articles, str):
        context = {'error': news_articles}
    else:
        context = {'articles': news_articles}
    
    # Render the news in a template
    return render(request, 'index.html', context)
