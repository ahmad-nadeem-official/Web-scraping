# import requests
# from bs4 import BeautifulSoup

# url = "https://www.foodpanda.pk/city/lahore"

# headers = {
#     'User-Agent': 'python-requests/2.26.0',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept': '*/*',
#     'Connection': 'keep-alive',
# }

# proxies = {
#    'http': 'http://182.93.69.74',
#    'https': 'http://144.202.62.103',
#    # Add more proxies if needed
# }

# response = requests.get(url, headers=headers, proxies=proxies)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content
#     soup = BeautifulSoup(response.content, "html.parser")
#     # Find elements containing restaurant names
#     restaurant_elements = soup.find_all("div", class_="box-flex vendor-title ai-center   fd-row")
#     # Extract restaurant names from the elements
#     restaurant_names = [element.text.strip() for element in restaurant_elements]
#     # Print the restaurant names
#     for name in restaurant_names:
#         print(name)
# else:
#     print("Failed to fetch data. Status code:", response.status_code)


import requests
from bs4 import BeautifulSoup

url = "https://www.foodpanda.pk/city/lahore"
headers = {
    'User-Agent': 'python-requests/2.26.0',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    restaurant_elements = soup.find_all("div", class_="box-flex vendor-title ai-center   fd-row")
    restaurant_names = [element.text.strip() for element in restaurant_elements]
    for name in restaurant_names:
        print(name)
else:
    print("Failed to fetch data. Status code:", response.status_code)
