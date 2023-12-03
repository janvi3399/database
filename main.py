from flask import Flask, jsonify
import pymongo

app = Flask(__name__)

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["nytimes"]
collection = db["monthcomments"]

@app.route('/get_data', methods=['GET'])
def get_data():
   
    cursor = collection.find()

    
    result_list = list(cursor)

    
    result_dict = {item["month"]: {"happy": item["happy"], "sad": item["sad"], "neutral": item["neutral"]} for item in result_list}
    print(result_dict)

    return jsonify(result_dict)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
