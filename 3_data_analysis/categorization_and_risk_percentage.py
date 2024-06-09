#import needed library
import pandas as pd

df = pd.read_csv('Heart.csv')

def categorize_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 25:
        return 'Normal weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

# Function to categorize blood pressure
def categorize_blood_pressure(bp):
    if bp < 120:
        return 'Normal'
    elif 120 <= bp < 130:
        return 'Elevated'
    elif 130 <= bp < 140:
        return 'High BP (Stage 1)'
    else:
        return 'High BP (Stage 2)'

df['BMI_Category'] = df['BMI'].apply(categorize_bmi)
df['BP_Category'] = df['ap_hi'].apply(categorize_blood_pressure)

bmi_categories = df['BMI_Category'].unique()
bp_categories = df['BP_Category'].unique()
cholesterol_levels = df['cholesterol'].unique()

def calculate_heart_disease_percentage(df, bmi_category, bp_category, cholesterol_level):
    # Filter the dataset based on the input categories
    filtered_df = df[(df['BMI_Category'] == bmi_category) & 
                     (df['BP_Category'] == bp_category) & 
                     (df['cholesterol'] == cholesterol_level)]
    
    # Count the number of individuals with heart disease
    heart_disease_count = filtered_df[filtered_df['cardio'] == 1].shape[0]
    
    # Count the total number of individuals in the filtered dataset
    total_count = filtered_df.shape[0]
    
    # Calculate the percentage
    if total_count == 0:
        return 0
    else:
        percentage = (heart_disease_count / total_count) * 100
        return percentage

# Create a DataFrame to store the results
results = []

# Iterate over all combinations of BMI categories, blood pressure categories, and cholesterol levels
for bmi_category in bmi_categories:
    for bp_category in bp_categories:
        for cholesterol_level in cholesterol_levels:
            percentage = calculate_heart_disease_percentage(df, bmi_category, bp_category, cholesterol_level)
            results.append({
                'BMI_Category': bmi_category,
                'BP_Category': bp_category,
                'Cholesterol_Level': cholesterol_level,
                'Heart_Disease_Percentage': percentage
            })

results_df = pd.DataFrame(results)

#save the results to a CSV file
results_df.to_csv('heart_disease_percentages.csv', index=False)
