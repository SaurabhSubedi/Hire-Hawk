import spacy
import os 

def skill_extraction(text):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    patterns_path = os.path.join(current_dir, 'patterns.jsonl')
    nlp = spacy.load("en_core_web_sm")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.from_disk(patterns_path)
    doc = nlp(text)
    skills = set()
    skills.update(entity.text for entity in doc.ents if entity.label_ == 'PROGRAMMING_LANGUAGE' or entity.label_ == 'Database' or entity.label_ == 'Frameworks')
    return list(skills)