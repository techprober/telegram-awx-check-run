from index import app
from dotenv import dotenv_values

config = dotenv_values(".env")

# Start flask server
app.run(host='0.0.0.0', port=config["PORT"], debug=True)
