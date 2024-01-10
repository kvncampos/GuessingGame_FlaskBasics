from flask import Flask, render_template
import random

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')


@app.route("/")
def start_game():
    return render_template('index.html')


@app.route("/<int:num>")
def guess_page(num=None):
    nums = list(range(1, 10))
    random_num = random.randint(1, 9)
    if num not in nums:
        return '404 ERROR'
    if num == random_num:
        return render_template('won.html', number=num)
    else:
        return render_template('lost.html', number=num)


if __name__ == '__main__':
    app.run(debug=True)
