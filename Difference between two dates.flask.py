from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        date1_str = request.form.get('date1')
        date2_str = request.form.get('date2')
        
        # Convert strings to datetime objects
        d1 = datetime.strptime(date1_str, '%Y-%m-%d')
        d2 = datetime.strptime(date2_str, '%Y-%m-%d')
        
        # Calculate absolute difference
        diff = abs((d2 - d1).days)
        result = f"The difference is {diff} days."
        
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
