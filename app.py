from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

rule = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    global rule
    if request.method == 'POST':
        if 'harga' in request.form:
            harga = float(request.form['harga'])
            satuan = request.form['satuan']
            rule = {'harga': harga, 'satuan': satuan}
            return redirect(url_for('calculate'))
        elif 'berat' in request.form:
            berat = float(request.form['berat'])
            total_harga = berat * rule['harga']
            return render_template('index.html', step=3, rule=rule, total_harga=total_harga)
    return render_template('index.html', step=1)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    return render_template('index.html', step=2, rule=rule)

@app.route('/reset', methods=['GET'])
def reset():
    global rule
    rule = {}
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
