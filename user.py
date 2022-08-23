from flask import Flask, render_template,request
import os
import json
app = Flask(__name__)


@app.route('/')
def main():
    if not os.path.exists("data/"):
        os.makedirs("data/")
        f = open("data/user_data.json", "w")
        f.write(json.dumps([]))
        f.close()
    user_data = []
    f = open("data/user_data.json","r")
    user_data = json.loads(f.read())

    return render_template("home.html",user_data = user_data)

@app.route("/save_data",methods=['POST'])
def new_user():
    if request.method == "POST":
        name = request.form['name']
        number = request.form["number"]
        f = open("data/user_data.json","r")
        user_data = json.loads(f.read())
        if len(user_data) > 0:
            maxId = max(user_data, key=lambda x:x['id'])['id']
            maxId = int(maxId) + 1
            user_data.append({
                "id": maxId,
                "name":name,
                "number": number
            })
        else:
            user_data.append({
                "id": 1,
                "name":name,
                "number": number
            })
        f = open("data/user_data.json","w")
        f.write(json.dumps(user_data))
        f.close()
    return {"msg": "Data saved successfully"}, 201

@app.route("/save_edited_data",methods=['POST'])
def edit_user():
    if request.method == "POST":
        id_ = int(request.form['id'])
        number = request.form["number"]
        f = open("data/user_data.json","r")
        user_data = json.loads(f.read())
        index = 0
        for i in user_data:
            if i["id"] == id_:
                user_data[index]["number"] = number
                break
            index = index + 1

        f = open("data/user_data.json","w")
        f.write(json.dumps(user_data))
        f.close()
    return {"msg": "Data edited successfully"}, 201
