# ADAS Sensor Event Analysis

This project analyzes Advanced Driver Assistance System (ADAS) sensor event data using Python. The analysis includes exploratory data analysis (EDA), visualization, and insights into sensor behavior and braking events. The processed data is saved for further use in dashboarding or advanced analysis.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dependencies](#dependencies)
- [Setup Guide](#setup-guide)
- [Usage](#usage)
- [Analysis Workflow](#analysis-workflow)
- [Results and Insights](#results-and-insights)
- [Future Work](#future-work)

---

## Project Overview

The **ADAS Sensor Event Analysis** project focuses on:
1. Exploring the distribution of vehicle speeds.
2. Analyzing the relationship between obstacle distances and brake application.
3. Investigating braking behavior when Vulnerable Road Users (VRUs) are detected.
4. Evaluating the confidence levels of the ADAS sensors.

The goal is to identify potential missed braking events and assess sensor reliability.

---

## Features

- **Exploratory Data Analysis (EDA)**: Visualizations of speed distribution, obstacle distances, braking behavior, and sensor confidence.
- **Missed Braking Insight**: Identifies scenarios where VRUs were detected but brakes were not applied.
- **Processed Data Output**: Saves the processed data for further use.

---

## Dependencies

This project requires the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

Install the required dependencies using the following command:

```bash
pip install pandas numpy matplotlib seaborn
```

---

## Setup Guide

1. Clone the repository or download the project files.
2. Ensure the dataset file `ADAS_Triage_Mock_Data.csv` is placed in the path: `C:/Users/ASUS/Documents/vscode/ADAS_Sensor_Event_Analysis/`.
3. Run the Python script to perform the analysis.

---

## Usage

1. Open the project in your preferred Python IDE or editor.
2. Run the script provided in `ADAS_Sensor_Event_Analysis.py`.
3. The script performs:
   - Visualization of sensor and vehicle data.
   - Insight generation for braking behavior.
   - Saves the processed file as `processed_adas_data.csv`.

---

## Analysis Workflow

1. **Load Dataset**:
   - The CSV file is loaded into a `pandas` DataFrame for processing.
2. **Basic Overview**:
   - Display the first few rows of the dataset, summary statistics, and column information.
3. **Exploratory Data Analysis**:
   - **Speed Distribution**: Histogram of vehicle speeds.
   - **Obstacle Distance vs Brake Signal**: Boxplot showing obstacle distances for brake application events.
   - **Brake Behavior When VRU Detected**: Stacked bar chart of brake behavior.
4. **Missed Braking Events**:
   - Identify instances where VRUs were detected but brakes were not applied.
5. **Sensor Confidence Analysis**:
   - Histogram of sensor confidence scores.
6. **Save Processed Data**:
   - Save the processed DataFrame as `processed_adas_data.csv` for further use.

---

## Results and Insights

### Key Findings:
- Distribution of vehicle speeds provides insights into driving patterns.
- Analysis of obstacle distances highlights the relationship between proximity and braking behavior.
- Braking behavior when VRUs are detected reveals potential safety gaps.
- Sensor confidence scores indicate the reliability of ADAS sensors.

### Identified Issues:
- **Missed Braking Events**: Instances where VRUs were detected but brakes were not applied. Number of such cases is printed during the analysis.

---

## Future Work

- Integrate the processed data into a dashboard for real-time monitoring.
- Perform advanced analytics, such as predictive modeling, on the dataset.
- Expand the analysis to include additional sensor parameters and scenarios.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author

**Monali0212**  
Feel free to reach out with questions or suggestions!
