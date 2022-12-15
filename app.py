from flask import Flask, request, jsonify, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    ANSI()
    return 'Hello World'

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
  
    def style_text(code):
        return "\33[{code}m".format(code=code)
  
    def color_text(code):
        return "\33[{code}m".format(code=code)

@app.route('/predict_api', methods=["GET","POST"])
def list_post():
    json_body = request.get_json()
    predictions = 2 * json_body[0]   
    predictions = list(predictions)
    return jsonify(results = predictions)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)