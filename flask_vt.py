
import sqlite3
from flask import Flask, render_template, request



app = Flask(__name__)

def index():
    return render_template('index.html')

@app.route('/musteri', methods=['GET', 'POST'])
def musteri():
    if request.method == 'POST':
        musteri_adi = request.form['musteri_adi']
        conn = sqlite3.connect('maliyet_analizi.db')
        c = conn.cursor()
        c.execute("SELECT * FROM maliyet_analizi WHERE musteri=?", (musteri_adi,))
        rows = c.fetchall()
        conn.close()
        return render_template('musteri.html', rows=rows)
    else:
        return render_template('musteri.html')

@app.route('/kayit', methods=['POST'])

def kayit():
    musteri_bilgisi_al = request.form['musteri_bilgisi_al']
    panel_sonuc_usd = float(request.form['panel_sonuc_usd'])
    src_fiyat = float(request.form['src_fiyat'])
    konstrüksiyon_fyt = float(request.form['konstrüksiyon_fyt'])
    diger_giderler = float(request.form['diger_giderler'])
    beton_fyt = float(request.form['beton_fyt'])
    iscilik_fyt = float(request.form['iscilik_fyt'])
    toplam_maliyet_usd = panel_sonuc_usd + src_fiyat + konstrüksiyon_fyt + diger_giderler + beton_fyt + iscilik_fyt

    conn = sqlite3.connect('maliyet_analizi.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS maliyet_analizi
                 (id INTEGER PRIMARY KEY,
                  musteri TEXT,
                  panel FLOAT,
                  surucu FLOAT,
                  konstruksiyon FLOAT,
                  diger_giderler FLOAT,
                  beton_maliyeti FLOAT,
                  iscilik_maliyeti FLOAT,
                  toplam_maliyet FLOAT)''')
    c.execute("INSERT INTO maliyet_analizi VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
              (musteri_bilgisi_al, panel_sonuc_usd, src_fiyat, konstrüksiyon_fyt,
               diger_giderler, beton_fyt, iscilik_fyt, toplam_maliyet_usd))
    conn.commit()
    conn.close()

    return render_template('kayit.html', musteri_bilgisi=musteri_bilgisi_al, toplam_maliyet=toplam_maliyet_usd)

if __name__ == '__main__':
    app.run(debug=True)

