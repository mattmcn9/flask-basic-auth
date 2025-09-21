import os
from flask import Flask
from flask_autoindex import AutoIndex
from flask_basicauth import BasicAuth

app = Flask(__name__)

# Get env vars (with defaults)
USERNAME = os.getenv("USERNAME", "user")
PASSWORD = os.getenv("PASSWORD", "password")
DATA_DIR = os.getenv("DATA_DIR", "/data")
PORT = int(os.getenv("PORT", "8080"))

# Configure basic auth
app.config['BASIC_AUTH_USERNAME'] = USERNAME
app.config['BASIC_AUTH_PASSWORD'] = PASSWORD
basic_auth = BasicAuth(app)

# Enable directory listing
AutoIndex(app, browse_root=DATA_DIR, add_url_rules=True)

@app.before_request
@basic_auth.required
def require_auth():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)

