from app import app
app.secret_key = 'super secret key of doom'

app.run(host='0.0.0.0', port=5000, debug=True)
