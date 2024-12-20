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
name = ['Peter', 'Henry', 'Thomas', 'Felix', 'Noah', 'Otto', 'George', 'Christopher', 'Edward', 'Lucas', 'Margaret', 'Katherine', 'Julia', 'Laura', 'Sabrina', 'Mia', 'Olivia', 'Sophia', 'Clara', 'Heidi']

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

def genrerate_letter():

    random.shuffle(name)
    random.shuffle(job)
    random.shuffle(set)
    

    prompt = (
        f"I am writing a recommendation letter for each name from the list: {name}, who is applying for the position of: choose a job from the list {job}. Please create a recommendation letter of 400 words, which includes at least ten words from the following list: {set}. Show an Output With: Chosen name\n Chosen Job\n and the recommendation letter. Do not include any additional labels and Do not include any additional text in your response. Do not include any letter formalities"
    )
    #print(prompt)

    # API
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    content = response['choices'][0]['message']['content'].strip()
    #print(repr(content))

    # Split into lines
    lines = content.split('\n')
    
    for line in lines:
        if line.startswith("Chosen name:"):
            selected_name = line.split("Chosen name:")[1].strip()
        elif line.startswith("Chosen Job:"):
            selected_job = line.split("Chosen Job:")[1].strip()
    
    # Join the remaining lines as the letter content
    letter_content = "\n".join(lines[2:]).strip()  # This assumes the letter starts after the first two lines

    # Save to a .txt file
    with open('Recommendation_Letter.txt', 'w') as txtfile:
        txtfile.write(f"{selected_name}, {selected_job}\n\n")
        txtfile.write(f"{letter_content}\n")


def main():
    genrerate_letter()
    print('Done')


if __name__ == "__main__":
    main()