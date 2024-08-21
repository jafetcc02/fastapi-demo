### FastAPI DEMO 

In this demo I installed FastAPI, and used it to create a new app. Learned how to define routes, handle errors, use request and path parameters, validating data with Pydantic models, modelling responses, and how to use the interactive documentation


## Prerequisities

Before you try to replicate this demo, ensure you have met the following requirements. 

* You have a Windows/Linux/Mac machine running Python 3.10+. 
* You have installed the latest versions of pip and virtualenv or conda (Anaconda). 

## Libraries 

The necessary libraries are 

```bash
pip install fastapi
pip install uvicorn
pip install requests
```

## Main Commands 

To start up application run the following command in different terminal 


```bash
uvicorn main:app --reload
```
Now the following commands are for a cmd.exe (Windows terminal). If using another, search for the corresponding commands. 

* Post item 

```bash
curl -X POST -H 'Content-Type:application/json' http://127.0.0.1:8000/items?item=banana
```

* Get item 

```bash
curl -X GET http://127.0.0.1:8000/items/0
```

* Get item using Item class 

```bash
curl -X POST -H "Content-Type:application/json" -d "{\"text\": \"apple\"}" http://127.0.0.1:8000/items
```


## FastAPI documentation 

Another way to test api is: http://127.0.0.1:8000/docs#/ 





