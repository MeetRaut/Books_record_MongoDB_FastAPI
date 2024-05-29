# Books_record_MongoDB_FastAPI
RESTful API for efficient book record management using MongoDB and FASTAPI.

## Run locally
### Setup Virtual Environment
```bash
 virtualenv venv
 source venv/scripts/activate
 ```

### Install dependancies
```bash
pip install pymongo fastapi uvicorn
 ```

> [!NOTE]
> ### Project Structure
> Books_record_MongoDB_FastAPI/
>   ├── config/
>   |     ├──db.py
>   ├── models/
>   |     ├──user.py
>   ├── routes/
>   |     ├──user.py
>   ├── schemas/
>   |     ├──user.py
>   ├── index.py

### Run the application
```bash
uvicorn index:app --reload
 ```
Once the application is running, you can access it at `http://localhost:8000/docs`.