from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body), 201
    return jsonify(todos)

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position), 200
    todos.pop((position-1))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['PUT'])
def update_todo(position):
    if position < 1 or position > len(todos):
        return jsonify({"error": "Invalid position"}), 400
    
    request_body = request.get_json(force=True)
    
    if "label" not in request_body or "done" not in request_body:
        return jsonify({"error": "Invalid request body"}), 400
    
    todos[position - 1] = request_body
    
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)