from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result='')

@app.route('/run', methods=['POST'])
def run_script():
    try:
        result = subprocess.run(['venv/Scripts/python', 'focus1.py'], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"An error occurred: {e.stderr}\n{e.stdout}"
    except Exception as e:
        import traceback
        output = f"An unexpected error occurred: {traceback.format_exc()}"
    return render_template('index.html', result=output)

if __name__ == '__main__':
    app.run(debug=True)
