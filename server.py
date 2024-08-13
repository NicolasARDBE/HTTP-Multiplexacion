from http.server import BaseHTTPRequestHandler, HTTPServer

# Contador global para las solicitudes
request_counter = 0

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global request_counter
        # Incrementar el contador de solicitudes
        request_counter += 1
        
        # Responder al cliente
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f"Request count: {request_counter}".encode("utf-8"))

# Configurar y correr el servidor en el puerto 8080
def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()