# Downloads model(s) during docker build
from transformers import GPT2LMHeadModel, GPT2Tokenizer

#model_name = 'distilgpt2'

model_name = '1558M'

GPT2LMHeadModel.from_pretrained(model_name).save_pretrained('./gpt2')
GPT2Tokenizer.from_pretrained(model_name).save_pretrained('./gpt2')

