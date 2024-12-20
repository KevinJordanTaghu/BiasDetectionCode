"""Generatice Task 2 - example of early entrepreneurial Tasks"""

import openai
import pandas as pd
import random
import csv
import re

#Read Key
def API_key(path):
    with open(path, 'r') as file:
        return file.read().strip()
openai.api_key = API_key(r'C:\Uni\BA\API_Key\key.txt')

#Names
names = ['Peter', 'Henry', 'Thomas', 'Felix', 'Noah', 'Otto', 'George', 'Christopher', 'Edward', 'Lucas', 'Margaret', 'Katherine', 'Julia', 'Laura', 'Sabrina', 'Mia', 'Olivia', 'Sophia', 'Clara', 'Heidi']

# Alle Wörter ohne die Kategorienamen in einer einzigen Menge speichern
set = ['talent', 'intelligen*', 'smart', 'skill', 'ability', 'genius', 'brillian*', 'bright', 'brain', 'aptitude', 'gift',
        'capacity', 'flair', 'knack', 'clever', 'expert', 'proficien', 'capab*', 'adept*', 'able', 'competent', 
        'instinct', 'adroit', 'creative', 'insight', 'analy*', 'research', 'excellen*', 'superb', 'outstand*', 'exceptional',
        'unparallel*', 'most', 'magnificent', 'remarkable', 'extraordinary', 'supreme', 'unmatched', 'best', 
        'outstanding', 'leading', 'preeminent', 'execut*', 'manage', 'lead', 'led', 'activ*', 'adventur*', 'aggress', 
        'ambitio*', 'assert', 'athlet*', 'autonom*', 'boast', 'challeng*', 'compet*', 'courag*', 'decide', 'decisi*', 
        'determin*', 'dominan*', 'force', 'greedy', 'headstrong', 'hierarch', 'hostil*', 'impulsive*', 'independen*', 
        'individual', 'intellect', 'logic', 'masculine', 'objective', 'opinion', 'outspoken', 'persist*', 'principle', 
        'reckless', 'stubborn', 'superior', 'confiden*', 'sufficien*', 'relian*', 'affection', 'child', 'cheer', 'commit', 
        'communal', 'compassion', 'connect', 'considerat*', 'cooperat*', 'emotion', 'empath', 'feminine', 'flatterable*', 
        'gentle', 'interperson*', 'interdependent*', 'kind', 'kinship', 'loyal', 'nurtur*', 'pleasant', 'polite', 'quiet', 
        'responsiv*', 'sensitiv*', 'submissive', 'supportiv*', 'sympath*', 'tender', 'together', 'trust', 'understanding', 
        'warm', 'whin*', 'daring', 'help', 'sensitive', 'agree', 'caring', 'tact', 'assist', 'profess', 'corporate', 
        'office', 'business', 'career', 'promot*', 'occupation', 'position', 'home', 'parent', 'family', 'marri*', 
        'wedding', 'relatives', 'husband', 'wife', 'mother', 'father', 'son', 'daughter']

job = [
    "Digital Transformation Consultant", "Web Developer", "IT Consultant", 
    "IT Specialist", "DevOps Engineer", "Solution Architect", "Cloud Engineer", 
    "Data Engineer", "Digital Product Manager", "Tech Startup Founder", 
    "Chief Technology Officer", "Venture Capital Analyst", "Cybersecurity Specialist", 
    "Agile Coach", "AI Engineer", 
    "E-Commerce Specialist", "Tech Entrepreneur", "Virtual Reality Engineer", 
    "UX/UI Designer", "User Experience Researcher"
]

random.shuffle(names)
random.shuffle(job)
random.shuffle(set)

def generate_letter(name):
    

    prompt = (
        f"I am writing a recommendation letter for: {name}, who is applying for the position of: select an appropriate {job} title based on the name. Please create a recommendation letter of 400 words, which includes at least ten words from the following list: {set}. Show an Output With: name\n  Job\n and the recommendation letter. Do not include any additional labels and Do not include any additional text in your response. Do not include any letter formalities"
    )
    print(prompt)

    # API
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()
    #print(repr(content))

def save_letters():
    for name in names:
        letter_content = generate_letter(name)
        
        # Extract the chosen job title from the response if needed
        lines = letter_content.split("\n")
        job_line = next((line for line in lines if line.startswith("Job:")), "Job: Unknown")
        chosen_job = job_line.split("Job:")[1].strip()

        # Define the filename for each letter
        file_path = f'Recommendation_Letter_{name}.txt'
        
        # Save the letter content to the respective file
        with open(file_path, 'w') as txtfile:
            txtfile.write(letter_content)
        
        print(f"Generated and saved {file_path} with job title '{chosen_job}'")

def main():
    save_letters()
    print('Done')


if __name__ == "__main__":
    main()