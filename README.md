# College Distance Dataset Analysis and Model Training

This project includes data processing and predictive modeling workflows for the College Distance dataset, targeting the prediction of the `score` variable. The project is divided into two main parts: Data Analysis and Model Training.

## Part 1: Data Analysis and Transformation

### Overview
Exploratory Data Analysis (EDA) and data cleaning tasks for preparing the College Distance dataset.

### Key Steps
1. **Data Exploration**: Initial data inspection with null checks, statistical summaries, and unique value counts.
2. **Visualizations**:
   - Bar plots for `education`, `tuition`, and `wage`.
   - Histogram of `score`.
3. **Statistical Analysis**:
   - Calculated skewness and kurtosis for numeric columns.
   - Correlation matrix to explore relationships.
4. **Categorical Encoding**:
   - Ordinal encoding for categorical columns; dictionary saved for mappings.
5. **Save Processed Data**:
   - Cleaned data: `CollegeDistanceCleaned.csv`.
   - Encoder: `ordinal_encoder.pkl`.

## Part 2: Model Training and Evaluation

### Overview
Regression models to predict `score` using Decision Tree, Random Forest, Linear Regression, and Gradient Boosting.

### Key Steps
1. **Data Preparation**:
   - Split data (80-20) for training and testing.
2. **Model Training**:
   - **Decision Tree**: Adjusted depths and criteria.
   - **Random Forest**: Tuned tree count and depth.
   - **Linear Regression**: Baseline linear model.
   - **Gradient Boosting**: Tested various parameters; feature selection refined.
3. **Evaluation Metrics**:
   - Used MAE, MSE, R², and custom accuracy for evaluation.
4. **Hyperparameter Tuning**:
   - Optimized Gradient Boosting with `RandomizedSearchCV`.

### Best Results
- **Gradient Boosting**:
  - MAE: 5.64, MSE: 48.19, R²: 0.36
  - Accuracy within ±10%: 51.05%

## Summary
The Gradient Boosting model outperformed other models, achieving the highest accuracy and lowest error rates.
