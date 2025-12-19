'''The Hugging Face pipeline is a high-level, easy-to-use API designed to perform various NLP tasks (like sentiment analysis, text summarization, translation, named entity recognition, etc.) directly, without needing to manually load tokenizers, models, or write inference loops. It abstracts away most of the complexity of using Transformer models.'''
'''Simplicity: Get powerful NLP results with just a few lines of code.
Rapid Prototyping: Quickly test different models for a task.
Ease of Use: Ideal for beginners and for quickly deploying models for inference.
Versatility: Supports a wide range of NLP tasks.'''

# sentiment analysis pipeline
'''Determines the emotional tone of a piece of text (e.g., positive, negative, neutral). The pipeline loads a pre-trained model specifically fine-tuned for this task.'''
from transformers import pipeline
print(f"--- Hugging Face Pipeline: Sentiment Analysis ---")
# 1. Initialize the sentiment-analysis pipeline
sentiment_classifier = pipeline("sentiment-analysis")
# 2. Analyze text
texts = [
    "I love using Hugging Face pipelines, they are so easy!",
    "This product is terrible and I'm very disappointed.",
    "The movie was okay, not great, not bad.",
    "What a wonderful day to learn NLP!"
]
results = sentiment_classifier(texts)
# 3. Print results
print("\nSentiment Analysis Results:")
for text,result in zip(texts,results):
    label = result['label']
    score = result['score']
    print(f" Text: '{text}' ")
    print(f"    -> Label: {label}, Score: {score:.4f}")

# Named Entity Recognition (NER) Pipeline
print("\n--- Hugging Face Pipeline: Named Entity Recognition (NER) ---")
ner_recognizer = pipeline("ner", grouped_entities=True) # grouped_entities merges subword tokens
text_for_ner = "My name is John Doe, and I work at Google in Mountain View, California. I visited Paris last year."
results = ner_recognizer(text_for_ner)

print("\nNamed Entity Recognition Results:")
for entity in results:
    word = entity['word']
    entity_group = entity['entity_group']
    score = entity['score']
    start = entity['start']
    end = entity['end']
    print(f"  Entity: '{word}' (Type: {entity_group}, Score: {score:.4f}, Span: [{start}-{end}])")

# Text Summarization Pipeline
print("\n--- Hugging Face Pipeline: Text Summarization ---")
summarizer = pipeline("summarization")
long_text = """
Hugging Face is an American company that develops tools for building, training, and
deploying machine learning models. It is known for its Transformers library, which
provides APIs for using Transformer models, a deep learning architecture that has
revolutionized natural language processing. The company also developed
datasets and shared a model hub with over 120,000 models and 20,000 datasets.
Its open-source contributions have made advanced NLP more accessible to researchers
and developers worldwide. Hugging Face also offers commercial products for model deployment.
"""
summary_results = summarizer(long_text, max_length=50, min_length=20, do_sample=False) # do_sample=False for deterministic output
print("\nOriginal Text:")
print(long_text)
print("\nSummary:")
print(summary_results[0]['summary_text'])

# Machine Translation Pipeline
print("\n--- Hugging Face Pipeline: Machine Translation ---")
translator_en_fr = pipeline("translation_en_to_fr")
english_texts = [
    "Hello, how are you today?",
    "Machine learning is a fascinating field.",
    "The cat is sleeping on the chair."
]
translated_results = translator_en_fr(english_texts)
print("\nEnglish to French Translation Results:")
for eng_text, result in zip(english_texts, translated_results):
    print(f"  English: '{eng_text}'")
    print(f"    -> French: '{result['translation_text']}'")

# Question Answering (QA) Pipeline
print("\n--- Hugging Face Pipeline: Question Answering ---")
qa_model = pipeline("question-answering")
context = """
The Amazon rainforest is the largest tropical rainforest in the world.
It covers an area of approximately 6.7 million square kilometers
(2.6 million square miles), spanning nine countries in South America:
Brazil, Peru, Colombia, Ecuador, Bolivia, Guyana, Suriname, French Guiana, and Venezuela.
The Amazon River, which flows through the rainforest, is the largest river by discharge volume in the world.
"""
question = "Which countries does the Amazon rainforest span?"
answer_results = qa_model(question=question, context=context)
print("\nQuestion Answering Results:")
print(f"  Question: '{question}'")
print(f"  Context:\n{context}")
print(f"  -> Answer: '{answer_results['answer']}' (Score: {answer_results['score']:.4f}, Span: [{answer_results['start']}-{answer_results['end']}])")
# Another example
question_river = "What is the largest river by discharge volume in the world?"
answer_river_results = qa_model(question=question_river, context=context)
print(f"\n  Question: '{question_river}'")
print(f"  -> Answer: '{answer_river_results['answer']}' (Score: {answer_river_results['score']:.4f})")

# Text Generation Pipeline
'''The task of generating new, coherent, and contextually relevant text based on a given prompt or "seed" text. These models have learned grammar, style, and facts from vast amounts of internet text.
Key Concepts:
Prompt/Seed: The initial text given to the model to start generation.
Autoregressive Models: Models like GPT (Generative Pre-trained Transformer) generate text one token at a time, using previously generated tokens as part of the context for the next token.'''
print("\n--- Hugging Face Pipeline: Text Generation ---")
generator = pipeline("text-generation", model="gpt2")
prompt = "The future of AI is bright because"
generated_texts = generator(
    prompt,
    max_new_tokens=50, # Generate up to 50 new tokens
    num_return_sequences=2, # Get 2 different completions
    do_sample=True,
    temperature=0.7
)
print(f"\nPrompt: '{prompt}'")
for i, gen_text in enumerate(generated_texts):
    print(f"  Generated Text {i+1}: '{gen_text['generated_text']}'\n")
# Another example with a different prompt
prompt_story = "Once upon a time, in a land far, far away, there was a brave knight who"
story_results = generator(
    prompt_story,
    max_new_tokens=80,
    num_return_sequences=1,
    do_sample=True,
    temperature=0.8
)
print(f"Prompt: '{prompt_story}'")
print(f"  Generated Story: '{story_results[0]['generated_text']}'")

# Fill-Mask Pipeline
'''The task of predicting missing words (masked tokens) in a sentence. It leverages models like BERT that are specifically pre-trained on a "Masked Language Modeling" (MLM) objective.'''
'''Key Concepts:
Masked Language Modeling (MLM): The pre-training task where the model learns to predict masked words based on their context.
tokenizer.mask_token: A special token (usually [MASK]) used to indicate the position of the word to be predicted.'''
print("\n--- Hugging Face Pipeline: Fill-Mask ---")
unmasker = pipeline("fill-mask")
text_with_mask = "The capital of France is the [MASK] city of Paris."
mask_results = unmasker(text_with_mask, top_k=3) # Get top 3 predictions
print(f"\nSentence with mask: '{text_with_mask}'")
print("Top predictions for [MASK]:")
for result in mask_results:
    print(f"  - Token: '{result['token_str']}' (Score: {result['score']:.4f}, Sequence: '{result['sequence']}')")
# Another example
text_another_mask = "I like to eat [MASK] and [MASK] for breakfast."
# For multiple masks, it often fills them sequentially
another_mask_results = unmasker(text_another_mask, top_k=2)
print(f"\nSentence with multiple masks: '{text_another_mask}'")
print("Top predictions for [MASK]:")
for result in another_mask_results:
    print(f"  - Sequence: '{result['sequence']}'")

# Zero-Shot Classification Pipeline (Very Powerful)
'''A highly versatile classification task where the model can classify text into categories it has never seen during training. Instead of learning fixed categories, it learns to understand text and relate it to descriptive labels provided at inference time.'''
'''Key Concepts:
NLI (Natural Language Inference): Underlying task for many zero-shot models. The model determines if a text "entails," "contradicts," or is "neutral" to a given hypothesis. Zero-shot classification converts the input text and labels into NLI problems.
Flexibility: You can define new categories on the fly without retraining the model.'''
print("\n--- Hugging Face Pipeline: Zero-Shot Classification ---")
classifier_zero_shot = pipeline("zero-shot-classification")
text_to_classify = "This is a great product and I really enjoyed using it."
candidate_labels = ["positive", "negative", "neutral", "anger", "joy"]
zero_shot_results = classifier_zero_shot(text_to_classify, candidate_labels)
print(f"\nText: '{text_to_classify}'")
print(f"Candidate Labels: {candidate_labels}")
print("\nZero-Shot Classification Results (ranked by score):")
# zip labels and scores, then sort by score
sorted_results = sorted(zip(zero_shot_results['labels'], zero_shot_results['scores']), key=lambda x: x[1], reverse=True)
for label, score in sorted_results:
    print(f"  - {label}: {score:.4f}")
# Another example with different labels and text
text_news = "The company announced record profits in the last quarter, exceeding all analyst expectations."
candidate_news_labels = ["business", "sports", "technology", "politics", "finance"]
news_results = classifier_zero_shot(text_news, candidate_news_labels)

print(f"\nText: '{text_news}'")
print(f"Candidate Labels: {candidate_news_labels}")
print("\nZero-Shot Classification Results (ranked by score):")
sorted_news_results = sorted(zip(news_results['labels'], news_results['scores']), key=lambda x: x[1], reverse=True)
for label, score in sorted_news_results:
    print(f"  - {label}: {score:.4f}")