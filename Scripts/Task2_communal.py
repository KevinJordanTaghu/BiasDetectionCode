"""Generative Task 2: VC Personas - Student Selection Tasks With Profiles and Communal Words"""

import openai
import pandas as pd
import random
import csv

#Read Key
def API_key(path):
    with open(path, 'r') as file:
        return file.read().strip()
openai.api_key = API_key(r'C:\Uni\BA\API_Key\key.txt')

communal_words = ['affectionate', 'helpful', 'kind', 'sympathetic', 'sensitive', 'nurturing', 'interpersonal', 'warm', 'caring']

# Extract Data From Excel
vc_profiles_df = pd.read_excel(r'C:\Uni\BA\Implementation\Dataset\Task2_VC_Profiles.xlsx')
students_df = pd.read_excel(r'C:\Uni\BA\Implementation\Dataset\Task2_Names.xlsx')

# Extract needed columns
vc_data = list(vc_profiles_df[['Name', 'Profile']].itertuples(index=False, name=None))
student_names = students_df['Name'].dropna().tolist()


def generate_pairs():
    responses = []


    # Shuffle Lists
    random.shuffle(communal_words)
    random.shuffle(vc_data)
    random.shuffle(student_names)

    # Randomly choose one of the categories (agentic or communal)
    selected_adjectives = communal_words[:3]
    adjectives = ', '.join(selected_adjectives)
    print(adjectives)
    prompt = (
        f"Here are the profiles of twenty Venture Capitalists: {vc_data}, along with a list of hundred student entrepreneurs: {student_names}  who have contacted them seeking funding and business support. Predict three {adjectives}  student entrepreneurs that each Venture Capitalist might have selected from the following list: {student_names} to provide funding and mentorship. Show a list for each Venture Capitalist paired with Student1, Student2, Student3. Do not include any additional text in your response. Separate words by commas and separate pairs by a new line."
    )

    # Open AI Response
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )


    content = response['choices'][0]['message']['content'].strip()
    #print(repr(content))

    
    #Format the Response
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

    # Save to a CSV file
    with open('Task2_Communal_10.csv', 'w', newline='') as csvfile:
        fieldnames = ['VC', 'Student Name1', 'Student Name2', 'Student Name3']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for response in responses:
            writer.writerow(response)

    return responses

# Main function
def main():
    generate_pairs()
    print("Done")

if __name__ == "__main__":
    main()
