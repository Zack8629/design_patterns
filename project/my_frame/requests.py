class RawDataRequests:
    @staticmethod
    def parse_input_data(raw_data):
        ready_data = {}
        if raw_data:
            params = raw_data.split('&')
            for item in params:
                key, val = item.split('=')
                ready_data[key] = val
        return ready_data


class GetRequests(RawDataRequests):
    @staticmethod
    def get_request_params(environ):
        query_string = environ['QUERY_STRING']
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


class PostRequests(GetRequests):
    @staticmethod
    def get_wsgi_input_data(env):
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0

        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
