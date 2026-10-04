# NLP Practicals — BIT4133 Natural Language Processing

Department of Information Technology
**BSCCS/2024/45844 — Kamunyu Raphael Kamau**
Bachelor of Science in Computer Science

Weekly practicals, tool activities, and the take-home project for the NLP
course, built progressively: **Text → N-grams → Context → POS Tags →
Sequences → HMM → Prediction → Evaluation**, then extended into named-entity
information extraction.

## Contents

| Week | Topic | Folder |
|---|---|---|
| 1 | Tokenization (NLTK) | [`week1-tokenization/`](week1-tokenization) |
| 2 | N-grams + frequency analysis tool activity (NLTK) | [`week2-ngrams/`](week2-ngrams) |
| 3 | Hidden Markov Models & sequence labeling, tool activity, take-home project, project report (NLTK + from-scratch HMM) | [`week3-hmm-sequence-labeling/`](week3-hmm-sequence-labeling) |
| 5 | IBM SkillsBuild — *Generative AI Essentials: Using LLMs to Work with Data* | see below |
| 6 | Information extraction with Named Entity Recognition (spaCy) | [`week6-information-extraction/`](week6-information-extraction) |

### Week 1 — Tokenization
Word tokenization with NLTK's `word_tokenize`.

### Week 2 — N-grams
Builds unigrams, bigrams, and trigrams with `nltk.util.ngrams`, plus the
Week 2 Tool Activity: a paragraph-frequency analyzer (lowercase → tokenise
→ n-grams → frequency counts → top-5 table).

### Week 3 — Hidden Markov Models & Sequence Labeling
- The lecture's sequence-labeling example.
- Tool Activity (#19): a manual HMM-style tagger built from raw transition
  and emission counts (no NLTK HMM classes).
- Take-Home Project (#22): a from-scratch HMM part-of-speech tagger —
  32 labelled training sentences, Laplace-smoothed transition/emission
  probabilities, full Viterbi decoding, evaluated on a held-out test set
  (91.4% accuracy), with error analysis.
- Project Report (#23): `HMM_Project_Report.docx`, covering introduction,
  dataset, methodology, implementation, results, error analysis,
  discussion, limitations, conclusion, and references.

### Week 5 — Skills Development
Completed the IBM SkillsBuild course *Generative AI Essentials: Using LLMs
to Work with Data*, covering large language models, text summarization,
language translation, content generation, and IBM's Granite model family
(Multilingual, Instruct, Guardian, Code, Japanese), plus prompting, data
summarization, and text classification.

Digital badge: https://www.credly.com/badges/b6fa6392-5eae-4578-91ea-46c6d438a303/public_url

### Week 6 — Information Extraction
A named-entity extraction system built with spaCy (`en_core_web_sm`):
extracts PERSON / ORGANIZATION / LOCATION / DATE from text, tested on the
supplied example and five additional sentences, with a discussion of
entities the model missed or mislabeled. Extended to also extract MONEY,
PRODUCT, EVENT, TIME, and PERCENTAGE.

## Running the notebooks

```bash
pip install nltk spacy
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt_tab')"
jupyter notebook
```
