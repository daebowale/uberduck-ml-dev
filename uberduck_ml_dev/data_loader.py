__all__ = [
    "pad_sequences",
    "prepare_input_sequence",
]

# TODO (Sam): move these to text.

import torch

from .text.symbols import (
    NVIDIA_TACO2_SYMBOLS,
)
from .text.util import text_to_sequence


def pad_sequences(batch):
    input_lengths = torch.LongTensor([len(x) for x in batch])
    max_input_len = input_lengths.max()

    text_padded = torch.LongTensor(len(batch), max_input_len)
    text_padded.zero_()
    for i in range(len(batch)):
        text = batch[i]
        text_padded[i, : text.size(0)] = text

    return text_padded, input_lengths


def prepare_input_sequence(
    texts,
    cpu_run=False,
    arpabet=False,
    symbol_set=NVIDIA_TACO2_SYMBOLS,
    text_cleaner=["english_cleaners"],
):
    p_arpabet = float(arpabet)
    seqs = []
    for text in texts:
        seqs.append(
            torch.IntTensor(
                # NOTE (Sam): this adds a period to the end of every text.
                text_to_sequence(
                    text,
                    text_cleaner,
                    p_arpabet=p_arpabet,
                    symbol_set=symbol_set,
                )[:]
            )
        )
    text_padded, input_lengths = pad_sequences(seqs)
    if not cpu_run:
        text_padded = text_padded.cuda().long()
        input_lengths = input_lengths.cuda().long()
    else:
        text_padded = text_padded.long()
        input_lengths = input_lengths.long()

    return text_padded, input_lengths
