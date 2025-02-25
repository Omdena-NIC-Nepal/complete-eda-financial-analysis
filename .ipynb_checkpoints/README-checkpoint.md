[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MFpQQ_l2)
﻿
# EDA_Assignment

# Climate Data Exploratory Data Analysis Assignment

## Overview
In this assignment, you will perform a comprehensive Exploratory Data Analysis (EDA) on a climate dataset containing information from 1900 to 2023. The dataset includes variables such as global temperatures, CO2 concentration, sea level rise, and Arctic ice area.

## Objectives
- Process and clean the provided climate data
- Aggregate the data by year to create a 124-year time series
- Perform univariate analysis on each climate variable
- Conduct bivariate analysis to explore relationships between variables
- Explore multivariate patterns in the climate data
- Create clear, informative visualizations using Matplotlib and Seaborn
- Draw meaningful conclusions from your analysis

## Requirements

### 1. Data Preparation (15 points)
- Load the provided Climate_Change_Indicators.csv file
- Clean any missing or inconsistent values (Basically none in this case, but check to be sure)
- Aggregate the data by year, computing the average for each climate variable

### 2. Univariate Analysis (25 points)
For each climate variable (Global Temperature, CO2 Concentration, Sea Level Rise, Arctic Ice Area):
- Calculate descriptive statistics (mean, median, range, std deviation, etc.)
- Create appropriate visualizations (histograms, box plots, time series plots)
- Identify and discuss trends, outliers, and distributions (Your discussion is to be done in the notebook)

### 3. Bivariate Analysis (25 points)
- Create scatter plots exploring relationships between pairs of variables
- Calculate and interpret correlation coefficients
- Analyze how variables change in relation to each other over time
- Create at least one pair plot or correlation heatmap

### 4. Multivariate Analysis (20 points)
- Explore relationships among three or more variables
- Create advanced visualizations (e.g., 3D plots, animated plots, or multiple small multiples) - Not covered in class but make sure to research how to create this. 
- Discuss complex patterns and interactions between climate indicators

### 5. Conclusions and Insights (15 points)
- Summarize key findings from your analysis
- Discuss potential implications of the observed trends
- Suggest areas for further investigation

## Technical Requirements
- Use Python libraries: Pandas, NumPy, Matplotlib, and Seaborn
- Complete all work in the provided Jupyter notebook (climate_eda.ipynb)
- Include clear markdown explanations with your code and visualizations
- Follow best practices for code organization and documentation (Make sure to have documentation as discussed earlier)

## Submission
Submit your completed Jupyter notebook by pushing your changes to this GitHub repository. The automated tests will verify that you've completed all required components of the analysis.

## Grading
Your assignment will be automatically graded based on:
- Completion of all required analyses (univariate, bivariate, multivariate)
- Proper use of required libraries
- Quality and variety of visualizations
- Correct aggregation of data by year
- Presence of meaningful interpretations and conclusions

Good luck!