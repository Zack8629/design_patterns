from app.fronts import fronts
from app.views import routes
from my_frame.main import Framework
from my_frame.server import Server

ip_address = '127.0.0.1'
port = 8000
open_browser = False

app = Framework(routes, fronts)

server = Server(ip_address=ip_address, port=port, app=app)
server.run(open_browser=open_browser)
