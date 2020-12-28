import time
import redis
import pymysql

from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from bson import json_util



app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
# uri = "mongodb://%s:%s@%s" % (
#     quote_plus("mongo"), quote_plus("mongo"), quote_plus("localhost:27017"))
mongo = MongoClient('mongo_db', 27017)

#mysqldb = pymysql.connect('mysql_db', 'root', '1234', 'andrew')


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/', methods=['GET'])
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/mongo', methods=['GET'])
def mongo_fetch():   
    db = mongo.netflix
    netflix = db.netflix_titles.find()
    result = dumps(netflix, default=json_util.default)
    return jsonify(result=result)

@app.route('/mongo/kpop', methods=['GET'])
def mongo_kpop_fetch():   
    db = mongo.kpop
    girl_grops = db.kpop_idols_girl_groups.find()
    result = dumps(girl_grops, default=json_util.default)
    return jsonify(result=result)


@app.route('/mysql', methods=['GET'])
def mysql_fetch():
    result=""   
    try:
        with mysqldb.cursor() as cur:
            cur.execute('SELECT * FROM exchange_rates')
            rows = cur.fetchall()
            for row in rows:
                result += f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} <br>'
                print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}')
    finally:
        print("")
        #mysqldb.close()
    return (result)


app.run(host='0.0.0.0', debug=True)

