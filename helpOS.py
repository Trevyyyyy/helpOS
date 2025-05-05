#!/usr/bin/env python3
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")

def poser_question(question):
    completion = client.chat.completions.create(
        model="mistral-7b-instruct-v0.3",
        messages=[
            {"role": "user", "content": f"Tu es un expert Linux, spécialisé en EndeavourOS (Arch Linux). Réponds précisément, très brièvement et clairement à cette question. Mon ordinateur est en français : {question}"}
        ],
        temperature=0.2,
        max_tokens=500
    )

    return completion.choices[0].message.content.strip()

if __name__ == "__main__":
    question = input("Quelle est ta question sur EndeavourOS ?\n> ")
    reponse = poser_question(question)
    print(f"\nRéponse : {reponse}\n")
