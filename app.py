from pathlib import Path
import json
import os
from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.static_folder = 'static'
app.config['DEBUG']=False
jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    # block_start_string='"%',
    # block_end_string='%"',
    # variable_start_string='**',
    # variable_end_string='**',
    comment_start_string='<#',
    comment_end_string='#>',
))
app.jinja_options = jinja_options

@app.route('/')
def main_page():
    with open("content.json", encoding='utf-8') as f:
        content = json.load(f)
    print(content)
    return render_template('index.html', **content)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 9001))
    debug = os.environ.get("DEBUG", True)
    print(f"Starting app at port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
