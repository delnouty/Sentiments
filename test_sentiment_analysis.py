import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
from memory_profiler import profile

class TestSentimentAnalyzer(unittest.TestCase):

    @profile
    def test_sentiment_analyzer(self):
        # Test case for positive sentiment
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], '5 stars')

        # Test case for negative sentiment
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], '1 star')

        # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], '3 stars')

if __name__ == '__main__': 
    print("Running Tests") 
    unittest.main()
