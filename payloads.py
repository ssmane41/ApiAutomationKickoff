def addBookPayLoads(isbn):
    body = {
        "name": "Book1",
        "isbn": isbn,
        "aisle": "005",
        "author": "Robot1"}
    return body


def head():
    head = {
        'Content-Type': 'application/json'}
    return head


def parameters():
    para = {
        "AuthorName": "Robot1"}
    return para
