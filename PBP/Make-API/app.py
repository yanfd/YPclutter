from flask import Flask, jsonify, request, abort
import random
import os

app = Flask(__name__)

# 模拟一个数据库
quotes = [
    "Life is short, enjoy it.",
    "Stay hungry, stay foolish.",
    "Never give up."
]

@app.route("/quote", methods=["GET"])
def get_random_quote():
    """获取随机一条名言"""
    random_quote = random.choice(quotes)
    return jsonify({"quote": random_quote})

@app.route("/quote/<int:id>", methods=["GET"])
def get_quote_by_id(id):
    """根据 ID 获取名言"""
    if id < 0 or id >= len(quotes):
        abort(404, description="Quote not found")  # 如果 ID 无效，返回 404 错误
    return jsonify({"quote": quotes[id]})

@app.route("/quote", methods=["POST"])
def add_quote():
    """添加一条名言"""
    data = request.get_json()
    if not data or "quote" not in data:
        abort(400, description="Invalid request")  # 如果请求数据无效，返回 400 错误
    
    new_quote = data["quote"]
    quotes.append(new_quote)
    return jsonify({"message": "Quote added", "id": len(quotes) - 1}), 201

@app.errorhandler(404)
def not_found(error):
    """处理 404 错误"""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(400)
def bad_request(error):
    """处理 400 错误"""
    return jsonify({"error": str(error)}), 400

if __name__ == "__main__":
    app.run(debug=True)

"""原代码 
from flask import Flask
from flask.json import jsonify
import random
import os

app = Flask(__name__)


@app.route("/")
def life():
    fin = open("projects/Make-API/quote.txt", "r")
    Random_line = random.randint(0, 2)
    quote = fin.readlines()[Random_line]
    
    return jsonify(quote[0:-1])


if __name__ == "__main__":
    app.run(debug=True)


# print(os.getcwd())
_____________________________________________________
"""

"""
改进后的功能
获取随机名言：

访问 GET /quote，返回一条随机的名言。

根据 ID 获取名言：

访问 GET /quote/<id>，返回指定 ID 的名言。如果 ID 无效，返回 404 错误。

添加名言：

访问 POST /quote，通过请求体传递 JSON 数据（如 {"quote": "New quote"}），添加一条新的名言。

错误处理：

对无效请求或资源不存在的情况返回合适的错误信息。

测试 API
获取随机名言：

bash
复制
curl http://127.0.0.1:5000/quote
返回：

json
复制
{
  "quote": "Stay hungry, stay foolish."
}
根据 ID 获取名言：

bash
复制
curl http://127.0.0.1:5000/quote/1
返回：

json
复制
{
  "quote": "Stay hungry, stay foolish."
}
添加名言：

bash
复制
curl -X POST http://127.0.0.1:5000/quote -H "Content-Type: application/json" -d '{"quote": "New quote"}'
返回：

json
复制
{
  "message": "Quote added",
  "id": 3
}
错误处理：

访问不存在的 ID：

bash
复制
curl http://127.0.0.1:5000/quote/100
返回：

json
复制
{
  "error": "404 Not Found: Quote not found"
}
总结
你最初的代码确实实现了一个简单的 API，但它只是一个起点。

通过添加更多功能（如支持多种 HTTP 方法、处理请求参数、错误处理等），可以构建一个更完整、更实用的 API。

API 的核心是提供标准化的接口，让客户端和服务器能够高效、可靠地交互。
"""