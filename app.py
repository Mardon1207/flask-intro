from flask import Flask, request

app = Flask(__name__)
@app.route("/api/sum")
def hello():
    data = request.values
    print(data["a"])
    return {"sum":int(data["a"])+int(data["b"])}

@app.route('/')
def query():
    html = """
    <form action="http://127.0.0.1:5000/api/sum">
    <label>a:</label><br>
    <input type="text"  name="a" value="0"><br>
    <label>b:</label><br>
    <input type="text" name="b" value="0"><br><br>
    <input type="submit" value="Submit">
    </form>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)
