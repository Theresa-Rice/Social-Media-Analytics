# Social Media Analytics
A sentiment analysis project that collects and analyzes review data (such as from Reddit) to understand user opinions and trends on social media.

---

## Description  
This repository contains code and data for performing social media sentiment analysis. It includes scripts to scrape and process review data, a dataset of reviews, and a notebook that demonstrates how sentiment analysis is applied to extract insights from text data. The goal of this project is to show how text data from social media platforms can be analyzed to uncover sentiment patterns and trends. The project offers practical examples of scraping data, cleaning it, and applying analytical techniques to derive meaningful results.

---

## Getting Started

### Dependencies  
- Python
- Libraries such as `pandas`, `nltk`, `scikit-learn`, `textblob` or similar for text processing  
- Jupyter Notebook environment (for running the analysis notebook)

---

### Installing  

1. Clone the repository  
   `git clone https://github.com/Theresa-Rice/Social-Media-Analytics`

2. Navigate to the project folder  
   `cd Social-Media-Analytics`

3. Install required Python packages  
   `pip install pandas nltk scikit-learn`

4. (Optional) Download any required NLP models or tokenizers for sentiment analysis

---

### Executing Program  

1. Run the scraper to collect review data:  
   `python ReviewScaper.py`

2. Process the collected data with the main analysis script:  
   `python Review.py`

3. Open `Sentiment Analysis.ipynb` in Jupyter Notebook  
   `jupyter notebook Sentiment Analysis.ipynb`

4. Run the notebook cells step-by-step to view preprocessing, sentiment scoring, and visualization results.

---

## Help

### Common Problems  
- Make sure all Python dependencies are installed correctly.  
- If scraping fails, check your API keys or site access rules.  
- For NLP libraries, ensure any required language models are downloaded before running the notebook.

To get help inside Jupyter, use `?` on functions or `%help` in the notebook.

---

## Authors  

- **Theresa Rice**  
  GitHub: https://github.com/Theresa-Rice

