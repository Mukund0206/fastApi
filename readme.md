
* FastAPI is express like framework to deploy production-ready ML models (as microservice) in python. 

* FastAPI => just a framework for building your api 
* To serve the HTTP request, fastAPI uses **Uvicorn** as server. 
* Uvicorn is lightning-fast ASGI server. ASGI stands for asynchronous gateway interface which is capable of providing async interface to serve the request.


checks > 

```
python3 --version 
pip --version 

pip list 
pip3 list (fastapi and uvicorn server are installed for pip3 so it is visible here only)


```


steps > 

1. ```pip install fastapi ```  => install framework 
2. ```pip install "uvicorn[standard]" ``` => install server to serve http request 
3. ```uvicorn main:app --reload ``` => create root route and run uvicorn server 
