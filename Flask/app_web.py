# 1 create Flask App
from flask import Flask, render_template

app = Flask(__name__)

class Movie:
    def __init__(self,t,cast,thumb):
        self.title=t
        self.casts=cast
        self.thumbnail_url=thumb

m1= Movie("batman: The Darkness","MC, KKY, Mgod", "http://image.phimmoi.net/film/2945/poster.medium.jpg")

m2= Movie("Ant man",
        "RTZ",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTABHfHyn3kJ9hr7ajSVgFI-pFOtUZllRBN_Ev6wBqKoC8OhRvJ")

movie_list = [m1,m2]
@app.route("/")
def index():
    return render_template("index.html", name = "Quy",
    image_url="https://scontent.fhan5-1.fna.fbcdn.net/v/t1.0-1/c2.0.240.240/p240x240/36845899_424319321414269_998014695803715584_n.jpg?_nc_cat=0&_nc_eui2=AeEVRCDS3ArdjOPyRAXxx_75HJ3sPCiRpXa9vnzRF-f3joaAFlzKZg6a7meiVleoOh10DHKaFMbdRdnokbwAIJfGs7po4Dyrz6vTcUV9bX2icQ&oh=9aa249e2fc2d106ecc59e27ae84b2bea&oe=5BCF00C7")

@app.route("/casts")
def casts():
    return render_template("casts.html", casts= ["CONG LY", "QUANG TEO", "XUAN BAC"])

class Brand:
    def __init__(self, n, prd, thumb):
        self.name=n
        self.producer=prd
        self.thumbnail_url=thumb

b1=Brand("Fear of god", "Jerry Lorenzo", "https://cdn.shopify.com/s/files/1/1003/3354/t/5/assets/fifthcollection-lookbook-4.jpg?13030340865237012428")
b2=Brand("Rick Owens","Rick Owens", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRipgtoaaCfBztITDg0rkCt6hZcjUoPYANSHG_YVU4_OTkPmJH_")
b3=Brand("Supreme", "James Jebbia", "https://d1vfs9f7h1rfk4.cloudfront.net/media/Ed-Rumour_Mills/Supreme.png")

brand_list=[b1,b2,b3]
@app.route("/clothes")
def clothes():
    return render_template("clothes.html", clothess =brand_list)


@app.route("/movie")
def movie ():
    return render_template("movie.html",movies=movie_list)
    
@app.route("/about-me")
def about():
    return "My name is Quy"

@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name

# 2 Run app
if __name__ == "__main__":
    app.run(debug=True)