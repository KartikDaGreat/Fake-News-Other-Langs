## Fake News Detection for other Languages

This repository hosts a Fake News Detection framework specifically designed for Tamil and Malayalam languages. The growing influence of digital media has led to an increase in misinformation, posing a challenge for truth and reliability in news consumption. To combat this, the framework leverages Natural Language Processing (NLP) and Machine Learning (ML) to accurately classify news content as real or fake.

This multi-stage pipeline integrates a combination of pre-trained language models, classical ML approaches, and neural networks, providing robust detection capabilities for Tamil and Malayalam language texts. The framework is trained on the HASOC-Offensive Language Identification (DravidianCodeMix) dataset, ensuring the model's capability to handle Dravidian language nuances.

# Features
Language Detection: A preprocessing step to identify the input language, ensuring the correct language-specific pipeline is applied.
Text Preprocessing: Includes tokenization, stop-word removal, and normalization tailored for Tamil and Malayalam.
Feature Engineering: Uses TF-IDF vectorization and embeddings like mBERT to extract relevant textual features for better classification.
Classification Models: Integrates multiple models, including:
  mBERT (Multilingual BERT) for capturing deep semantic features.
  SVM (Support Vector Machine) with TF-IDF features for traditional classification.
  LSTM Networks to capture sequential patterns in text.
Softmax Voting Classifier: Combines the predictions from multiple models to provide a final classification decision with improved accuracy.
