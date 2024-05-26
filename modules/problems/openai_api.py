import openai
import os
import re

def evaluate_code(code, problem_title, problem_description):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    content = f"Review this Python code and rate it from 0 to 100 based on quality, style, and correctness:\n\n{code}\n\nThe problem is: {problem_title}\n\n{problem_description}"
    print(os.getenv("OPENAI_API_KEY"))
    messages = [
        {"role": "system", "content": "You are an assistant skilled in software engineering and code review."},
        {"role": "user", "content": content},
        {"role": "system", "content": "THE RESPONSE YOU CAN GIVE IS STRUCTURED AS FOLLOWS: 'Rating: XX / 100. Comments: ...'"},
        {"role": "assistant", "content": "Rating: 90 / 100. Comments: The code is well-structured and easy to read. It follows best practices and is free of errors."},
        {"role": "assistant", "content": "Rating: 70 / 100. Comments: The code is mostly correct, but there are some style issues that could be improved."},
        {"role": "assistant", "content": "Rating: 50 / 100. Comments: The code has some errors and is difficult to follow. It needs significant improvement."},
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=150
        )
        rating_text = response['choices'][0]['message']['content'].strip()
        print("Prompt:", content)
        print(f"Rating text: {rating_text}")

        score = 0
        comments = "No comments found."
        score_match = re.search(r'Rating: (\d+)', rating_text)
        comments_match = re.search(r'Comments: (.*)', rating_text)

        if score_match:
            score = int(score_match.group(1))
        if comments_match:
            comments = comments_match.group(1)

        return min(max(score, 0), 100), comments
    except Exception as e:
        print(f"Failed to evaluate code: {e}")
        return 0, "Error in processing the request."
