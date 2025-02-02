## Trading-app-backend

Deployed base url: https://trading-app-backend-4.onrender.com  
Tech: Python, FastAPI


## How to run locally

```bash

#clone repo
git clone https://github.com/groom115/Trading-app-backend.git
cd trading-app-backend

#create virtual env
python -m venv venv
.\venv\Scripts\activate

# For installing lib
pip install -r requirements.txt

# For running locally
uvicorn app.main:app --reload

```

## Different routes

```bash

Auth: post /login Payload: [email, password]
      post /signup Payload: [email, password]

Table: post /table (for adding table)
       get /table (for fetching table)
       put /table?row_id (for updating table)
       del /table (for deleting table)
       get /table/restore (for restoring table)

Random Number: get /numbers (for fetching random numbers)

