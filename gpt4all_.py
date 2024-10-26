import argparse
from gpt4all import GPT4All

def main(prompt):
    model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM. Better function if it exists? 
    print("Let me think about that...")
    with model.chat_session():
        response = model.generate(prompt, max_tokens=1024)  # Limit tokens to avoid excessive output
        print(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="For running the GPT4All script via CLI")
    parser.add_argument("prompt", type=str, help="The prompt to send to llama")
    args = parser.parse_args()
    print(args)
    main(args.prompt)