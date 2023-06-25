
import requests


def download_file(url, destination, headers=None):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print("Download complete.")
    else:
        print("Failed to download the file.")


# Example usage with headers
url = "https://www.draftkings.com/lineup/getavailableplayerscsv?contestTypeId=37&draftGroupId=88776"
destination = "DKSalaries.csv"
headers = {"User-Agent": "Mozilla/5.0"}  # Example header
download_file(url, destination, headers)
