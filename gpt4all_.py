from gpt4all import GPT4All

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
print("1. Running...")
with model.chat_session():
    print("2. Running...")
    print(model.generate("You're a locally run LLM. Tell em about yourself", max_tokens=1024)) #max_tokens just cuts off the output

#dangerous? what happens if i dont give it a max_tokens? 
