import pandas as pd
from docx import Document
import os


# Set up OpenAI API key
class AI:
    def __init__(self, api_key):
        from langchain_openai import ChatOpenAI
        os.environ["OPENAI_API_KEY"] = api_key

        self.llm = ChatOpenAI(model='gpt-4o-mini')

    def __call__(self, prompt):
        response = self.llm.invoke([
            ("human", prompt),
        ])
        return response.content


def create_prompt_for_task(task_description, contract_text):
    prompt = f"""
    You are a compliance analyst. Given the following contract conditions and task description, analyze whether the task description complies with the contract. If not, specify the reason for non-compliance.

    Contract Conditions:
    {contract_text}

    Task Description:
    {task_description}

    Return only Compliance Analysis:
    """

    return prompt


def read_contract_file(file):
    """ Read the contract text from a file """
    if file.endswith('.txt'):
        return file.read().decode('utf-8')
    elif file.endswith('.docx'):
        doc = Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])
    else:
        return "Unsupported file format."


def run_pipeline(table_file, contract_file, openai_key):
    contract_text = read_contract_file(contract_file)

    llm = AI(openai_key)
    # Load the CSV/XLSX file with task descriptions and cost estimates
    df = pd.read_csv(table_file) if table_file.endswith('.csv') else pd.read_excel(table_file)

    results = []
    for _, row in df.iterrows():
        task_description = row.values[0]
        cost_estimate = row.values[1]
        prompt = create_prompt_for_task(task_description, contract_text)
        compliance_analysis = llm(prompt)
        results.append({
            'task_description': task_description,
            'cost_estimate': cost_estimate,
            'compliance_analysis': compliance_analysis
        })

    result_df = pd.DataFrame(results)
    return result_df


def gradio_interface(contract_file, table_file):
    result_df = run_pipeline(table_file.name, contract_file.name, os.environ["OPENAI_API_KEY"])

    return result_df.to_csv(index=False)


if __name__ == "__main__":
    table_file, contract_file = 'Task example v3 (1).xlsx', 'contract.docx'
    run_pipeline(table_file, contract_file, os.environ["OPENAI_API_KEY"])
