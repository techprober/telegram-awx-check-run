import os
from index import app
from dotenv import load_dotenv

load_dotenv()

# Start flask server
app.run(host='0.0.0.0', port=os.getenv("PORT"), debug=True)
