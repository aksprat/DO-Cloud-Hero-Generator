import os
import requests

DO_AI_ENDPOINT = os.getenv("DO_AI_ENDPOINT")
DO_AI_KEY = os.getenv("DO_AI_KEY")


def generate_avatar(name):

    prompt = f"""
Ultra detailed cinematic superhero portrait of {name}, a futuristic AI cloud architect.

Style:
photorealistic, cinematic lighting, ultra detailed, 8k concept art,
marvel style superhero portrait, dramatic lighting

Scene:
{name} standing confidently as a powerful cloud hero controlling
AI infrastructure and cloud systems.

Environment:
floating Kubernetes clusters,
glowing neural network patterns,
cloud servers orbiting around,
data streams flowing through the sky,
futuristic Bangalore skyline at sunset,
digital particles and energy waves.

Hero suit:
futuristic tech armor with glowing blue highlights,
AI circuits embedded in the suit,
energy core on chest.

Atmosphere:
epic lighting,
cinematic depth of field,
heroic pose.

Footer text:
Generated with DigitalOcean Serverless Inference
CloudConf Bangalore
"""

    payload = {
        "prompt": prompt,
        "num_images": 1
    }

    headers = {
        "Authorization": f"Bearer {DO_AI_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        DO_AI_ENDPOINT,
        headers=headers,
        json=payload
    )

    return response.json()