from textwrap import indent
import folium
import requests
import json
ENDPOINT="https://eonet.gsfc.nasa.gov/api/v2.1/events?status=open"


def upda(name,dict):
    try:
        with open(f"{name}.json","r") as f:
            data=json.load(f)
            data.update(dict)
        with open(f"{name}.json","w") as f:
            json.dump(data,f,indent=4)
    except:
        with open(f"{name}.json","a") as f:
            json.dump(dict,f,indent=4)
k=requests.get(ENDPOINT)
k=k.json()
for m in k["events"]:
    # print(m)
    if m["categories"][0]["id"]==8:
        dict={
            m["title"]:{
                "coordinates":m[ "geometries"][0]["coordinates"]

            }
        }
        upda("wildfire",dict)
    elif m["categories"][0]["id"]==10:
        dict={
            m["title"]:{
                "coordinates":m[ "geometries"][0]["coordinates"]

            }
        }
        upda("cyclones",dict)
    elif m["categories"][0]["id"]==12:
        dict={
            m["title"]:{
                "coordinates":m[ "geometries"][0]["coordinates"]

            }
        }
        upda("volcanos",dict)
    else:
        dict={
            m["title"]:{
                "coordinates":m[ "geometries"][0]["coordinates"]

            }
        }
        upda("iceberg",dict)



