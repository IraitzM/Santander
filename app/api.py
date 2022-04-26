import random
import datetime
import json

# Serving
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # Sensors
    num_sensors = 486
    resources = []
    for i in range(num_sensors):
        sensor_data = {}
        sensor = str(1001+i)
        ocupacion = random.triangular(0, 100, 52)
        intensidad = random.randrange(2000)
        carga = random.triangular(0, 100, 52)
        sensor_data["ayto:ocupacion"] = str(int(ocupacion))
        sensor_data["ayto:intensidad"] = str(int(intensidad))
        sensor_data["ayto:carga"] = str(int(carga))
        sensor_data["ayto:medida"] = sensor
        sensor_data["ayto:idSensor"] = sensor
        sensor_data["dc:modified"] = datetime.datetime.now()
        identifier = f"{sensor}-6fc329f8-fedd-11e9-8087-005056a43242"
        sensor_data["dc:identifier"] = identifier
        sensor_data["usri"] = f"http://datos.santander.es/api/datos/mediciones/{identifier}.json"
        resources += [sensor_data]
    data = {}
    data['summary'] = {"items" : num_sensors, "items_per_page" : num_sensors, "pages": 1, "current_page": 1}
    data['resources'] = resources
    
    return data

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)