# Legislative Text Analytics for Financial Technology (FinTech) 🏛️📊

## Project Overview

**Legislative Text Analytics for Financial Technology (FinTech)** uses the LegiScan API to collect and analyze state legislative data related to financial technology, consumer finance, and financial regulation.

The current pipeline identifies active legislative sessions, retrieves legislative bills, and filters potential FinTech-related legislation using keyword matching. Areas of interest include consumer credit, lending regulation, and emerging financial products.

It demonstrates the full workflow of legislative data collection and analysis: querying legislative sessions, retrieving bill metadata, filtering relevant legislation, generating bill URLs, and preparing legislative data for future NLP applications. The repository is organized for clarity and reproducibility with commented code, modular functions, and API-based data retrieval.

* **Attribution:** Legislative metadata is provided through the LegiScan API.
* **Source:** Data is retrieved from LegiScan legislative datasets and state legislative records.
* **Purpose:** Personal, educational, and non-commercial research use only.
* **Future Development:** Planned enhancements include bill text retrieval, named entity recognition (NER), topic modeling, policy classification, and cross-state legislative analysis.

*Note: This repository does not redistribute legislative datasets. It only provides scripts that interact with the LegiScan API and analyze publicly accessible legislative metadata.*

---

## Installation

### 1. Clone the repository

git clone https://github.com/amythnn/legislative-text-analytics.git

cd legislative-text-analytics

### 2. (Optional) Create a virtual environment

python -m venv .venv

source .venv/bin/activate    # Windows: .venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

---

## API Setup

Create a file named:

keys.py

Add your LegiScan API key:

legiscan_key = "YOUR_API_KEY"

The keys.py file should never be committed to GitHub.

---

## Usage

Run the pipeline:

python legislative_text_analytics.py

Example configuration:

STATE = "CA"

The pipeline will:

* Identify the current legislative session
* Retrieve legislative bills for the selected state
* Display recent bills and metadata
* Identify potential FinTech and consumer finance legislation
* Display matched bills and triggering keywords

Outputs include:

* Current legislative session information
* Retrieved bill metadata
* Potential FinTech-related bills
* Direct URLs to legislative records

---

## Technologies

* Python
* Requests
* JSON
* LegiScan API
* Policy Analytics
* Legislative Data
* Natural Language Processing (planned)

---

## Future Research Directions

Potential research applications include:

* Consumer credit and lending policy
* Financial inclusion initiatives
* State-level FinTech regulation
* Financial regulation and public policy research

---

## Licensing and Attribution

* **Code:** All original code in this repository is licensed under the MIT License.
* **Data & Attribution:** Legislative metadata is retrieved through the LegiScan API and remains subject to LegiScan's applicable terms of service, licensing requirements, and usage restrictions.

  * Users are responsible for complying with LegiScan licensing requirements.
  * This repository does not redistribute legislative datasets.
  * This repository is intended for personal, educational, and non-commercial research purposes only.
