# mini-rag 

this is an implementation of RAG SYSTEM for question answering 

##  Requrements 

- Python 3.10 or later 

### install pythong using miniconda 

- go to the cmd  and write these commands 

1) download and install mini conda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install)

``` bash 
$ curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
```
2) create the environment 
``` bash
~ conda create -n mini-rag-app python=3.10 
``` 
3) Activate the environment:
``` bash 
$ conda activate mini-rag-app
``` 

### install required packages 

``` bash
$ pip install -r requirements.txt 
``` 
### setup environment variables
``` bash 
$ cp .env.example .env  
- set your environment variables in you '.env' like 'OPEN_API_KEY' to your actual key in openai

4) run fastapi 
``` bash 
$ uvicorn main:app --reload 
```