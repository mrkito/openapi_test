---
title: Just Promt
emoji: 🐨
colorFrom: green
colorTo: indigo
sdk: gradio
sdk_version: 4.39.0
app_file: app.py
pinned: false
---

# Task Compliance Analysis

This project provides a system for analyzing task descriptions against contract conditions to determine compliance. It uses OpenAI's GPT-4 model to perform the analysis and presents the results through a Gradio interface.

## Features

- Upload contract files (txt or docx format)
- Upload task descriptions and cost estimates (CSV or XLSX format)
- Analyze task compliance using GPT-4
- Download analysis results as a JSON file

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`


# GUI

https://huggingface.co/spaces/speechmaster/just_promt

or install local

```
docker run -it -p 7860:7860 --platform=linux/amd64 \
	registry.hf.space/speechmaster-just-promt:latest python app.py
```

# Install pipeline local

```
pip install -r requirements.txt
```

## Usage

1. Run the Gradio interface:
```
python app.py
```
2. Open the provided URL in your web browser.

3. Upload your contract file (txt or docx) and task description file (CSV or XLSX).

4. Click "Submit" to run the analysis.

5. Download the results as a JSON file.

## File Structure

- `app.py`: Main application file with Gradio interface
- `pipeline.py`: Core logic for task compliance analysis
- `requirements.txt`: List of Python dependencies
