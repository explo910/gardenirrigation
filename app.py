from flask import Flask, request, render_template
import threading
import time

app = Flask(__name__)

def workerThread():
    # Here goes the Logic
    while True:
        try:
            with open('config.ini', 'r') as f:
                content = f.read()
                # print("Tick")
        except FileNotFoundError:
            print("File not present")
        time.sleep(10)

@app.route('/', methods=['GET', 'POST'])
def index():
    content = ''
    if request.method == 'POST':
        # Get new Settings from Form
        text = request.form['text']
        print("Kreis 1 - Start: " + request.form['start1'] + " End: " + request.form['end1'])
        print("Kreis 2 - Start: " + request.form['start2'] + " End: " + request.form['end2'])
        print("Kreis 3 - Start: " + request.form['start3'] + " End: " + request.form['end3'])
        print("Kreis 4 - Start: " + request.form['start4'] + " End: " + request.form['end4'])
        print("Kreis 5 - Start: " + request.form['start5'] + " End: " + request.form['end5'])
        
        # Write the Config
        with open('config.ini', 'w') as f:
            f.write(text)
        with open('config.ini', 'r') as f:
            content = f.read()
    # Render Site with new config
    return render_template('index.html', content=content)

if __name__ == '__main__':
    # Start Worker Thread
    threading.Thread(target=workerThread, daemon=True).start()
    # Start Site
    app.run(debug=True)