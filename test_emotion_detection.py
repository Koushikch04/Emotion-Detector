import unittest

from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetector(unittest.TestCase):
    def test1(self):
        test_result1 = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(test_result1, "joy")
    def test2(self):
        test_result2 = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(test_result2, "anger")
    def test3(self):
        test_result3 = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(test_result3, "disgust")
    def test4(self):
        test_result4 = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(test_result4, "sadness")
    def test5(self):
        test_result5 = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(test_result5, "fear")



unittest.main()