"""Tests for the cdstemplate.word_count methods and classes."""
from cdstemplate import word_count

def test_stop_words():
    """Test that stop words are removed when enabled."""
    counter = word_count.CorpusCounter(remove_stop_words=True)
    counter.add_doc("The cat and the dog")
    counts = counter.get_counts()
    
    # Check that common stop words are removed
    assert "the" not in counts['token'].values
    assert "and" not in counts['token'].values
    
    # Check that regular words are kept
    assert "cat" in counts['token'].values
    assert "dog" in counts['token'].values
