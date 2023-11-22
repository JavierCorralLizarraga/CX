import os
import re
import pandas as pd
from pysentimiento import create_analyzer

def process_and_save_sentiment(input_file='Base Total Twitter.xlsx', output_excel='sentimental.xlsx', output_csv='sentimental.csv'):
    df = pd.read_excel(input_file)

    # Extract mentions and emojis
    tweets = df['Asunto']
    menciones = tweets.apply(lambda tweet: re.findall(r"@([A-Za-z0-9_]+)", tweet))
    df['menciones'] = menciones
    emojis = tweets.apply(lambda tweet: re.findall(r":([^:]+):", tweet))
    df['emojis'] = emojis[emojis.apply(lambda x: len(x) > 0)]

    # Unique mentions and emojis
    unique_menciones = list(set([string for sublist in menciones for string in sublist]))
    unique_emojis = list(set([string for sublist in emojis for string in sublist]))

    # Clean tweets
    aux_serie = tweets.apply(lambda tweet: re.sub(r"@([A-Za-z0-9_]+)", '', tweet))  # remove mentions
    aux_serie = aux_serie.apply(lambda tweet: re.sub(r":([^:]+):", '', tweet))  # remove emojis
    aux_serie = aux_serie.apply(lambda tweet: re.sub(r"\bhttps?://\S+\b", '', tweet))  # remove URLs
    df['asunto_limpio'] = aux_serie

    # Sentiment analysis
    analyzer = create_analyzer(task="sentiment", lang="es")
    df['sentiment'] = df['asunto_limpio'].apply(lambda x: analyzer.predict(str(x)))
    df['out'] = df['sentiment'].apply(lambda x: x.output)
    df['probas'] = df['sentiment'].apply(lambda x: x.probas)
    df['proba_neg'] = df['probas'].apply(lambda x: x['NEG'])
    df['proba_neu'] = df['probas'].apply(lambda x: x['NEU'])
    df['proba_pos'] = df['probas'].apply(lambda x: x['POS'])

    # Save to Excel and CSV
    df.to_excel(output_excel)
    df.to_csv(output_csv)

    print(f"Processed and saved sentiment analysis to {output_excel} and {output_csv}")

# Call the function with default parameters or provide custom file names
process_and_save_sentiment()

