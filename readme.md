# Smart Review Analyzer

An AI-powered product review analysis tool that automatically extracts **sentiment** and **feature mentions** from customer reviews using Hugging Face NLP models. Upload a JSON file of reviews and get instant visual insights — sentiment distribution, feature breakdown, confidence scores, and exportable results.

## Demo

[![Watch the Demo](https://img.youtube.com/vi/nTInIHAIDx8/maxresdefault.jpg)](https://youtu.be/nTInIHAIDx8)

## Features

- **Sentiment Analysis** — Classifies each review as Positive or Negative with a confidence score using a pre-trained Hugging Face sentiment pipeline.
- **Feature Classification** — Identifies which product feature (Battery, Camera, Performance, Price, Build Quality) a review discusses using Facebook's BART zero-shot classification model.
- **Drag & Drop Upload** — Upload a JSON file of reviews (up to 200 MB) via drag-and-drop or file picker.
- **Interactive Dashboard** — Visualizes results with a sentiment distribution doughnut chart and a feature mentions bar chart using Chart.js.
- **CSV Export** — Download the full analysis results as a CSV file for further use.
- **Keyboard Shortcuts** — `Ctrl+O` to open a file, `Ctrl+Enter` to start analysis.

## Tech Stack

| Layer    | Technology                                      |
| -------- | ----------------------------------------------- |
| Backend  | Python, FastAPI, Hugging Face Transformers       |
| Frontend | HTML, CSS, Vanilla JavaScript, Chart.js          |
| Models   | `sentiment-analysis` pipeline, `facebook/bart-large-mnli` |
| Server   | Uvicorn                                          |

## Project Structure

```
Smart-Review-Analyzer/
├── backend.py       # FastAPI server with sentiment & classification endpoints
├── index.html       # Complete frontend (UI, charts, file handling, API calls)
├── sample.json      # Example review data for testing
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/radhika-khatri/Smart-Review-Analyzer.git
cd Smart-Review-Analyzer

# Install dependencies
pip install fastapi uvicorn transformers torch pydantic

# Start the backend server
python backend.py
```

The API server will start at `http://localhost:8000`.

### Usage

1. Open `index.html` in your browser.
2. Upload a JSON file of reviews (see format below) or download the included sample.
3. Click **Analyze Reviews** and view the results dashboard.
4. Export results as CSV if needed.

### Sample Review Format

```json
[
  {
    "review_id": "1",
    "text": "The camera quality is excellent but battery drains fast."
  },
  {
    "review_id": "2",
    "text": "Great value for the price. Build feels premium."
  }
]
```

The tool also accepts `review_text` or `comment` as the text field name.

## API Endpoints

| Method | Endpoint          | Description                          |
| ------ | ----------------- | ------------------------------------ |
| POST   | `/api/sentiment`  | Returns sentiment label and score    |
| POST   | `/api/classify`   | Returns feature labels and scores    |
