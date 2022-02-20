from flask import Flask ,render_template,request,jsonify
import json
from alert import send_email
import folium

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/signup")
def k():
    return render_template("signup.html")
    
@app.route("/signup",methods=["POST","GET"])
def singup():
    email=request.form['emai']
    name=request.form['name']
    phn=request.form['phn']
    password=request.form['pass']
    dict={
        name:
       { 'phone':phn,
        "email":email,
        "pass":password,
        "location":"location"
        }
    }
    try:
        with open("json/data.json","r") as f:
            data=json.load(f)
            print(type(data))
            data.update(dict)
        with open("json/data.json","w") as f:
            json.dump(data,f,indent=4)
    except:
        with open("json/data.json","a") as f:
            json.dump(dict,f,indent=4)

    send_email(email ,name)
    k=folium.Map(location=[30.733315,76.779419])
    folium.Marker(location=[30.733315,76.779419]).add_to(k)
    return render_template("index.html")

@app.route("/wildfire")
def func():
    map = folium.Map(
        location=[53.760860, -98.813873],
        tiles='Stamen Terrain',
        zoom_start=5.5
    )
     
    with open("json/wildfire.json","r") as f:
         dict=json.load(f)
    
    for m in dict:
        lat=dict[m]["coordinates"][1]
        lon=dict[m]["coordinates"][0]
        folium.Marker(
             icon = folium.Icon(color='red'),
             popup=(
                 "Coordinates: {coord}<br>"
                 "Name: {name}<br>"
             ).format(coord=[lat,lon],name=m),
             location=[lat,lon]
             ).add_to(map)

    return map._repr_html_()

@app.route("/cyclone")
def cyclone():
    map = folium.Map(
        location=[-18.334, 60.9],
        tiles='Stamen Terrain',
        zoom_start=2
    )
    with open("json/cyclones.json","r") as f:
         dict=json.load(f)
    
    for m in dict:
        lat=dict[m]["coordinates"][1]
        lon=dict[m]["coordinates"][0]
        folium.Marker(
             icon = folium.Icon(color='red'),
             popup=(
                 "Coordinates: {coord}<br>"
                 "Name: {name}<br>"
             ).format(coord=[lat,lon],name=m),
             location=[lat,lon]
             ).add_to(map)

    return map._repr_html_()

@app.route("/volcano")
def volcano():
    map = folium.Map(
        location=[-8.874217, 125.727539],
        tiles='Stamen Terrain',
        zoom_start=3
    )
    with open("json/volcanos.json","r") as f:
         dict=json.load(f)
    
    for m in dict:
        lat=dict[m]["coordinates"][1]
        lon=dict[m]["coordinates"][0]
        folium.Marker(
             icon = folium.Icon(color='red'),
             popup=(
                 "Coordinates: {coord}<br>"
                 "Name: {name}<br>"
             ).format(coord=[lat,lon],name=m),
             location=[lat,lon]
             ).add_to(map)

    return map._repr_html_()

@app.route("/iceberg")
def iceberg():
    map = folium.Map(
        location=[-75.22, -25.78],
        tiles='Stamen Terrain',
        zoom_start=3
    )
    with open("json/iceberg.json","r") as f:
         dict=json.load(f)
    
    for m in dict:
        lat=dict[m]["coordinates"][1]
        lon=dict[m]["coordinates"][0]
        folium.Marker(
             icon = folium.Icon(color='red'),
             popup=(
                 "Coordinates: {coord}<br>"
                 "Name: {name}<br>"
             ).format(coord=[lat,lon],name=m),
             location=[lat,lon]
             ).add_to(map)

    return map._repr_html_()


if __name__=="__main__":
 app.run(debug=True)