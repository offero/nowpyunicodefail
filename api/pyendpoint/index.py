from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            post_body = self.rfile.read(int(self.headers['content-length'])).decode('utf-8')
            name = post_body['name']
            print(post_body)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response_data = {'greeting': f'hello {name}'}
            self.wfile.write(json.dumps(response_data, sort_keys=True, indent=2).encode('utf-8'))
        except Exception as err:
            print("error while sending response")
            print(err)
            self.send_error(500)
            raise
        return
