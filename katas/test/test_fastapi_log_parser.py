import unittest
from katas.fastapi_log_parser import parse_fastapi_log

class TestFastAPILogParser(unittest.TestCase):

    def test_empty_Str(self):
        self.assertEqual(parse_fastapi_log(""), {})
    
    def test_no_match(self):
        self.assertEqual(parse_fastapi_log("My name is Tameer!"), {})
    
    def test_match(self):
        self.assertEqual(parse_fastapi_log('INFO:     127.0.0.1:54321 - "GET /api/users HTTP/1.1" 200 OK'), {
        "client_ip": "127.0.0.1",
        "client_port": "54321", 
        "http_method": "GET",
        "endpoint": "/api/users",
        "http_version": "1.1",
        "status_code": "200",
        "status_text": "OK"
    })

    
    
    