# Simple Data Dashboard 📊

This is a simple data dashboard application built with [Streamlit](https://streamlit.io/), allowing users to upload CSV files, filter the data, and generate visualizations with ease.

## Features 🚀

- **Upload CSV files** 📂: Upload your CSV data to explore and visualize.![1](https://github.com/user-attachments/assets/5efdf434-9d86-4895-91e2-88deae13c7ef)

- **Data Preview** 👀: View the first few rows of the uploaded dataset.
- **Data Summary** 📋: Get a quick statistical summary of the data.
- **Filter Data** 🔍: Filter your data by selecting specific columns and values.
- **Plot Data** 📈: Generate interactive line plots for visualizing the relationship between columns.

## Getting Started 🛠️

### Prerequisites

Make sure you have Python installed. You can download it [here](https://www.python.org/downloads/).

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/simple-data-dashboard.git
    cd simple-data-dashboard
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Once you have the dependencies installed, run the app with Streamlit:

```bash
streamlit run app.py
```

This will launch the dashboard in your default web browser.

## Application Overview 

### Upload CSV File

 - Click on the "Browse files" button to upload your CSV file.

### Data Preview

- After uploading, the first few rows of the dataset will be displayed.

### Data Summary

- View the statistical summary of the dataset, including mean, median, min, max, etc.

### Filter Data

- Select a column and filter the dataset by unique values in that column.

### Plot Data

- Choose columns for the x-axis and y-axis to generate a line plot.
- Click on "Generate Plot" to visualize your filtered data.

## Project Structure 📂

```bash
simple-data-dashboard/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## Dependencies 📦

The following packages are required to run the application:

- Streamlit
- Pandas
- Matplotlib
- openpyxl

Install them using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

## Example Use Case 🎯

1. Upload a CSV file containing your dataset.
2. Filter the data by selecting specific columns and values.
3. Visualize the filtered data with a line plot by choosing appropriate columns for the x-axis and y-axis.

## Screenshots 🖼️

Here’s a screenshot of the dashboard interface:

![1](https://github.com/user-attachments/assets/25615d77-74e7-4da9-ba5d-911dfbacc81e)
![2](https://github.com/user-attachments/assets/5a34f510-ef44-49c1-bacd-6d41eb3a8b5c)
![3](https://github.com/user-attachments/assets/5a4cba9d-3969-44b6-9cd5-972e7d90ae31)
![4](https://github.com/user-attachments/assets/af85f0c4-e95f-48d9-9c81-320a58310f40)

## Contributing 👥

Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or find a bug.

