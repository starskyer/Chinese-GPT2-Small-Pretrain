# 把下面脚本放到文件 check_token_lengths.py 里运行
import json, sys
from tokenizations.tokenization_bert import BertTokenizer  # 根据项目路径调整
tok = BertTokenizer(vocab_file='cache/vocab_small.txt')

maxlen = 0
count = 0
big_examples = []
with open('data/novel/train.json','r',encoding='utf-8') as f:
    for i, line in enumerate(f):
        try:
            obj = json.loads(line)
        except:
            continue
        # text = obj.get('text') or obj.get('content') or obj.get('raw') or line
        text = line
        ids = tok.convert_tokens_to_ids(tok.tokenize(text))
        L = len(ids)
        if L > maxlen:
            maxlen = L
            big_examples.append((i, L, (text[:200]+'...') if len(text)>200 else text))
        count += 1
        if i % 10000 == 0 and i>0:
            print(f"processed {i} lines, current max {maxlen}")
print("total:", count, "max_token_len:", maxlen)
print("some biggest examples (index, len, head):", big_examples[-5:])
