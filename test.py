# import requests
# from bs4 import BeautifulSoup
#
# # Base URL pattern
# base_url = "https://www.postkhmer.com/national/{date}-{time}-{unique_code}.html"
#
# # Loop through years (yyyy)
# for year in range(2023, 2024):  # You can adjust the range as needed
#     # Loop through months (mm)
#     for month in range(8, 13):
#         # Loop through days (dd)
#         for day in range(3, 32):
#             # Loop through hours and minutes (HHMM)
#             for hour in range(8, 50):
#                 for minute in range(0, 60, 10):  # Increment by 10 minutes
#                     # Loop through the unique code (you can adjust the range as needed)
#                     for unique_code in range(253115, 253117):
#                         # Create the complete URL by formatting the components
#                         url = base_url.format(
#                             date=f"{year:04d}-{month:02d}-{day:02d}",
#                             time=f"{hour:02d}{minute:02d}",
#                             unique_code=unique_code
#                         )
#
#                         # Make the request and extract the content
#                         response = requests.get(url)
#                         if response.status_code == 200:
#
#                             soup = BeautifulSoup(response.content, 'html.parser')
#                             s = soup.find('div', class_='node node-article node-promoted clearfix')
#                             # Extract and print the desired content here
#                             # For example, print the title of the article
#
#                             print(f"URL: {url}, Title: {s}")
#                         else:
#                             continue
# import pickle
# import requests
# from bs4 import BeautifulSoup
#
# data = {}
# count = 0
# base_url = "https://www.postkhmer.com/national/{date}-{time}-{unique_code}.html"
#
# for year in range(2023, 2024):
#     for month in range(8, 13):
#         for day in range(3, 32):
#             for hour in range(8, 50):
#                 for minute in range(0, 60, 10):
#                     for unique_code in range(253115, 253117):
#                         url = base_url.format(
#                             date=f"{year:04d}-{month:02d}-{day:02d}",
#                             time=f"{hour:02d}{minute:02d}",
#                             unique_code=unique_code
#                         )
#                         count += 1
#
#                         response = requests.get(url)
#                         if response.status_code == 200:
#                             soup = BeautifulSoup(response.content, 'html.parser')
#                             s = soup.find('div', class_='paragraph-style')
#                             try:
#                                 content = s.find_all('p')
#                                 text = ''
#                                 for part in content:
#                                     text += part.text.replace('\u200b', '')
#                                 data[url] = text
#
#                                 if count % 1000 == 0:
#                                     print('Count: {}'.format(count))
#                             except:
#                                 pass
#                         else:
#                             continue
#
#                     pickle_file = 'data_postkhmer.pkl'
#                     with open(pickle_file, 'wb') as file:
#                         pickle.dump(data, file)
#
# print("Data has been saved to 'data_postkhmer.pkl'.")
#
#


import requests
from bs4 import BeautifulSoup

# Base URL pattern
base_url = "https://www.postkhmer.com/national/{date}-{time}-{unique_code}.html"

# Loop through years (yyyy)
for year in range(2023, 2024):  # You can adjust the range as needed
    # Loop through months (mm)
    for month in range(1, 13):
        # Loop through days (dd)
        for day in range(1, 32):
            # Loop through hours and minutes (HHMM)
            for hour in range(0, 24,1):
                for minute in range(0, 60, 30):  # Increment by 10 minutes
                    # Loop through the unique code (you can adjust the range as needed)
                    for unique_code in range(253100, 253103):
                        # Create the complete URL by formatting the components
                        url = base_url.format(
                            date=f"{year:04d}-{month:02d}-{day:02d}",
                            time=f"{hour:02d}{minute:02d}",
                            unique_code=unique_code
                        )

                        # Make the request and extract the content
                        response = requests.get(url)
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.content, 'html.parser')
                            # Extract and print the desired content here
                            # For example, print the title of the article
                            title = soup.find('h1', class_='title').text.strip()
                            print(f"URL: {url}, Title: {title}")
                        else:
                            print(f"Failed to fetch the content for URL: {url}")

