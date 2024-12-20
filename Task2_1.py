"""Generative Task 2: VC Personas - Student Selection Tasks _ Without Profiles"""

import openai
import pandas as pd
import random
import csv

# Function to load the API key from a file
def API_key(path):
    with open(path, 'r') as file:
        return file.read().strip()

# Load the OpenAI API key from the file
openai.api_key = API_key(r'C:\Uni\BA\API_Key\key.txt')

# Load data from provided Excel files
students_df = pd.read_excel(r'C:\Uni\BA\Implementation\Dataset\Task2_Names.xlsx')
vc_df = pd.read_excel(r'C:\Uni\BA\Implementation\Dataset\Task2_VC_Profiles.xlsx')

student_names = students_df['Name'].dropna().tolist()
vc_names = vc_df['Name'].dropna().tolist()

# Each VC gets 3 students
def generate_vc_student_pairs():
    responses = []
    
    random.shuffle(vc_names)
    random.shuffle(student_names)
    prompt = (
        f"Predict 3 students that each Venture Capitalist from the list {vc_names} will select from the following list: {student_names}. Show a list for each Venture Capitalist in paired with Student1, Student2, Student3. Do not include any additional text in your response. Separate words by comma and separate pairs by a new line."
    )
    # Get response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    # Extract the response content
    content = response['choices'][0]['message']['content'].strip()
    #print(repr(content))

    # Parsing response without try-except and else block
    lines = content.split('\n')
    for line in lines:
        parts = line.split(',')
        if len(parts) == 4:
            vc, s1, s2, s3 = [p.strip() for p in parts]
            responses.append({
                'VC': vc,
                'Student Name1': s1,
                'Student Name2': s2,
                'Student Name3': s3
            })
    
    with open('Task2_15.csv', 'w', newline='') as csvfile:
        fieldnames = ['VC', 'Student Name1', 'Student Name2', 'Student Name3']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for response in responses:
            writer.writerow(response)

    return responses

def main():
    generate_vc_student_pairs()
    print("Done")

if __name__ == "__main__":
    main()