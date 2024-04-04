from flask import Flask, request
from flask_cors import CORS 

PORT=8091

app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

#@app.route("/")
#def hello():
#    return f"<h1 style='color: blue; font-size: 500%;'>Hello, {request.remote_addr}!</h1>"

@app.route("/")
def greeting():
    return{'greeting':"Hello, from flask!",'ip':request.remote_addr}    

@app.route("/test", methods=[ "GET", "POST"])
def test():
    if request.method == "POST":
        new_id = 555
        return {
            'msg': f"här får du id: {id}",
            'method': request.method
        }
    if request.method == 'DELETE':
        return {
            'msg': f"Du har raderat"
        }
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, ssl_context=(
        '/etc/letsencrypt/fullchain.pem', 
        '/etc/letsencrypt/privkey.pem'
    ))

