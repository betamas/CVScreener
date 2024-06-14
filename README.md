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
3. Install PyTorch with CUDA toolkit packaged:

    ```sh
    conda install anaconda::pillow==9.2.0 pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
    ```

4. Install Detectron2 (Windows):

    Follow the instructions [here](https://ivanpp.cc/detectron2-walkthrough-windows/#step3installdetectron2).

5. Install Layout Parser:

    Follow the instructions [here](https://layout-parser.readthedocs.io/en/latest/notes/installation.html).



## Run Application

To setup the backend service, in a separate shell run `python backend\qa_service.py`

With both services setup, you can ping `http://localhost:8001/` & start submitting queries!


### Dependencies
- unstructured
- dspy-ai
- qdrant-client[fastembed]
- onnx
- cudatoolkit
- torch
- pdf2image
- pillow
- charset-normalizer
- layoutparser
- detectron2


## License
This project is licensed under the MIT License - see the LICENSE file for details.

