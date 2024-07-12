import unittest

from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetector(unittest.TestCase):
    def test1(self):
        test_result1 = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(test_result1, "joy")
        test_result2 = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(test_result2, "anger")
        test_result3 = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(test_result3, "disgust")
        test_result4 = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(test_result4, "sadness")
        test_result5 = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(test_result5, "fear")



unittest.main()