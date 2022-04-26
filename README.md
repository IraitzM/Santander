# Santander

Some additional files for those wanting to wrangle with information from [Santander's Open Data platform](http://datos.santander.es)

## Mock data generator

Sometimes the Open Data portal is not available so below you have the instructions to generate some mock data to emulate requests to the portal.

### Running the app

By simply setting a python environment so that requirements are installed:
```
pip install -r requirements.txt
```
Then it is just a matter of calling
```
python app/api.py
```

So the service is accesible at http://localhost:8000.

### Using docker

Could not be easier, just hit:
```
docker-compose up -d
```

And the container will be instantiated and running so requests to http://localhost:8000 can be done.