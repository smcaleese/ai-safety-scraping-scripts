Scripts for scraping and analyzing posts from from the Alignment Forum, OpenAI and DeepMind.

Information scraped and analyzed using these scripts was used in this LessWrong post: https://www.lesswrong.com/posts/mC3oeq62DWeqxiNBx/estimating-the-current-and-future-number-of-ai-safety

# Instructions

## Alignment Forum
1. Run the scraping script: `python3 alignment-forum-scraping-script.py`
2. Run the analysis script `alignment-forum-analysis.ipynb`

## OpenAI
1. Run `python3 openai-publication-scraping-script.py` to get a list of publications and authors.
2. Copy the resulting CSV file named `openai-papers-and-authors.csv` and name the copy 
`openai-papers-and-authors-classified.csv`.
3. In `openai-papers-and-authors-classified.csv`, manually classify papers as related to AI safety or not in the `is_safety_paper` column. Also manually add any missing authors for safety papers.

## DeepMind
1. Run `python3 deepmind-publication-scraping-script.py`.
2. Run `deepmind-publication-analysis.ipynb`.
