<h1 align="center">Ali Nawaz</h1>

<p align="center">
  <strong>PYTHON DEVELOPER</strong><br />
  Applied NLP &nbsp;·&nbsp; Web Scraping &nbsp;·&nbsp; Web Applications
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1100&color=36BCF7&center=true&vCenter=true&width=760&lines=Python+Developer+%7C+Applied+NLP;Web+Scraping+%7C+Web+Applications;Building+Sindhi+Language+Technology" alt="Animated text: Python Developer, Applied NLP, Web Scraping, Web Applications, and Sindhi Language Technology" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/ali-nawaz-786w/">LinkedIn</a>
  &nbsp;·&nbsp;
  <a href="https://huggingface.co/alinawazmahar">Hugging Face</a>
  &nbsp;·&nbsp;
  <a href="https://pypi.org/project/sindhi-nlp/">PyPI package</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Transformers" />
  <img src="https://img.shields.io/badge/SentencePiece-6A4C93?style=flat-square" alt="SentencePiece" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/Gradio-F97316?style=flat-square" alt="Gradio" />
</p>

---

## Python developer building from data to application

I build Python software that turns data and focused experiments into tools people can use. My work spans web scraping and data preparation, NLP model development, APIs, and web applications.

My deepest project area is **Sindhi language technology**. I work across the pipeline: preparing language data, training and comparing tokenizers and classifiers, documenting what the evaluations do and do not show, and packaging models behind reusable Python interfaces.

## Sindhi language engineering

### [Sindhi Tokenizer](https://github.com/alinawazcode/sindhi-tokenizer)

**A corpus-driven SentencePiece Unigram tokenizer for Sindhi in Perso-Arabic script.**

- Trained on a corpus of **1.46M+ sentences**, including Sindhi and regional text sources.
- Publishes four vocabulary sizes: **32k, 64k, 100k, and 150k**; 64k is the recommended balance in the project documentation.
- Compares **14 baseline tokenizers** with four custom vocabulary sizes across four registers: FLORES+, Wikipedia, sentiment text, and regional news. The 18 benchmark entries represent 17 distinct behaviors because two listed baselines are equivalent in this evaluation.
- Uses full observed-character coverage and byte fallback; includes training scripts, corpus provenance, benchmark results, and documented experiments that did not help.
- The reported **0.0000% normalized-length loss** is a length-based round-trip check. The repository explicitly notes that it cannot prove exact character identity for arbitrary text. Downstream task gains have not yet been established.

**Explore:** [Repository](https://github.com/alinawazcode/sindhi-tokenizer) · [Documentation](https://alinawazcode.github.io/sindhi-tokenizer/) · [Models](https://huggingface.co/alinawazmahar/sindhi-tokenizer) · [Demo code](https://github.com/alinawazcode/sindhi-tokenizer/tree/main/demo)

### [sindhi-nlp](https://github.com/alinawazcode/sindhi-nlp)

**A reproducible Sindhi sentiment-classification package—not just a notebook.**

- Predicts **negative, neutral, or positive** sentiment for short Sindhi text.
- Includes a fast TF-IDF + LinearSVC baseline and a fine-tuned XLM-RoBERTa model, plus Python SDK, CLI, batch inference, and FastAPI service.
- On the 884-sentence held-out test set, the TF-IDF baseline reports **0.8695 macro-F1 / 0.8688 accuracy**; the mixed XLM-R model reports **0.8906 macro-F1 / 0.8903 accuracy**.
- The measured difference was **not statistically significant** in the reported paired test (McNemar p = 0.116). The baseline is a meaningful option when CPU speed and simplicity matter.
- The package includes tests, CI, typed interfaces, API documentation, and a model card. The natural-language labels were assigned by one annotator, and the project documents limits on dialect, social text, sarcasm, and other domains.

**Explore:** [Repository](https://github.com/alinawazcode/sindhi-nlp) · [PyPI](https://pypi.org/project/sindhi-nlp/) · [Documentation](https://alinawazcode.github.io/sindhi-nlp/) · [Hugging Face model](https://huggingface.co/alinawazmahar/sindhi-sentiment-xlmr)

### [Sindhi Sentiment Dataset](https://github.com/alinawazcode/Sindhi_Sentiment_dataset)

**A public dataset and classical machine-learning baseline for Sindhi sentiment.**

- Contains **4,420 human-labeled sentences** balanced across positive, negative, and neutral labels.
- The training script compares Logistic Regression, LinearSVC, and Complement Naive Bayes with a dual TF-IDF representation: character n-grams (2–6) and word n-grams (1–2).
- Uses stratified train/validation/test splits and five-fold tuning on training data; saves model bundles and a metrics report.
- The README explains why an earlier pseudo-labeled evaluation produced a higher score and why the expanded human-labeled evaluation is a more cautious measure.
- **Data caveat:** one person labeled the sentences; agreement between annotators was not measured. News-style text is not a substitute for evaluation on social media or conversational Sindhi.

**Explore:** [Repository](https://github.com/alinawazcode/Sindhi_Sentiment_dataset) · [Live demo](https://huggingface.co/spaces/alinawazmahar/sindhi-sentiment)

## Python, search, and web applications

### [DataScout](https://github.com/alinawazcode/datascout)

**A Gradio web app for finding datasets by meaning.** It retrieves a keyword-filtered candidate set from the Hugging Face Hub, embeds descriptions with `all-MiniLM-L6-v2`, then ranks candidates using **75% semantic similarity and 25% metadata/popularity signals**. Kaggle search is optional. The quality component is a documentation/popularity proxy, not an audit of dataset quality; live search also means candidates are fetched again for each query.

[Repository](https://github.com/alinawazcode/datascout) · [Live demo](https://huggingface.co/spaces/alinawazmahar/DataScout)

### [Passli](https://github.com/alinawazcode/passli)

**A Django document vault with encrypted storage and time-limited sharing.** It implements AES-256-GCM encryption at rest, hashed share keys, QR-based access, view/download restrictions, expiry, revocation, and security logging. Its security policy is clear that the server holds the master key and can read documents: **Passli is not zero-knowledge and has not had an independent security audit.**

[Repository](https://github.com/alinawazcode/passli) · [Security policy](https://github.com/alinawazcode/passli/blob/main/SECURITY.md)

### [CCTV Visual RAG](https://github.com/alinawazcode/CCTV-Visual-RAG)

**Natural-language search over sampled video frames.** OpenCV samples frames, CLIP creates image/text embeddings, and FAISS ranks matching frames with timestamps. The demo uses 1 FPS sampling and a 500-frame cap. It retrieves relevant frames; temporal clip understanding is listed as future work.

[Repository](https://github.com/alinawazcode/CCTV-Visual-RAG) · [Live demo](https://huggingface.co/spaces/alinawazmahar/cctv-visual-rag)

### [ANEX Programming Language](https://github.com/alinawazcode/Anex-Programming-Language)

**An educational programming-language and visual-debugger project built in Python.** It demonstrates a lexer, parser/AST, interpreter, variables, control flow, functions, and a customtkinter interface that visualizes the execution pipeline. The README also describes optimization and pseudo-code generation stages; see the repository for the current implementation and examples.

[Repository](https://github.com/alinawazcode/Anex-Programming-Language)

### [React + Vite Site](https://github.com/alinawazcode/The-Shaikh-Ayaz-University-Website)

A React + Vite web project. Its public README is still the Vite starter template, so project-specific screenshots, setup, and my contribution are not documented there yet.

[Repository](https://github.com/alinawazcode/The-Shaikh-Ayaz-University-Website)

## Skills and tools

| Area | Tools and work |
| --- | --- |
| **Python development** | Python packages, command-line tools, APIs, data processing |
| **Applied NLP / ML** | scikit-learn, PyTorch, Transformers, SentencePiece, text evaluation |
| **Web and data** | Web scraping, Django, FastAPI, Gradio, React + Vite |
| **Search and vision** | Sentence Transformers, FAISS, CLIP, OpenCV |
| **Engineering practices** | Tests, CI, reproducible runs, model cards, documented limitations |

## How I work

**Understand the data → build a baseline → measure carefully → package the useful result → document the limits.**

I value readable code and claims that can be checked against source, metrics, and a reproducible run.

---

<p align="center">
  <a href="https://www.linkedin.com/in/ali-nawaz-786w/">Connect on LinkedIn</a>
  &nbsp;·&nbsp;
  <a href="https://huggingface.co/alinawazmahar">Explore my Hugging Face work</a>
</p>
