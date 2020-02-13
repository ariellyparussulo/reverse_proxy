# Basic Reverse Proxy in Python

## Step-to-Step

1. read file as a parameter.
2. use looping to read its sintax.
3. define sintax that we will use in the config file (maybe use yaml of json to simplify).
4. write simple reverse proxy rules
   1. port that it will listen
   2. answers localhost/127.0.0.1
   3. yaml:
    
```yaml
main: # mandatory
  port: 80
  redirect-to-https: boolean
root: # mandatory (will be /)
  redirect: boolean
  to: path1 # must be a node of this yaml
path1: # will be /path1
  to: localhost:8080
path2:
  to: localhost:8081
```