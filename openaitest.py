from transformers import pipeline
generator=pipeline('text-generation',model='EleutherAI/gpt-neo-2.7B')
prompt="Write a code to find even odd number"
res=generator(prompt,max_length=100,do_sample=True,temperature=0.9,pad_token_id=generator.tokenizer.eos_token_id)
print(res)