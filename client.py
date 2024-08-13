import requests
import threading

# Función que cada hilo ejecutará
def send_request():
    try:
        response = requests.get("http://localhost:8080")
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

# Función principal para crear y lanzar hilos
def simulate_requests(n):
    threads = []
    for _ in range(n):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()
    
    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Número de solicitudes a simular
    n = 10000
    simulate_requests(n)