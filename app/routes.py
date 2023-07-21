from app import app

@app.route('/')
def index():
    return 'Gotta Catch Em All'