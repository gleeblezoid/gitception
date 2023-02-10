from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

picture = r"potatoes.jpeg"


@app.route("/")
def generate_page():
    if picture == "potatoes.jpeg":
        header = "Po-tay-toes!"
    else:
        header = "Oh no, that's not potatoes!"
    page = render_template("page.html", vegetable=picture, header=header)

    return page


if __name__ == "__main__":  # pragma: no cover
    app.run(host="0.0.0.0", port=8080, debug=True)
