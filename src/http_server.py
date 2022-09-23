import http
from http.server import BaseHTTPRequestHandler,HTTPServer
from io import BytesIO
from urllib.parse import unquote
from qr_Test import info

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        if not self.path.startswith("/qr"):
            self.send_response(500)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Bruh")
            return
        path = unquote(str(self.path)[4:])

        print(self.path)
        self.send_response(200)
        self.send_header('content-type','image/png')
        self.end_headers()

        img = info(path)
        # print(img.tobytes())
        # self.wfile.write(b"hello !")


        f_bytes = BytesIO()
        f_bytes: BytesIO
        img.save(fp=f_bytes, format="png")
        bytar = f_bytes.getbuffer().tobytes()
        self.wfile.write(bytar)



serv = HTTPServer(("0.0.0.0",8088),HttpProcessor)
serv.serve_forever()