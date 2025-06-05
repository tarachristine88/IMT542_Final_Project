from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

DATA_PATH = '/Users/tarahulcome/imt542_tara/myproject/tara_diary_examples.json'

with open(DATA_PATH, 'r') as f:
    diary_data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', entries=diary_data)

@app.route('/filter', methods=['GET'])
def filter_entries():
    # Get filter values from the query string
    confidence_min = request.args.get('min_confidence', type=float)
    name = request.args.get('name', '').strip().lower()
    country = request.args.get('country', '').strip().lower()
    date = request.args.get('date')  # Format: 'YYYY-MM-DD'

    # Start with all data
    filtered = diary_data

    # Apply OCR confidence filter
    if confidence_min is not None:
        filtered = [e for e in filtered if e.get('ocr_confidence', 0) >= confidence_min]

    # Apply person name filter (partial match against list)
    if name:
        filtered = [
            e for e in filtered
            if any(name in person.lower() for person in e.get('people_mentioned', []))
        ]

    # Apply exact country match (case-insensitive)
    if country:
        filtered = [
            e for e in filtered
            if e.get('country', '').strip().lower() == country
        ]

    # Apply date filter (on or after)
    if date:
        filtered = [
            e for e in filtered
            if e.get('date', '') >= date
        ]

    # Render the UI with filtered results
    return render_template('index.html', entries=filtered)

@app.route('/diary')
def all_entries():
    return jsonify(diary_data)

@app.route('/ocr-confidence')
def ocr_confidence():
    min_conf = float(request.args.get('min', 0))
    return jsonify([e for e in diary_data if e.get('ocr_confidence', 0) >= min_conf])
