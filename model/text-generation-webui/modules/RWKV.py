import os
from pathlib import Path

import numpy as np

import modules.shared as shared

np.set_printoptions(precision=4, suppress=True, linewidth=200)

os.environ['RWKV_JIT_ON'] = '1'
os.environ["RWKV_CUDA_ON"] = '0' #  '1' : use CUDA kernel for seq mode (much faster)

from rwkv.model import RWKV
from rwkv.utils import PIPELINE, PIPELINE_ARGS


class RWKVModel:
    def __init__(self):
        pass

    @classmethod
    def from_pretrained(self, path, dtype="fp16", device="cuda"):
        tokenizer_path = Path(f"{path.parent}/20B_tokenizer.json")

        if shared.args.rwkv_strategy is None:
            model = RWKV(model=os.path.abspath(path), strategy=f'{device} {dtype}')
        else:
            model = RWKV(model=os.path.abspath(path), strategy=shared.args.rwkv_strategy)
        pipeline = PIPELINE(model, os.path.abspath(tokenizer_path))

        result = self()
        result.pipeline = pipeline
        return result

    def generate(self, context, token_count=20, temperature=1, top_p=1, alpha_frequency=0.25, alpha_presence=0.25, token_ban=[0], token_stop=[], callback=None):
        args = PIPELINE_ARGS(
            temperature = temperature,
            top_p = top_p,
            alpha_frequency = alpha_frequency, # Frequency Penalty (as in GPT-3)
            alpha_presence = alpha_presence, # Presence Penalty (as in GPT-3)
            token_ban = token_ban, # ban the generation of some tokens
            token_stop = token_stop
        )

        return context+self.pipeline.generate(context, token_count=token_count, args=args, callback=callback)
