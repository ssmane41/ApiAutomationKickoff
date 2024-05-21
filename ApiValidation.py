import json
import requests

# Add Book
# head = {
#     "name": "Book1",
#     "isbn": "bcd003",
#     "aisle": "003",
#     "author": "Robot1"}
#
# response_add = requests.post("http://216.10.245.166/Library/Addbook.php", headers=head)
# print(response_add.json())
#
# if response_add.status_code == 200:
#     print("Book Added Successfully")

#Fetch Book
para = {
    "AuthorName": "Robot1"}

response = requests.get("http://216.10.245.166/Library/GetBook.php?AuthorName=Robot1", params=para)
print(response.status_code)
json_response = response.json()
pretty_json = json.dumps(json_response, indent=4)
print(pretty_json)
print(response.headers)

# print(response.headers)

# for actual_book in json_response:
#     if actual_book['isbn'] == 'bcd002':
#         print(actual_book)
#         break
#
# expected_book = {
#         "book_name": "Book1",
#         "isbn": "bcd002",
#         "aisle": "2"
#     }
# assert actual_book == expected_book


