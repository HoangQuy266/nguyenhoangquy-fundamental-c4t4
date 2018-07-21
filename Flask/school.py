from flask import Flask,redirect

app = Flask(__name__)
@app.route("/about-me")
def about_me() :
    return "Quy,16 "

@app.route("/school")
def school() :
    return redirect ("http://techkids.vn" ,code = 302)

if __name__ =="__main__" :
    app.run (debug=True)


from flask import Flask,redirect
app = Flask(__name__)
@app.route("/about-me")
def about_me() :
    return "Quy, 16"

@app.route("/users/<username>")
def users(username) :
    if username == "Quy" :
     return redirect ("http://127.0.0.1:5000/about-me",code=303)
    else :
        return "user not found"

if __name__ == "__main__" :
    app.run(debug=True)
    