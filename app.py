from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    data = request.values
    print(data)
    
    return {"sum":15}

@app.route('/form')
def query():
    html = """
    <form action="http://127.0.0.1:5000/">
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
