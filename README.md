# ProjectSDT Software Development Tools: 
This project aims to provide additional practice on common software engineering SPRINT 4

it’s time to apply the knowledge and skills you’ve acquired to a project: building and deploying a web application dashboard to a cloud service.

### Step 1. Getting started

- Create an account on github.com.
- Create a new git repository with a README.md file and a .gitignore file (choose a Python template).
- Make a new Python environment. Install the following packages: pandas, streamlit, plotly.express, and altair. Feel free to install more packages if you want to implement additional features in your web app.
- Create an account on render.com and link it to your GitHub account.
- Use git to clone your new project’s git repository to your local machine. From now on, you’ll be working on the project on your local machine, and then committing and pushing the changes back to the GitHub repository.
- Install VS Code and load the project into VS Code (by opening the project directory with VS Code).

### Step 2. Download the data file

- Download the car advertisement dataset (vehicles_us.csv) or find your own dataset in a CSV format.
- Place the dataset in the root directory of the project.

### Step 3. Exploratory Data Analysis

- Create an EDA.ipynb Jupyter notebook in VS Code.
- Save the notebook in the notebooks directory of your project.
- Perform some basic exploratory analysis of the dataset in the notebook.
- Create a couple of histograms and scatterplots using plotly-express library.

### Step 4. Develop the web application dashboard

- Create an app.py file in the root of the project’s directory. The following steps (2-4) will require you to write code into this app.py file.
- In the app.py file, import streamlit, pandas, and plotly.express.
- Read the dataset’s CSV file into a Pandas DataFrame.
- From the Jupyter notebook, create and/or copy:
at least one st.header with text
at least one Plotly Express histogram using st.write or st.plotly_chart
at least one Plotly Express scatter plot using st.write or st.plotly_chart
at least one checkbox using st.checkbox that changes the behavior of any of the above components.
- Your project will only build on the online service if all project files are present in your GitHub repository. Therefore, you must commit and push each new file change to your repository as soon as you’ve completed it.

### Step 5. Deploy the application to Render

- To make Streamlit compatible with Render, we need to create two new files: requirements.txt and .streamlit/config.toml.
- First, we need to create the requirements.txt file. Create this new file in your project folder’s root level. Then, add your project’s required packages. 
- Second, we need to add the configuration file to your git repository. Create the .streamlit directory, then add the config.toml file there (this can all be done with the right-click menu in the left-hand tab of VS Code).