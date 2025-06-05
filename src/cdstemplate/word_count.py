from collections import Counter
import logging
import re
import pandas as pd

logger = logging.getLogger(__name__)

# Common English stop words
STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "he",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "that",
    "the",
    "to",
    "was",
    "were",
    "will",
    "with",
}


def tokenize(text, pattern=r"\s"):
    """Split text into tokens based on regex pattern."""
    return [t for t in re.split(pattern, text) if t]


class CorpusCounter:
    """Tracks word counts in a corpus of documents."""

    def __init__(self, case_insensitive=False, remove_stop_words=False):
        """Initialize counter with optional case insensitivity and stop word removal."""
        self.counter = Counter()
        self.case_insensitive = case_insensitive
        self.remove_stop_words = remove_stop_words
        self.doc_count = 0

    def add_doc(self, text):
        """Add a document to the corpus."""
        tokens = tokenize(text)
        if self.case_insensitive:
            tokens = [t.lower() for t in tokens]
        if self.remove_stop_words:
            tokens = [t for t in tokens if t not in STOP_WORDS]
        self.counter.update(tokens)
        self.doc_count += 1

    def get_counts(self):
        """Return token counts as a DataFrame."""
        return pd.DataFrame(self.counter.items(), columns=["token", "count"]).sort_values("token")

    def save_counts(self, csv_path):
        """Save token counts to CSV."""
        self.get_counts().to_csv(csv_path, index=False)
