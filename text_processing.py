import aiohttp
import asyncio
import re

async def fetch_text(session, semaphore, unique_texts):
    async with semaphore:
        async with session.get('https://en.wikipedia.org/api/rest_v1/page/random/summary') as response:
            if response.status == 200:
                data = await response.json()
                full_text = data['extract']
                sentences = re.findall(r'[^.!?]*[.!?]', full_text)
                for sentence in sentences:
                    sentence = sentence.strip()
                    clean_sentence = re.sub(r',+', ',', sentence)  # Remove multiple commas
                    clean_sentence = re.sub(r'[^a-zA-Z,.!? ]', '', clean_sentence)
                    clean_sentence = re.sub(r' +', ' ', clean_sentence)  # Remove multiple spaces
                    clean_sentence = re.sub(r',([.!?])', r'\1', clean_sentence)  # Remove comma before punctuation
                    clean_sentence = re.sub(r' ([.!?])', r'\1', clean_sentence)  # Remove space before punctuation
                    clean_sentence = re.sub(r'([A-Z]{2,})', lambda m: m.group(1)[0], clean_sentence)  # Replace two or more consecutive capital letters with a single one
                    clean_sentence = re.sub(r' ,', ',', clean_sentence)  # Remove space before comma
                    if clean_sentence and clean_sentence not in unique_texts:
                        unique_texts.add(clean_sentence)
                        if len(unique_texts) >= 1000:
                            return

async def fetch_1000_unique_texts():
    unique_texts = set()
    semaphore = asyncio.Semaphore(100)
    async with aiohttp.ClientSession() as session:
        while len(unique_texts) < 1000:
            tasks = [fetch_text(session, semaphore, unique_texts) for _ in range(100)]
            await asyncio.gather(*tasks)
    return list(unique_texts)

def select_n_texts_from_pool(texts, n, difficulty):
    min_chars, max_chars = 0, 0
    if difficulty == "easy":
        min_chars, max_chars = 20, 60
    elif difficulty == "medium":
        min_chars, max_chars = 60, 100
    elif difficulty == "hard":
        min_chars, max_chars = 100, 140

    selected_texts = []
    for text in texts:
        if min_chars <= len(text) <= max_chars:
            selected_texts.append(text)
            if len(selected_texts) == n:
                break
    return selected_texts

def longest_common_subsequence(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    return lengths[-1][-1]
