# sentiment.py

from textblob import TextBlob

def analyze_sentiment(text):
	"""
	Analyze the sentiment of the given text using TextBlob
	Returns: 'Positive', 'Neutral', or 'Negative'.
	"""
	blob = TextBlob(text)
	polarity = blob.sentiment.polarity # Polarity ranges from -1 (neg) to 1 (pos)

	if polarity > 0.1:
		return "Positive"
	elif polarity < -0.1:
		return "Negative"
	else:
		return "Neutral"