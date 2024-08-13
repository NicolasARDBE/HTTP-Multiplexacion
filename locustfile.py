from locust import HttpUser, task, between

class WebsiteUser(HttpUser):

    @task
    def load_test(self):
        self.client.get("/")  # Enviar una solicitud GET al servidor