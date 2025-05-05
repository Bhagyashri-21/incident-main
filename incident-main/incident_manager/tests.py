import requests

def test_google_geocoding_api(api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': '1600 Amphitheatre Parkway, Mountain View, CA', 'key': api_key}
    response = requests.get(url, params=params)
    return response

def test_google_places_api(api_key):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {'query': 'restaurants in New York', 'key': api_key}
    response = requests.get(url, params=params)
    return response

def test_google_calendar_api(api_key):
    url = "https://www.googleapis.com/calendar/v3/users/me/calendarList"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response

def test_youtube_data_api(api_key):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {'part': 'snippet', 'forUsername': 'GoogleDevelopers', 'key': api_key}
    response = requests.get(url, params=params)
    return response

def test_google_translation_api(api_key):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {'q': 'Hello, world!', 'target': 'es', 'key': api_key}
    response = requests.post(url, data=params)
    return response

def test_google_vision_api(api_key):
    url = "https://vision.googleapis.com/v1/images:annotate"
    headers = {'Content-Type': 'application/json'}
    body = {
        "requests": [{
            "image": {"source": {"imageUri": "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"}},
            "features": [{"type": "LABEL_DETECTION"}]
        }]
    }
    response = requests.post(url, headers=headers, json=body, params={'key': api_key})
    return response

def test_google_drive_api(api_key):
    url = "https://www.googleapis.com/drive/v3/files"
    params = {'pageSize': 10, 'fields': 'files(id, name)', 'key': api_key}
    response = requests.get(url, params=params)
    return response

def test_google_sheets_api(api_key):
    url = "https://sheets.googleapis.com/v4/spreadsheets"
    params = {'key': api_key}
    response = requests.get(url, params=params)
    return response

def test_google_distance_matrix_api(api_key):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        'origins': 'New York,NY',
        'destinations': 'Los Angeles,CA',
        'key': api_key
    }
    response = requests.get(url, params=params)
    return response

def print_response(api_name, response):
    if response.status_code == 200:
        data = response.json()
        if 'error' in data or 'error_message' in data:
            print(f"{api_name} API Key is invalid or has insufficient permissions: {data.get('error', data.get('error_message'))}")
        else:
            print(f"{api_name} API Key is valid.")
    else:
        print(f"Failed to connect to {api_name} API. Status code: {response.status_code}")

def test_all_apis(api_key):
    apis = {
        'Google Geocoding': test_google_geocoding_api,
        'Google Places': test_google_places_api,
        'Google Calendar': test_google_calendar_api,
        'YouTube Data': test_youtube_data_api,
        'Google Translation': test_google_translation_api,
        'Google Vision': test_google_vision_api,
        'Google Drive': test_google_drive_api,
        'Google Sheets': test_google_sheets_api,
        'Google Distance Matrix': test_google_distance_matrix_api
    }
    
    for api_name, api_function in apis.items():
        print(f"Testing {api_name} API...")
        response = api_function(api_key)
        print_response(api_name, response)
        print()

# Replace with your API key
api_key = "AIzaSyCqu22Fn0KgrvgobU0U0Cwpc85s1vTVWrk"
test_all_apis(api_key)
