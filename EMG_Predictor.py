#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import re
import math
import numpy as np

file_path = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personal/index_finger_motion_raw.csv'
df = pd.read_csv(file_path)
headers = df.columns
print(headers)


# In[251]:


def calculate_and_save_zero_crossings(input_directory, threshold):
    # Function for zero-crossing calculation
    def zero_crossing(row, threshold):
        N = len(row)
        ZC = 0  # counter for zero crossing
        for i in range(N - 1):
            if ((row[i] > 0 and row[i + 1] < 0) or (row[i] < 0 and row[i + 1] > 0)) and (abs(row[i] - row[i + 1])) >= threshold:
                ZC += 1
        return ZC

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate zero crossings
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate zero crossings for each row
        df['zero_crossings'] = df.iloc[:, :150].apply(lambda row: zero_crossing(row, threshold), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated zero crossings as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_zero_crossing'] = df['zero_crossings']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../zero_crossing_results')
    print(output_directory)
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_zero_crossings_result.csv'
    print(output_filename)
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/zero_crossing_results', output_filename)
    print(output_file_path)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Zero crossings calculated and saved successfully.")


parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform zero-crossing calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_zero_crossings(input_directory, threshold=0.01)


# In[252]:


def calculate_and_save__standard_deviations(input_directory):
    # Function for _standard_deviation calculation
    def standard_deviation(X):
        N = len(X)
        mean = statistics.mean(X)
        return math.sqrt((1/N) * np.sum([(x - mean)**2 for x in X]))

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = [int(re.search(r'\d+', file).group()) for file in csv_files]
    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate standard_deviations
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate standard_deviation for each row
        df['standard_deviations'] = df.iloc[:, :150].apply(lambda row: standard_deviation(row), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated standard_deviations as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_standard_deviation'] = df['standard_deviations']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../standard_deviation_results')
    print(output_directory)
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_standard_deviation_results.csv'
    print(output_filename)
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/standard_deviation_results', output_filename)
    print(output_file_path)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Standard deviations calculated and saved successfully.")

parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform standard deviations calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save__standard_deviations(input_directory)


# In[253]:


def calculate_and_save_root_mean_square(input_directory):
    # Function for root mean square calculation
    def root_mean_square(X):
        return math.sqrt(np.mean(np.square(X)))

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate root mean square values
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate root mean square for each row
        df['root_mean_square'] = df.iloc[:, :150].apply(lambda row: root_mean_square(row), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated root mean square values as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_root_mean_square'] = df['root_mean_square']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../root_mean_square_results')
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_root_mean_square_results.csv'
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/root_mean_square_results', output_filename)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Root mean square values calculated and saved successfully.")

# Example usage
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform root mean square calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_root_mean_square(input_directory)


# In[254]:


def calculate_and_save_mean_absolute_value(input_directory):
    # Function for mean absolute value calculation
    def mean_absolute_value(X):
        return np.sum(X) / len(X)

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate mean absolute values
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate mean absolute value for each row
        df['mean_absolute_value'] = df.iloc[:, :150].apply(lambda row: mean_absolute_value(row), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated mean absolute values as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_mean_absolute_value'] = df['mean_absolute_value']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../mean_absolute_value_results')
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_mean_absolute_value_results.csv'
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/mean_absolute_value_results', output_filename)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Mean absolute values calculated and saved successfully.")

# Example usage
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform mean absolute value calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_mean_absolute_value(input_directory)


# In[255]:


def calculate_and_save_modified_mean_absolute_value_1(input_directory):
    # Function for modified mean absolute value calculation
    def modified_mean_absolute_value_1(X):
        N = len(X)
        sum = 0
        for i in range(len(X)):
            w = 0.5
            if 0.25 * N <= i <= 0.75 * N:
                w = 1
            sum += w * abs(X[i])
        return sum / N

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate modified mean absolute values
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate modified mean absolute value for each row
        df['modified_mean_absolute_value_1'] = df.iloc[:, :150].apply(lambda row: modified_mean_absolute_value_1(row), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated modified mean absolute values as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_modified_mean_absolute_value_1'] = df['modified_mean_absolute_value_1']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../modified_mean_absolute_value_1_results')
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_modified_mean_absolute_value_1_results.csv'
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/modified_mean_absolute_value_1_results', output_filename)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Modified mean absolute values (Method 1) calculated and saved successfully.")

# Example usage
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform modified mean absolute value (Method 1) calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_modified_mean_absolute_value_1(input_directory)


# In[256]:


def calculate_and_save_modified_mean_absolute_value_2(input_directory):
    # Function for modified mean absolute value calculation
    def modified_mean_absolute_value_2(X):
        sum = 0
        N = len(X)
        for i in range(len(X)):
            w = 1
            if i < 0.25 * N:
                w = (4 * i) / N
            elif i > 0.75 * N:
                w = 4 * (i - N) / N
            sum += w * abs(X[i])
        return sum / N

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate modified mean absolute values
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate modified mean absolute value for each row
        df['modified_mean_absolute_value_2'] = df.iloc[:, :150].apply(lambda row: modified_mean_absolute_value_2(row), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated modified mean absolute values as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_modified_mean_absolute_value_2'] = df['modified_mean_absolute_value_2']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../modified_mean_absolute_value_2_results')
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_modified_mean_absolute_value_2_results.csv'
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/modified_mean_absolute_value_2_results', output_filename)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Modified mean absolute values (Method 2) calculated and saved successfully.")

# Example usage
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform modified mean absolute value (Method 2) calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_modified_mean_absolute_value_2(input_directory)


# In[257]:


def calculate_and_save_simple_square_integral(input_directory):
    # Function for simple square integral calculation
    def simple_square_integral(X):
        total = 0
        for i in range(len(X)):
            total = total + (X[i]**2)
        return total

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate simple square integrals
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate simple square integral for each row
        df['simple_square_integral'] = df.iloc[:, :150].apply(lambda row: simple_square_integral(row), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated simple square integrals as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_simple_square_integral'] = df['simple_square_integral']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../simple_square_integral_results')
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_simple_square_integral_results.csv'
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/simple_square_integral_results', output_filename)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Simple square integrals calculated and saved successfully.")

# Example usage
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform simple square integral calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_simple_square_integral(input_directory)


# In[258]:


def calculate_and_save_average_amplitude_change(input_directory):
    # Function for average amplitude change calculation
    def average_amplitude_change(X):
        total = 0
        for i in range(len(X) - 1):
            diff = abs(X[i + 1] - X[i])
            total = total + diff
        return total / len(X)

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate average amplitude changes
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate average amplitude change for each row
        df['average_amplitude_change'] = df.iloc[:, :150].apply(lambda row: average_amplitude_change(row), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated average amplitude changes as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_average_amplitude_change'] = df['average_amplitude_change']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../average_amplitude_change_results')
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_average_amplitude_change_results.csv'
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/average_amplitude_change_results', output_filename)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Average amplitude changes calculated and saved successfully.")

# Example usage
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform average amplitude change calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_average_amplitude_change(input_directory)


# In[259]:


def calculate_and_save_waveform_length(input_directory):
    # Function for waveform length calculation
    def waveform_length(X):
        sum = 0
        for i in range(len(X) - 1):
            sum += abs(X[i + 1] - X[i])
        return sum

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate waveform lengths
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate waveform length for each row
        df['waveform_length'] = df.iloc[:, :150].apply(lambda row: waveform_length(row), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated waveform lengths as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_waveform_length'] = df['waveform_length']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../waveform_length_results')
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_waveform_length_results.csv'
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/waveform_length_results', output_filename)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Waveform lengths calculated and saved successfully.")

# Example usage
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform waveform length calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_waveform_length(input_directory)


# In[260]:


def calculate_and_save_willison_amplitude(input_directory, threshold=0.05):
    # Function for willison amplitude calculation
    def willison_amplitude(X, threshold=0.05):
        total = 0
        newArray = np.diff(X)
        for val in newArray:
            if np.absolute(val) >= threshold:
                total = total + 1
        return total

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate willison amplitudes
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate willison amplitude for each row
        df['willison_amplitude'] = df.iloc[:, :150].apply(lambda row: willison_amplitude(row, threshold), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated willison amplitudes as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_willison_amplitude'] = df['willison_amplitude']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../willison_amplitude_results')
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_willison_amplitude_results.csv'
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/willison_amplitude_results', output_filename)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Willison amplitudes calculated and saved successfully.")

# Example usage
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform willison amplitude calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_willison_amplitude(input_directory, threshold=0.05)


# In[261]:


def calculate_and_save_slope_sign_change(input_directory, threshold):
    # Function for slope sign change calculation
    def slope_sign_change(X, thresh):
        L = len(X)
        SSC = 0
        for i in range(1, L - 1):
            if (((X[i] > X[i - 1] and X[i] > X[i + 1]) or (X[i] < X[i - 1] and X[i] < X[i + 1]))
                    and (((abs(X[i] - X[i + 1])) >= thresh) or (abs(X[i] - X[i - 1]) >= thresh))):
                SSC += 1
        return SSC

    # Get a list of all CSV files in the input directory
    csv_files = [file for file in os.listdir(input_directory) if file.endswith('.csv')]

    # Extract numbers from CSV filenames
    file_numbers = []
    for file in csv_files:
        match = re.search(r'\d+', file)
        if match:
            file_numbers.append(int(match.group()))
        else:
            print(f"Warning: File '{file}' does not match naming pattern.")

    sorted_indices = sorted(range(len(file_numbers)), key=lambda k: file_numbers[k])

    # Create an empty DataFrame to store the results
    result_df = pd.DataFrame()

    # Iterate through each CSV file and calculate slope sign changes
    for index in sorted_indices:
        csv_file = csv_files[index]
        input_file_path = os.path.join(input_directory, csv_file)
        df = pd.read_csv(input_file_path)

        # Calculate slope sign change for each row
        df['slope_sign_change'] = df.iloc[:, :150].apply(lambda row: slope_sign_change(row, threshold), axis=1)

        # Extract electrode number from filename
        electrode_number = re.search(r'\d+', csv_file).group()

        # Add the calculated slope sign changes as a column in the result DataFrame
        result_df[f'electrode_{electrode_number}_slope_sign_change'] = df['slope_sign_change']

    # Determine the output directory and filename
    output_directory = os.path.join(input_directory, '../slope_sign_change_results')
    
    last_folder_name = os.path.basename(os.path.normpath(input_directory))
    output_filename = f'{last_folder_name}_slope_sign_change_results.csv'
    output_file_path = os.path.join('/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/slope_sign_change_results', output_filename)
    
    # Save the result DataFrame to the output file
    result_df.to_csv(output_file_path, index=False)

    print("Slope sign changes calculated and saved successfully.")

# Example usage
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/raw_emg_data_cropped_and_arranged'

# List of subdirectories within the parent directory
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

# Loop through each subdirectory and perform slope sign change calculations
for subdirectory in subdirectories:
    input_directory = os.path.join(parent_directory, subdirectory)
    calculate_and_save_slope_sign_change(input_directory, threshold= 2)


# In[263]:


# Define the parent directory
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2'

# Get the list of subdirectories
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d)) and d != 'raw_emg_data_cropped_and_arranged']

# Define the order of feature folders
feature_folders = [
    'standard_deviation_results',
    'root_mean_square_results',
    'modified_mean_absolute_value_1_results',
    'modified_mean_absolute_value_2_results',
    'zero_crossing_results',
    'average_amplitude_change_results',
    'slope_sign_change_results',
    'mean_absolute_value_results',
    'waveform_length_results',
    'willison_amplitude_results',
    'simple_square_integral_results'
]

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Iterate through each feature folder
for feature_folder in feature_folders:
    feature_folder_path = os.path.join(parent_directory, feature_folder)
    
    # Get the list of CSV files in the feature folder
    csv_files = [file for file in os.listdir(feature_folder_path) if file.startswith('index_finger') and file.endswith('.csv')]
    
    # Iterate through each CSV file in the feature folder
    for csv_file in csv_files:
        csv_file_path = os.path.join(feature_folder_path, csv_file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Add the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], axis=1)

# Add the classification column
combined_df['classification'] = 1

# Save the combined DataFrame to a CSV file
output_filename = 'index_finger_gestures.csv'
output_directory = os.path.join(parent_directory, 'hand_gestures')
os.makedirs(output_directory, exist_ok=True)
output_file_path = os.path.join(output_directory, output_filename)
combined_df.to_csv(output_file_path, index=False)


# In[262]:


# Define the parent directory
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2'

# Get the list of subdirectories
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d)) and d != 'raw_emg_data_cropped_and_arranged']

# Define the order of feature folders
feature_folders = [
    'standard_deviation_results',
    'root_mean_square_results',
    'modified_mean_absolute_value_1_results',
    'modified_mean_absolute_value_2_results',
    'zero_crossing_results',
    'average_amplitude_change_results',
    'slope_sign_change_results',
    'mean_absolute_value_results',
    'waveform_length_results',
    'willison_amplitude_results',
    'simple_square_integral_results'
]

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Iterate through each feature folder
for feature_folder in feature_folders:
    feature_folder_path = os.path.join(parent_directory, feature_folder)
    
    # Get the list of CSV files in the feature folder
    csv_files = [file for file in os.listdir(feature_folder_path) if file.startswith('middle_finger') and file.endswith('.csv')]
    
    # Iterate through each CSV file in the feature folder
    for csv_file in csv_files:
        csv_file_path = os.path.join(feature_folder_path, csv_file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Add the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], axis=1)

# Add the classification column
combined_df['classification'] = 2

# Save the combined DataFrame to a CSV file
output_filename = 'middle_finger_gestures.csv'
output_directory = os.path.join(parent_directory, 'hand_gestures')
os.makedirs(output_directory, exist_ok=True)
output_file_path = os.path.join(output_directory, output_filename)
combined_df.to_csv(output_file_path, index=False)


# In[264]:


# Define the parent directory
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2'

# Get the list of subdirectories
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d)) and d != 'raw_emg_data_cropped_and_arranged']

# Define the order of feature folders
feature_folders = [
    'standard_deviation_results',
    'root_mean_square_results',
    'modified_mean_absolute_value_1_results',
    'modified_mean_absolute_value_2_results',
    'zero_crossing_results',
    'average_amplitude_change_results',
    'slope_sign_change_results',
    'mean_absolute_value_results',
    'waveform_length_results',
    'willison_amplitude_results',
    'simple_square_integral_results'
]

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Iterate through each feature folder
for feature_folder in feature_folders:
    feature_folder_path = os.path.join(parent_directory, feature_folder)
    
    # Get the list of CSV files in the feature folder
    csv_files = [file for file in os.listdir(feature_folder_path) if file.startswith('ring_finger') and file.endswith('.csv')]
    
    # Iterate through each CSV file in the feature folder
    for csv_file in csv_files:
        csv_file_path = os.path.join(feature_folder_path, csv_file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Add the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], axis=1)

# Add the classification column
combined_df['classification'] = 3

# Save the combined DataFrame to a CSV file
output_filename = 'ring_finger_gestures.csv'
output_directory = os.path.join(parent_directory, 'hand_gestures')
os.makedirs(output_directory, exist_ok=True)
output_file_path = os.path.join(output_directory, output_filename)
combined_df.to_csv(output_file_path, index=False)


# In[265]:


# Define the parent directory
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2'

# Get the list of subdirectories
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d)) and d != 'raw_emg_data_cropped_and_arranged']

# Define the order of feature folders
feature_folders = [
    'standard_deviation_results',
    'root_mean_square_results',
    'modified_mean_absolute_value_1_results',
    'modified_mean_absolute_value_2_results',
    'zero_crossing_results',
    'average_amplitude_change_results',
    'slope_sign_change_results',
    'mean_absolute_value_results',
    'waveform_length_results',
    'willison_amplitude_results',
    'simple_square_integral_results'
]

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Iterate through each feature folder
for feature_folder in feature_folders:
    feature_folder_path = os.path.join(parent_directory, feature_folder)
    
    # Get the list of CSV files in the feature folder
    csv_files = [file for file in os.listdir(feature_folder_path) if file.startswith('little_finger') and file.endswith('.csv')]
    
    # Iterate through each CSV file in the feature folder
    for csv_file in csv_files:
        csv_file_path = os.path.join(feature_folder_path, csv_file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Add the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], axis=1)

# Add the classification column
combined_df['classification'] = 4

# Save the combined DataFrame to a CSV file
output_filename = 'little_finger_gestures.csv'
output_directory = os.path.join(parent_directory, 'hand_gestures')
os.makedirs(output_directory, exist_ok=True)
output_file_path = os.path.join(output_directory, output_filename)
combined_df.to_csv(output_file_path, index=False)


# In[266]:


# Define the parent directory
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2'

# Get the list of subdirectories
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d)) and d != 'raw_emg_data_cropped_and_arranged']

# Define the order of feature folders
feature_folders = [
    'standard_deviation_results',
    'root_mean_square_results',
    'modified_mean_absolute_value_1_results',
    'modified_mean_absolute_value_2_results',
    'zero_crossing_results',
    'average_amplitude_change_results',
    'slope_sign_change_results',
    'mean_absolute_value_results',
    'waveform_length_results',
    'willison_amplitude_results',
    'simple_square_integral_results'
]

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Iterate through each feature folder
for feature_folder in feature_folders:
    feature_folder_path = os.path.join(parent_directory, feature_folder)
    
    # Get the list of CSV files in the feature folder
    csv_files = [file for file in os.listdir(feature_folder_path) if file.startswith('thumb') and file.endswith('.csv')]
    
    # Iterate through each CSV file in the feature folder
    for csv_file in csv_files:
        csv_file_path = os.path.join(feature_folder_path, csv_file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Add the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], axis=1)

# Add the classification column
combined_df['classification'] = 5

# Save the combined DataFrame to a CSV file
output_filename = 'thumb_gestures.csv'
output_directory = os.path.join(parent_directory, 'hand_gestures')
os.makedirs(output_directory, exist_ok=True)
output_file_path = os.path.join(output_directory, output_filename)
combined_df.to_csv(output_file_path, index=False)


# In[267]:


# Define the parent directory
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2'

# Get the list of subdirectories
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d)) and d != 'raw_emg_data_cropped_and_arranged']

# Define the order of feature folders
feature_folders = [
    'standard_deviation_results',
    'root_mean_square_results',
    'modified_mean_absolute_value_1_results',
    'modified_mean_absolute_value_2_results',
    'zero_crossing_results',
    'average_amplitude_change_results',
    'slope_sign_change_results',
    'mean_absolute_value_results',
    'waveform_length_results',
    'willison_amplitude_results',
    'simple_square_integral_results'
]

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Iterate through each feature folder
for feature_folder in feature_folders:
    feature_folder_path = os.path.join(parent_directory, feature_folder)
    
    # Get the list of CSV files in the feature folder
    csv_files = [file for file in os.listdir(feature_folder_path) if file.startswith('rest') and file.endswith('.csv')]
    
    # Iterate through each CSV file in the feature folder
    for csv_file in csv_files:
        csv_file_path = os.path.join(feature_folder_path, csv_file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Add the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], axis=1)

# Add the classification column
combined_df['classification'] = 6

# Save the combined DataFrame to a CSV file
output_filename = 'rest_gestures.csv'
output_directory = os.path.join(parent_directory, 'hand_gestures')
os.makedirs(output_directory, exist_ok=True)
output_file_path = os.path.join(output_directory, output_filename)
combined_df.to_csv(output_file_path, index=False)


# In[268]:


# Define the parent directory
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2'

# Get the list of subdirectories
subdirectories = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d)) and d != 'raw_emg_data_cropped_and_arranged']

# Define the order of feature folders
feature_folders = [
    'standard_deviation_results',
    'root_mean_square_results',
    'modified_mean_absolute_value_1_results',
    'modified_mean_absolute_value_2_results',
    'zero_crossing_results',
    'average_amplitude_change_results',
    'slope_sign_change_results',
    'mean_absolute_value_results',
    'waveform_length_results',
    'willison_amplitude_results',
    'simple_square_integral_results'
]

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Iterate through each feature folder
for feature_folder in feature_folders:
    feature_folder_path = os.path.join(parent_directory, feature_folder)
    
    # Get the list of CSV files in the feature folder
    csv_files = [file for file in os.listdir(feature_folder_path) if file.startswith('victory_gesture') and file.endswith('.csv')]
    
    # Iterate through each CSV file in the feature folder
    for csv_file in csv_files:
        csv_file_path = os.path.join(feature_folder_path, csv_file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Add the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], axis=1)

# Add the classification column
combined_df['classification'] = 7

# Save the combined DataFrame to a CSV file
output_filename = 'victory_gesture_gestures.csv'
output_directory = os.path.join(parent_directory, 'hand_gestures')
os.makedirs(output_directory, exist_ok=True)
output_file_path = os.path.join(output_directory, output_filename)
combined_df.to_csv(output_file_path, index=False)


# In[269]:


import pandas as pd
import os

# Define the parent directory
parent_directory = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/hand_gestures'

# Define the order of CSV files
csv_file_order = [
    'index_finger_gestures.csv',
    'little_finger_gestures.csv',
    'middle_finger_gestures.csv',
    'rest_gestures.csv',
    'ring_finger_gestures.csv',
    'thumb_gestures.csv',
    'victory_gesture_gestures.csv'
]

# Read the first CSV file to initialize the combined DataFrame
combined_df = pd.read_csv(os.path.join(parent_directory, csv_file_order[0]))

# Iterate through the remaining CSV files in the specified order and append their data to the combined DataFrame
for csv_file in csv_file_order[1:]:
    df = pd.read_csv(os.path.join(parent_directory, csv_file))
    combined_df = combined_df.append(df, ignore_index=True)

# Save the combined DataFrame to a CSV file
output_file_name = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/hand_gestures.csv'
combined_df.to_csv(output_file_name, index=False)

print("Combined CSV file created and saved successfully.")


# In[270]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

# Load the dataset
dataset_path = '/Users/rishimachanpalli/RishiSoftwareEMGAnalysis/personalV2/hand_gestures.csv'
df = pd.read_csv(dataset_path)

# Split dataset into features (X) and labels (y)
X = df.drop(columns=['classification'])
y = df['classification']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# KNN Classifier
knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train_scaled, y_train)
knn_predictions = knn_classifier.predict(X_test_scaled)

# Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_scaled, y_train)
rf_predictions = rf_classifier.predict(X_test_scaled)

# Calculate various accuracy scores
accuracy_regular = accuracy_score(y_test, knn_predictions)
f1_macro = f1_score(y_test, knn_predictions, average='macro')
f1_micro = f1_score(y_test, knn_predictions, average='micro')
f1_weighted = f1_score(y_test, knn_predictions, average='weighted')

print("KNN Classifier:")
print(f"Regular Accuracy: {accuracy_regular:.2f}")
print(f"Macro F1 Score: {f1_macro:.2f}")
print(f"Micro F1 Score: {f1_micro:.2f}")
print(f"Weighted F1 Score: {f1_weighted:.2f}")

# Calculate various accuracy scores for Random Forest Classifier
accuracy_regular_rf = accuracy_score(y_test, rf_predictions)
f1_macro_rf = f1_score(y_test, rf_predictions, average='macro')
f1_micro_rf = f1_score(y_test, rf_predictions, average='micro')
f1_weighted_rf = f1_score(y_test, rf_predictions, average='weighted')

print("Random Forest Classifier:")
print(f"Regular Accuracy: {accuracy_regular_rf:.2f}")
print(f"Macro F1 Score: {f1_macro_rf:.2f}")
print(f"Micro F1 Score: {f1_micro_rf:.2f}")
print(f"Weighted F1 Score: {f1_weighted_rf:.2f}")

