#assigment 

## Info

### External services required 

#### Redis https://hub.docker.com/_/redis 
#### pipenv https://pipenv.pypa.io/en/latest/


### Environmental Variables

```bash
REDIS_HOST        # Host of running redis instance
REDIS_USER        # Redis username 
REDIS_PASSWORD    # Redis password 
```

### How to run 
```bash
pipenv install 
pipenv shell 
uvicorn api.main:app --reload
```
### Test

```
pytest
```
