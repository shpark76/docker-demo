# docker-demo
A Docker - composer example that provides a Flask, Java, Redis, MySQL and Mongo container

# How to use a docker and composer
##Docker Prerequisites:
- Windows
https://docs.docker.com/docker-for-windows/install/
- Mac
https://docs.docker.com/docker-for-mac/install/

### 1. git clone
```
git clone git@github.com:shpark76/docker-demo.git
```

### 2. docker compose build and up 
```
$ docker-compose build
...
 ---> Using cache
 ---> 57f1486a97fe
Step 5/5 : ENTRYPOINT ["java","-jar","spring-boot-web.jar"]
 ---> Using cache
 ---> a597836853da

Successfully built a597836853da
Successfully tagged docker-demo_java_app:latest
```

```
$ docker-compose up
```


### 3. Python application
```
http://localhost:5000
```

### 4. Java application
```
cd java/docker-spring-boot
mvn clean pacakge
...
http://localhost:8080
```  

