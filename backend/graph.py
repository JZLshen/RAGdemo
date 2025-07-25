from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("graph.html")


@app.route("/update_graph", methods=["POST"])
def update_graph():
    try:
        with open("./templates/triplet.json", "r", encoding="utf-8") as f:
            triplet = json.load(f)  # 解析 JSON 数据为 Python 对象
        print(triplet)
        return triplet
    except Exception as e:
        return {"error": f"Error parsing graph data: {str(e)}"}


with open("./templates/triplet.json", "r", encoding="utf-8") as f:
    triplet = json.load(f)  # 解析 JSON 数据为 Python 对象
    print(triplet)
app.run(host="0.0.0.0", port=8085)
