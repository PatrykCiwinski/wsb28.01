import json
import  pandas as pd

df=pd.read_json("f1.json")
drivers=df["drivers"]

list_points=[]
for driver in drivers:
    points=driver["points"]
    list_points.append(points)
    best=max(list_points)
    if driver["points"]==best:
        print(driver)
