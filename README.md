# AIQA Geography API - Django

## Build and Run
Server comes with example pre-populated data. 

### Local server
In order to run API locally you need to install Python 3 (version at least 3.7 is suggested). Best way to do it is using `virtualenv` (or similar like `pipenv`). 

Copy repository and open the root folder then:
* run `pip3 install -r requirements.txt` to install necessary libraries. 
* go to `backend/` directory and start server via  `python3 manage.py runserver`

This will spin up the API running on `127.0.0.1:8000`. You can kill server using `control + C`


### Docker Container
Go to repository root folder (where the `docker-compose.yml` file is located.

Using Docker Compose:
* Build the image by `docker-compose build`
* Run the server by `docker-compose up`

This will spin up the API running on `127.0.0.1:8000`. You can kill server using `control + C`. It's good to clean up after

## Limitations
The API is not production ready and should not be used as such. Database of local server will be persistent as it's stored in SQLite file. For Docker containers data is only as container-lifetime persistent (destroying container will restore data to default state). 


## Tests

```
cd geo-docker-django/
pip3 install -r requirements.txt
cd backend-python/
pytest
```

## Integration Tests

Start backend and then:

```
cd geo-docker-django/
pip3 install -r requirements.txt
cd integration_tests
HOST=http://localhost:8000; export HOST
pytest
```
