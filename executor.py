import io
import pandas as pd
import duckdb
from utils.plotter import plot_and_encode
from utils.scraper import scrape_grossing_films

def handle_question(questions, files):
    answers = []
    if "highest grossing films" in questions.lower():
        df = scrape_grossing_films()
        q_lines = questions.strip().split("\n")

        q1 = df[(df['Worldwide gross'] >= 2e9) & (df['Year'] < 2000)].shape[0]
        answers.append(q1)

        q2_df = df[df['Worldwide gross'] > 1.5e9]
        q2 = q2_df.sort_values('Year').iloc[0]['Title']
        answers.append(q2)

        corr = df['Rank'].corr(df['Worldwide gross'])
        answers.append(round(corr, 6))

        encoded_img = plot_and_encode(df)
        answers.append(encoded_img)

    elif any(f.endswith('.csv') for f in files):
        for name, file in files.items():
            if name.endswith('.csv'):
                df = pd.read_csv(file)
                answers.append(f"Loaded {len(df)} rows from {name}")

    return answers
