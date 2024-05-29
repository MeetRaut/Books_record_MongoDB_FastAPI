def bookEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "title":item["title"],
        "author":item["author"],
        "publishYear":item["publishYear"]
    }

def booksEntity(entity) -> list:
    return [bookEntity(item) for item in entity]