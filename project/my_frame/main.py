from quopri import decodestring

from my_frame.requests import PostRequests, GetRequests


class PageNotFound404:
    def __call__(self, request):
        return '404 Not Found', '404 Page Not Found'


class Framework:
    def __init__(self, routes, fronts):
        self.routes_lst = routes
        self.fronts_lst = fronts

    def __call__(self, environ, start_response):
        request = {}
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'POST: {Framework.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'GET: {request_params}')

        if path not in self.routes_lst:
            view = PageNotFound404()
        else:
            view = self.routes_lst[path]

        for front in self.fronts_lst:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(raw_data):
        ready_data = {}
        for key, val in raw_data.items():
            val = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            ready_data[key] = val_decode_str
        return ready_data
