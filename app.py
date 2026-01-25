from flask import Flask, render_template

app = Flask(__name__)

# Anasayfa Rotası
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    # JetMenu 5000'de çalışıyor, Ajans sitesi 5001'de çalışsın.
    app.run(debug=True, port=5001)