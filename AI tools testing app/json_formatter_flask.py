from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

TOOLS_JSON_FILE = "tools.json"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_json", methods=["POST"])
def generate_json():
    data = request.json

    new_entry = {
        "id": os.urandom(4).hex(),
        "Institution": "Jisc",
        "Author": "Jisc AI team",
        "Title": data.get("title"),
        "Description": data.get("description"),
        "Content": f"""
            <h2>Getting Started</h2><p>{data.get('gettingStarted')}</p>
            <h2>Examples of Use</h2><ul>{''.join([f'<li><a href="{ex['url']}" target="_blank">{ex['title']}</a> - {ex['institution']}</li>' for ex in data.get('examples', [])])}</ul>
            <h2>Key Information</h2><ul>{''.join([f'<li><strong>{info['label']}:</strong> <a href="{info['url']}" target="_blank">{info['value']}</a></li>' if 'url' in info else f'<li><strong>{info['label']}:</strong> {info['value']}</li>' for info in data.get('keyInfo', [])])}</ul>
        """,
        "Category": "General Chatbots and Assistants",
        "Logo": "/jisc-logo.svg",
    }

    # Load existing tools.json file and append new entry
    if os.path.exists(TOOLS_JSON_FILE):
        with open(TOOLS_JSON_FILE, "r") as file:
            try:
                tools_data = json.load(file)
            except json.JSONDecodeError:
                tools_data = []
    else:
        tools_data = []

    tools_data.append(new_entry)

    with open(TOOLS_JSON_FILE, "w") as file:
        json.dump(tools_data, file, indent=4)

    return jsonify(new_entry)


if __name__ == "__main__":
    app.run(debug=True)
