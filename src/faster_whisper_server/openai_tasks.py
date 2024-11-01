

import os
from openai import OpenAI




class Local_OpenAIAPI:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("OPENAI_BASE_URL")
        self.openai_client = OpenAI(base_url=f"{self.base_url}", api_key=f"{self.api_key}")
        self.MODEL_NAME = "gpt-3.5-turbo"

    def text_proofreading(self, text: str):
        response = self.openai_client.chat.completions.create(
            model=self.MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "Please proofread. Please return only the proofreading results.",
                },
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0]["message"]["content"].strip()
