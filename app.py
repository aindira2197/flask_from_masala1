from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/res1', methods=['GET', 'POST'])
def res1():
    if request.method == 'POST':
        n = request.form.get('name')
        e = request.form.get('email')

        return render_template('res1.html', n=n, e=e)

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
