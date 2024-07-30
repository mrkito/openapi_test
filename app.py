import json
import os

import gradio as gr

from pipeline import run_pipeline


def gradio_interface(contract_file, table_file, OPENAI_API_KEY):
    result_df = run_pipeline(table_file.name, contract_file.name, OPENAI_API_KEY)

    result_json = result_df.to_json(orient='records')  # Convert to JSON string
    with open('result.json', 'w') as f:
        json.dump(result_json, f)

    return 'result.json'


# Create Gradio interface
iface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.File(label="Contract file"),
        gr.File(label="Upload CSV/XLSX with Task Descriptions and Cost Estimates"),
        gr.Textbox(label="OPENAI_API_KEY"),
    ],
    outputs=gr.File(label="Download Analysis Results (JSON)"),
    title="Task Compliance Analysis",
    description="Upload a CSV/XLSX file containing task descriptions and cost estimates. The system will analyze the compliance of each task description with the contract conditions and provide the results."
)

if __name__ == "__main__":
    iface.launch()
