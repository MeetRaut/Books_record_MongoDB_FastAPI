from fastapi import APIRouter, HTTPException
from models.book import Book
from config.db import conn
from schemas.book import bookEntity, booksEntity
from bson import ObjectId 

book = APIRouter()

@book.get('/')
async def find_all_books():
    return booksEntity(conn.local.book.find())

@book.get('/{id}')
async def find_one_book(id: str):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid ID format")
    
    book_data = conn.local.book.find_one({"_id": object_id})
    if not book_data:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return bookEntity(book_data)

@book.post('/')
async def create_book(book: Book):
    conn.local.book.insert_one(dict(book))
    return booksEntity(conn.local.book.find())

@book.put('/{id}')
async def update_book(id: str, book: Book):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid ID format")
    
    updated_book = conn.local.book.find_one_and_update(
        {"_id": object_id},
        {"$set": dict(book)},
        return_document=True 
    )
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return bookEntity(updated_book)

@book.delete('/{id}')
async def delete_book(id: str):
    try:
        object_id = ObjectId(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid ID format")
    
    deleted_book = conn.local.book.find_one_and_delete({"_id": object_id})
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return bookEntity(deleted_book)
