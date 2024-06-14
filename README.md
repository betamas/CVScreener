# O-1A Visa Screener

## Author
Sravan Jayanthi

## Demo


## Introduction

This project aims to develop an AI application that can roughly assess how qualified a person is for an O-1A immigration visa based on their curriculum vitae (CV) or resume. The O-1A visa is a non-immigrant visa for individuals with extraordinary ability in the sciences, arts, education, business, or athletics.
Project Overview
The O-1A visa has eight criteria defined by the United States Citizenship and Immigration Services (USCIS). This project uses natural language processing (NLP) and large language models (LLMs) to analyze a person's CV and provide an assessment of how well they meet each of the eight criteria.
The project has the following components:

System Design: A detailed design document outlining the architecture and components of the AI application.
API Endpoint: A FastAPI endpoint that accepts a CV as input and returns two outputs:

- A score for each of the eight O-1A criteria, indicating how well the person meets that criterion.
- An overall assessment of the person's qualification for the O-1A visa based on the scores.


## Setup Instructions

### Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.10
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [Optional]- [Tesseract](https://github.com/tesseract-ocr/tesseract) & [Poppler](https://poppler.freedesktop.org/)


### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/Multimodal-RAG.git
    cd Multimodal-RAG
    ```

2. Create and activate a new Conda environment:

    ```sh
    conda create -n mrag python=3.8
    conda activate mrag
    ```
3. [Optional] Install PyTorch with CUDA toolkit packaged:

    ```sh
    conda install anaconda::pillow==9.2.0 pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
    ```

4. [Optional] Install Detectron2 (Windows):

    Follow the instructions [here](https://ivanpp.cc/detectron2-walkthrough-windows/#step3installdetectron2).

5. [Optional] Install Layout Parser:

    Follow the instructions [here](https://layout-parser.readthedocs.io/en/latest/notes/installation.html).



## Run Application

To setup the backend service, in a separate shell run `python backend\qa_service.py`

With both services setup, you can ping `http://localhost:8001/` & start submitting queries!

## Test a Query
In a separate python shell, load your pdf
```
import pdfplumber
def load_pdf_text(filename):
    with pdfplumber.open(filename) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

filename = 'docs/cvsamples.pdf'
pdf_text = load_pdf_text(filename)
```

and write a script to call the API
```
import requests
import json

def run_query(query):
    url = "http://localhost:8001/answer"

    # Sample data to send in the request body
    data = {"message": query}

    # Convert the data to JSON
    json_data = json.dumps(data)

    # Set the headers to application/json
    headers = {"Content-Type": "application/json"}

    # Send a GET request (since the endpoint is defined with @app.get)
    response = requests.get(url, headers=headers, params={"message_json": json_data})

    # Check if the response was successful
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.text)
```
to test a resume:
```
output = run_query(pdf_text)
print(output['result'])
```


### Example Results
For `docs/cvsamples.pdf`, here is an output from the grading service
```
Based on the information provided in Juan Garcia's CV, we can assess his qualifications for an O-1A immigration visa against the 8 criteria set by USCIS:
```
### 1. Awards
- **Fulbright Scholarship to pursue a PhD**, 20XX (20 scholarships awarded in Argentina that year)
- **Flag Honor Guard Member**, 20XX (Qualified by graduating with honors and ranking 4th among engineering majors at UNSJ)

**Assessment**: **Medium**. The Fulbright Scholarship is internationally recognized and highly prestigious; however, additional awards could strengthen this criterion further.

### 2. Membership
- No specific memberships in associations that require outstanding achievements are listed.

**Assessment**: **Low**. No evidence provided in the CV fits this criterion.

### 3. Press
- No published material in major media or trade publications about Juan Garcia is listed.

**Assessment**: **Low**. No evidence provided in the CV fits this criterion.

### 4. Judging
- No evidence of judging the work of others is listed.

**Assessment**: **Low**. No evidence provided in the CV fits this criterion.

### 5. Original Contribution
- **Research Experience**: Contributed to multi-disciplinary projects aimed at developing visualizations and simulations for seismic force resistance and seismic assessment of large projects (e.g., Dr. Guillermo Rawson Hospital).

**Assessment**: **Medium to High**. Highlights contributions to significant research projects; however, more specific examples of original contributions of major significance would strengthen this criterion.

### 6. Scholarly Articles
- Authorship of several journal articles and conference presentations.

**Assessment**: **High**. Multiple scholarly articles in respected journals and numerous conference presentations demonstrate a strong track record of scholarly work.

### 7. Critical Employment
- Employed in critical capacities, such as leading seismic validation at a large hospital and contributing to significant structural assessment projects.

**Assessment**: **Medium to High**. Demonstrates critical work in essential projects; employed in roles critical to large and distinguished organizations.

### 8. High Remuneration
- No specific evidence of commanded high salary or other remuneration is listed.

**Assessment**: **Low**. No evidence provided in the CV fits this criterion.

### Overall Rating: **Medium**
Juan Garcia shows substantial evidence in several key areas, such as original contributions, scholarly articles, and critical employment. However, the lack of evidence in other criteria like membership, press, judging, and high remuneration limits the overall assessment. To improve his qualification rating, additional documentation and achievements in the weaker criteria would be beneficial.

### Summary of Criteria Met:
- **Awards**: Fulbright Scholarship, Flag Honor Guard Member
- **Original Contribution**: Notable research projects on seismic force resistance and assessments
- **Scholarly Articles**: Multiple publications in journals and conference presentations
- **Critical Employment**: Key roles in significant engineering projects


# Dependencies
- pdf2image
- pillow


## License
This project is licensed under the MIT License - see the LICENSE file for details.

