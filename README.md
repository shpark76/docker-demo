# docker-demo
A Docker - composer example that provides a Django, Flask, Java, Redis, Elasticsearch, MySQL and Mongo container

# How to use a docker and composer
---
## Docker Prerequisites:
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
// create a java jar package to build a docker-compose
cd java/docker-spring-boot
mvn clean package


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

# Let’s run the API using docker
## Let’s build the docker image
```
docker-compose build
```

## Docker compose up with all associated docker compose services
```
$ docker-compose up
```
#### Note:
If you prefer to use a daemon mode, Let’s run the above command in the background:
```
$ docker-compose up -d
```

### 3. Flask Python application
```
http://localhost:5000
```

### 4. Django Python application
```
http://localhost:8000
```

### 5. Java application
```
http://localhost:8080
```  

### 6. Node.js application
Reference: https://github.com/nodejs/docker-node/blob/master/README.md#how-to-use-this-image
```
...
http://localhost:3000
```  

### 7. Jupyter Notebook
```
...
notebook_1        | [I 01:04:55.648 NotebookApp]  or http://127.0.0.1:8888/?token=0b6df051cfa20fa2656ae45bfc77bfe7510ea66abb7fcce7
...

Open browser:
http://127.0.0.1:8888/?token=0b6df051cfa20fa2656ae45bfc77bfe7510ea66abb7fcce7
```


#### If you want to build/run a specific application
> ```
> docker-compose build <custom service>
> docker-compose run <custom service>
> 
> i.e. 
> docker-compose build nodejs_app
> docker-compose run nodejs_app
> ```

---
## How to use Redis, Elasticsearch, MySQL and Mongo
### 1. Redis
https://redis.io/topics/rediscli
```
$ redis-cli -h localhost -p 6379
localhost:6379> exit
$ redis-cli ping
PONG
```

### 2. Elasticsearch
https://logz.io/blog/elasticsearch-cheat-sheet/
```json
curl -X GET  http://localhost:9200
{
  "name" : "es01",
  "cluster_name" : "es-docker-cluster",
  "cluster_uuid" : "Zv5BbMKkRza4s6YXiE5HxA",
  "version" : {
    "number" : "7.10.1",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "1c34507e66d7db1211f66f3513706fdf548736aa",
    "build_date" : "2020-12-05T01:00:33.671820Z",
    "build_snapshot" : false,
    "lucene_version" : "8.7.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

### 3. MySQL
https://www.mysql.com/products/workbench/
```
mysql -h localhost -p 3306 -u root -p1234
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)

But, you may not be able to connect via command line.
Please use workbench
```

### 4. Mongo
https://docs.mongodb.com/manual/mongo/
```
$ mongo "mongodb://localhost:27017"
MongoDB shell version v4.2.0
connecting to: mongodb://localhost:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("01c0e70a-3a99-45f1-9362-b9fa55378ed7") }
MongoDB server version: 4.4.2
...
Server has startup warnings:
{"t":{"$date":"2020-12-29T22:41:27.486+00:00"},"s":"W",  "c":"CONTROL",  "id":22120,   "ctx":"initandlisten","msg":"Access control is not enabled for the database. Read and write access to data and configuration is unrestricted","tags":["startupWarnings"]}
...
```