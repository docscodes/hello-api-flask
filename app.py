from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/todo")
def todo():
  return jsonify("TODO")


@app.get("/greet")
def greet():
  return "Hello World!"


@app.get("/data")
def data():
  response = {"data": "Hello, World!"}
  return jsonify(response)


@app.get("/name")
def name():
  name = request.args.get("name")
  if not name:
    return jsonify({"status": "error"})

  response = {"data": f"Hello, {name} !"}
  return jsonify(response)


@app.get("/fullname")
def fullname():
  fname = request.args.get("fname")
  lname = request.args.get("lname")

  if not fname and not lname:
    return jsonify({"status": "error"})
  elif fname and not lname:
    response = {"data": f"Hello, {fname} !"}
  elif not fname and lname:
    response = {"data": f"Hello, Mr. {lname} !"}
  else:
    response = {"data": f"Is your name {fname} {lname} ?"}

  return jsonify(response)
