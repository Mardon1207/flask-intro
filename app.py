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
    <form action="https://mardon.pythonanywhere.com/api/sum">
    <label>a:</label>
    <input type="text"  name="a" value="">
    <p>+</p>
    <label>b:</label>
    <input type="text" name="b" value=""><br><br>
    <input type="submit" value="Submit">
    </form>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)
