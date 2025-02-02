## Trading-app-backend

Deployed base url: https://trading-app-backend-4.onrender.com.
Tech: Python, fastApi

## How to run locally

```bash

#clone repo
git clone
cd trading-app-backend

#create virtual env
python -m venv venv
.\venv\Scripts\activate

# For installing lib
pip install -r requirements.txt

# For running locally
uvicorn app.main:app --reload

