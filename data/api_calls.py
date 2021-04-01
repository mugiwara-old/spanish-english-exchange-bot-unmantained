import os
import requests
import json

class API_CALLS:

  def get_unsplash_image_url():
    unsplash_params = {
      'count': 1, 
      'client_id': os.getenv('UNSPLASH_TOKEN')
    }
    
    response = requests.get('https://api.unsplash.com/photos/random', params=unsplash_params)
    
    json_data = json.loads(response.text)
    
    image_url = json_data[0]["urls"]['full']
    
    return(image_url)

  def get_newsapi_news(lang):
    if lang == "spanish":
      newsapi_params = {
        'language':'es', 
        'pageSize': 1, 
        'category':'technology',
        'apiKey':os.getenv('NEWSAPI_TOKEN')
      }

      res = requests.get('https://newsapi.org/v2/top-headlines',params=newsapi_params)

      json_data = json.loads(res.text)

      spanish_text = json_data["articles"][0]

      return(spanish_text)

    elif lang == "english":
      newsapi_params = {
        'country':'us', 
        'pageSize': 1, 
        'category':'entertainment',
        'apiKey':os.getenv('NEWSAPI_TOKEN')
      }

      res = requests.get('https://newsapi.org/v2/top-headlines',params=newsapi_params)

      json_data = json.loads(res.text)

      english_text = json_data["articles"][0]
      
      return(english_text)