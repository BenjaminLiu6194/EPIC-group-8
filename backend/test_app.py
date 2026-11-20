import unittest
from unittest.mock import patch
from app import app, QUESTIONS
class DemoTests(unittest.TestCase):
 def setUp(self): self.client=app.test_client()
 def test_questions(self): self.assertEqual(len(self.client.get('/api/questions').json),3)
 def test_unknown(self): self.assertEqual(self.client.post('/api/compare',json={'questionId':'bad'}).status_code,404)
 def test_empty(self): self.assertEqual(self.client.post('/api/compare',json={'questionId':'0','response':''}).status_code,400)
 @patch.dict('os.environ',{'OPENAI_API_KEY':''})
 def test_cached(self):
  d=self.client.post('/api/compare',json={'questionId':'0','response':QUESTIONS[0]['examples'][0]['response']}).json
  self.assertEqual(d['basic']['total'],3)
  self.assertEqual(d['aligned']['total'],5)
 @patch.dict('os.environ',{'OPENAI_API_KEY':''})
 def test_custom_requires_key(self): self.assertEqual(self.client.post('/api/compare',json={'questionId':'0','response':'custom'}).status_code,503)
