from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5.0, 9.0)
    
    @task
    def hello_world(self):
        self.client.get("/")