'''Custom NER means teaching an NLP model to find and label specific "entities" (names, products, IDs, custom medical/drug names, etc.) in text, where the set of entities or their types is specialized for your application.'''
'''Why and When?
General NER models ("PER", "ORG", "LOC") are powerful, but you may need something unique:
Medical NER: Drug names, diseases, gene mutations, symptoms.
Brand/Product NER: Brand names, model numbers.
Legal/Contract NER: Clause names, dates, case/precedent names.
Your own company’s jargon or confidential identifiers.'''
'''Key Concepts
Annotation: Marking up text with what words/phrases belong to which entity classes.
Entity Types: You define them! E.g., "PRODUCT", "BRAND", "INGREDIENT".
Fine-tuning: Adapting a pre-trained model to spot your entity types using labeled training examples.
Evaluation: Test on a held-out set and check Precision/Recall/F1 for each type.'''

