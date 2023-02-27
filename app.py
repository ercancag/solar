from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/musteri')
def musteri():
    musteri_adi = request.args.get('musteri_adi')
    conn = sqlite3.connect('maliyet_analizi.db')
    c = conn.cursor()
    c.execute("SELECT * FROM maliyet_analizi WHERE musteri=?", (musteri_adi,))
    rows = c.fetchall()
    conn.close()
    return render_template('musteri.html', musteri_adi=musteri_adi, rows=rows)

if __name__ == '__main__':
    app.run()
