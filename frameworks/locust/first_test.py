from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    """
    This user will make an HTTP request to /hello, then to /world, and then repeat. 
    For a full explanation and a more realistic example see Writing a locustfile.
    """
    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/api")