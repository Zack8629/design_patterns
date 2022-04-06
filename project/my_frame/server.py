import webbrowser
from wsgiref.simple_server import make_server


class Server:
    def __init__(self, app, ip_address='0.0.0.0', port=8000):
        self.ip_address = ip_address
        self.port = port
        self.app = app

    def _open_browser(self):
        webbrowser.open(f'{self.ip_address}:{self.port}')

    def run(self, open_browser=False):
        with make_server(host=self.ip_address, port=self.port, app=self.app) as httpd:
            print(f'The server is running at {self.ip_address}:{self.port}...')

            if open_browser:
                self._open_browser()

            httpd.serve_forever()
