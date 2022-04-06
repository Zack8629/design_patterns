from time import time


class LinkCreation:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()


class Debugger:
    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def name_cls(run_cls):
            def timed(*args, **kw):
                time_start = time()
                result = run_cls(*args, **kw)
                time_end = time()
                lead_time = time_end - time_start

                print(f'Debugger: lead time {self.name} = {lead_time:.2f} ms')
                return result

            return timed

        return name_cls(cls)
