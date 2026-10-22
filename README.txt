PYTHON AND MACHINE LEARNING LAB EXERCISES

This folder contains all 24 exercises. Exercises 1-12 and 15-22 are runnable Python programs. Exercises 13, 14, 23, and 24 require the named external platform and are provided as procedures. Sample datasets are identified as either built-in scikit-learn data or manually created demonstration data in each file.

SETUP
Python 3.10 or later is required because the math and statistics menu programs use match-case. Open PowerShell in this folder and install the dependencies used by the programs:

    py -m pip install numpy pandas matplotlib seaborn scikit-learn

If the Windows Python launcher is unavailable, use the equivalent command for your Python installation:

    python -m pip install numpy pandas matplotlib seaborn scikit-learn

Run an exercise with:

    py 01_math_library.py

Replace the filename with the program to run. Exercises 8, 9, 19, and 22 open chart windows; exercise 20 opens a feature-importance chart. Exercises 1-4 are menu driven; enter 0 to exit. Supervised learning programs request a new sample from the user. Built-in Iris data is included with scikit-learn and does not need a separate download. All other data is embedded in the program as small manually created examples; no local CSV is required.

EXERCISE INDEX
01 | Implement the functions using Math library | 01_math_library.py | Standard library
02 | Create and manipulate multidimensional arrays using NumPy | 02_numpy_arrays.py | numpy
03 | Perform statistical functions using Statistics library | 03_statistics_library.py | Standard library
04 | DataFrame implementation using Pandas | 04_pandas_dataframe.py | pandas
05 | Handling the missing values in a dataset | 05_missing_values.py | pandas
06 | Load a dataset and perform data analysis | 06_load_and_analyze_dataset.py | pandas, scikit-learn (built-in Iris)
07 | Load a dataset and display its structure with statistical summaries using Pandas | 07_pandas_structure_summary.py | pandas, scikit-learn (built-in Iris)
08 | Load a dataset and display its structure with graphs using Pandas and Matplotlib | 08_pandas_matplotlib_graphs.py | matplotlib, scikit-learn (built-in Iris)
09 | Perform Visualization using Seaborn | 09_seaborn_visualization.py | seaborn, matplotlib, scikit-learn (built-in Iris)
10 | Implementation of Covariance and Correlation | 10_covariance_correlation.py | pandas
11 | Perform Normalization in a given dataset | 11_normalization.py | pandas, scikit-learn
12 | Perform feature selection using Extra Trees Classifier | 12_extra_trees_feature_selection.py | scikit-learn (built-in Iris)
13 | Analyze the dataset using Julius AI | 13_julius_ai_procedure.txt | Julius AI account and internet; CSV sample described in procedure
14 | Analyze the dataset with dashboard using Bricks AI | 14_bricks_ai_dashboard_procedure.txt | Bricks AI account and internet; CSV sample described in procedure
15 | Perform feature extraction using Principal Component Analysis | 15_pca_feature_extraction.py | scikit-learn (built-in Iris)
16 | Implement KNN classification algorithm for an Iris dataset using scikit-learn | 16_knn_iris.py | scikit-learn (built-in Iris)
17 | Home Price Prediction using Linear Regression for error-based learning | 17_home_price_linear_regression.py | scikit-learn; embedded sample prices
18 | Perform SVM Classification using scikit-learn | 18_svm_classification.py | scikit-learn (built-in Iris)
19 | Implement Decision Tree algorithm for an elective dataset | 19_decision_tree_elective.py | matplotlib, scikit-learn; embedded sample elective data
20 | Implement Random Forest algorithm with customer churn dataset | 20_random_forest_customer_churn.py | pandas, matplotlib, scikit-learn; embedded sample churn data
21 | Perform Naïve Bayes Classification for loan dataset using scikit-learn | 21_naive_bayes_loan.py | scikit-learn; embedded sample loan data
22 | Customer Segmentation based on Annual Income using K-means algorithm | 22_kmeans_customer_segmentation.py | matplotlib, scikit-learn; embedded sample customer data
23 | Perform E-mail Classification using Levity | 23_levity_email_classification_procedure.txt | Levity account/workspace; connected test inbox or enabled workflow required
24 | Implementation of Image Classification using Teachable Machine | 24_teachable_machine_image_classification_procedure.txt | Teachable Machine website; user-provided image samples or webcam

SAMPLE OUTPUTS
01: Selecting 3 and entering 5 displays “Factorial: 120”.
02: Displays 1D/2D/3D arrays and lets the user enter a matrix for transpose, summaries, update, slicing, and matrix addition/subtraction.
03: Entering “1 3 5” and selecting mean displays “Mean: 3”.
04: Displays the initial student DataFrame, selected Name column, and a modified table.
05: Displays missing counts, complete rows after dropna, and mean-filled numeric values.
06: Displays Iris rows, 5 columns, types, numeric statistics, and species counts.
07: Displays Iris head and tail, shape (150, 5), metadata, numerical and categorical summaries.
08: Opens an Iris sepal-length histogram, species-count bar chart, and sepal/petal scatter plot.
09: Opens Iris scatter, histogram, and species box-plot charts.
10: Displays covariance and correlation matrices for StudyHours, PracticeTests, and Score.
11: Displays original Age/Income, Min-Max values from 0 to 1, and standardized values.
12: Prints the Extra Trees importance score for each Iris feature and the top two names.
13: Expected platform output: uploaded-file statistics, missing-value counts, analysis, and requested chart; generated only when run by a student.
14: Expected platform output: dashboard metrics, charts, and filters based on the imported sales CSV; generated only when run by a student.
15: Displays Iris feature names and shape, transformed rows, explained variance ratios, and total variance explained.
16: Displays test accuracy and predicted Iris species for four user-entered measurements.
17: Displays MAE/MSE and a predicted price in thousands of dollars for entered area and bedrooms.
18: Displays test accuracy and predicted Iris species for four user-entered measurements.
19: Displays test accuracy, readable tree rules, a decision-tree diagram, and a predicted elective for entered interest and mark.
20: Displays test accuracy, classification report, confusion matrix, top feature importances, and predicted churn class.
21: Displays test accuracy and predicted approval class (Approved/Rejected) for categorical inputs.
22: Opens an elbow-method chart, then displays sample cluster assignments, centers, and the cluster assigned to a new customer.
23: Expected platform output: a test email receives a configured label such as Track and Trace; requires the Levity workspace flow.
24: Expected platform output: tested images display a predicted class and confidence scores; requires user training.

CHECKING
The platform procedures cannot be run here because they require external accounts, user data, and/or camera/image inputs. No external platform action or model training is claimed. Python execution and dependency availability depend on the local Python installation.
