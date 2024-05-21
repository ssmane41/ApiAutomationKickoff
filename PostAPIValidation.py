import json
import time

import requests
import sys
from payloads import addBookPayLoads, head, parameters
from utilities.Configuration import getConfig, getPass
from utilities.resourses import ApiResources

# Add Book
url = getConfig()['API']['endpoint']
response_addBook = requests.post(url + ApiResources.AddBook, json=addBookPayLoads('bcd005'), headers=head())
json_response = response_addBook.json()
Book_ID = json_response['ID']
print(f"{Book_ID}:" + json.dumps(json_response))
if json_response["Msg"] == "Book Already Exists":
    sys.exit()
time.sleep(2)

# Delete Book
response_deleteBook = requests.post(url + ApiResources.DeleteBook, json={"ID": Book_ID}, headers=head())
json_response1 = response_deleteBook.json()
print(f'{Book_ID}: ' + json.dumps(json_response1))
time.sleep(2)

# Feth the Result
fetch_response = requests.get("http://216.10.245.166/Library/GetBook.php?AuthorName=Robot1", params=parameters())
print(fetch_response.status_code)
json_response = fetch_response.json()
pretty_json = json.dumps(json_response, indent=4)
print(pretty_json)

for actual_book in json_response:
    if actual_book['isbn'] == 'bcd005':
        print(actual_book)
        break
    else:
        print(f"TEST PASSED : Book having ID {Book_ID} is Deleted Successfully")
        break

expected_book = {
    "book_name": "Book1",
    "isbn": "bcd005",
    "aisle": "5"
}

if actual_book == expected_book:
    print("Book is not deleted")
else:
    print("Confirm!!! it is deleted")

# Authentication
url = "https://github.com"
github_response = requests.get(url, verify=False, auth=('ssmane41', getPass()))
print(github_response.status_code)
