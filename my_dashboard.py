#!pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

# Set the page title
st.set_page_config(page_title="Cerys's Dashboard",  # Title that appears on the browser tab
                   layout="centered")  # "wide" makes use of full browser width; alternative: "centered"

titanic = sns.load_dataset("titanic")

titanic_town_counts = titanic[['embark_town', 'survived']].groupby(
    'embark_town').agg(count=('survived', 'count'), survived_sum=('survived', 'sum')).reset_index()

#### SETTING UP DASHBOARD LAYOUT ####

# Title and description
# Displays a large title at the top of the app
st.title("Cerys's Awesome Dashboard")
# Displays a markdown text description
st.markdown(
    "This is a very rudimentary dashboard that uses Plotly plots. You can add additional text here...")

# Sidebar filters
# (1) Creates a multi-select dropdown to filter data based on category
category_filter = st.sidebar.multiselect(
    "Select Category",  # Label shown in sidebar
    # Unique categories from the dataset
    options=titanic_town_counts["embark_town"].unique(),
    default=titanic_town_counts["embark_town"].unique())  # Default selection includes all categories

# Filter the dataset based on sidebar inputs
filtered_data = titanic_town_counts[(titanic_town_counts["embark_town"].isin(
    category_filter))]  # Filters rows where category is in the selected list


#### PLOTS WITH PLOTLY ####

# Plot 1: bar chart to show the average value for each category
fig = px.bar(filtered_data, x="embark_town", y="count",color='survived_sum',title="Embark Town Distribution on Titanic")

# Display the bar chart with full width
st.plotly_chart(fig, theme="streamlit", use_container_width=True)


###### HOW TO RUN THE DASHBOARD? #####

# Open terminal (Mac users) or conda terminal (Windows users) and run:
# streamlit run "PATH TO FILE/FILE NAME.py"

# in case it does not work - try navigating to the folder in which your .py file is saved
# by running the following in the terminal
# cd /path/to/directory

# and then run
# streamlit run "PATH TO FILE/FILE NAME.py" or
# streamlit run FILE NAME.py in the terminal

#### HOW TO DEPLOY THE DASHBOARD ON STREAMLIT COMMUNITY CLOUD? ######

# How to deploy your streamlit dashboard/app to Streamlit community cloud?

# Note that you need to have a github and streamlit community cloud accounts for this type of deployment.

# 1. Open [streamlit github starter kit](https://github.com/streamlit/app-starter-kit) and click `Use this template` and then `Create a new repository`.

# 2. Set up the new github repository for the dashboard and create the repository.

# 3. Open (for edit) requirements.txt file and add names of Python packages that are necessary to run the dashboard in addition to streamlit (e.g., pandas, plotly, etc.). Commit changes.

# 4. Add `.py` file to the repo.

# 5. Go to [streamlit community cloud](https://streamlit.io/cloud) and sign in to your account + provide authorisation for streamlit to access your github account.

# 6. Click on `create app` in the top right corner and select `Deploy a public app from github` and fill in the information.

# Done! Now your dashboard is live.
