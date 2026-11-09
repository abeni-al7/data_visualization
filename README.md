# ESBL Case Visualization

An exploratory data-analysis script that cleans an ESBL (antibiotic-resistance) case dataset and renders a multi-panel dashboard of charts.

## Features

- Loads `ESBL_cases.csv`, parsing dates and cleaning age, gender, pathogen, and ESBL-type fields
- Builds a figure with plots for daily cases, age and gender distribution, top pathogens, ESBL-type positivity, SME categories, and ESBL-CARBA cases over time
- Available as both a plain script (`data_viz.py`) and a Jupyter notebook (`data_viz.ipynb`)

## Built with

- Python 3
- pandas
- matplotlib

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install pandas matplotlib
python data_viz.py
```

Or open `data_viz.ipynb` in Jupyter. A CSV named `ESBL_cases.csv` must be present in the working directory (it is git-ignored and not included).
