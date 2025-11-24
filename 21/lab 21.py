import requests

class JSONPlaceholderClient:
    def __init__(self):
        self.base_url = 'https://jsonplaceholder.typicode.com'

    # GET: Fetch all posts
    def get_posts(self):
        url = f'{self.base_url}/posts'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.reason}"

    # GET: Fetch a single post by ID
    def get_post(self, post_id):
        url = f'{self.base_url}/posts/{post_id}'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.reason}"

    # POST: Create a new post
    def create_post(self, title, body, user_id):
        url = f'{self.base_url}/posts'
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(url, json=payload)

        if response.status_code == 201:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.reason}"

client = JSONPlaceholderClient()

# Fetch all posts
posts = client.get_posts()
print(posts[:3])  # Print first 3 posts

# Fetch a single post
single_post = client.get_post(1)
print(single_post)

# Create a new post
new_post = client.create_post(
    title="Hello from Dhruv",
    body="This is my test post.",
    user_id=10
)
print(new_post)
