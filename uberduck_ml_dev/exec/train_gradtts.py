__all__ = ["parse_args", "run"]


import argparse
import json
import librosa  # NOTE(zach): importing torch before librosa causes LLVM issues for some unknown reason.
import sys

import torch
from torch import multiprocessing as mp

from ..trainer.gradtts import GradTTSTrainer
from ..vendor.tfcompat.hparam import HParams
from ..models.gradtts import DEFAULTS as GRADTTS_DEFAULTS


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to JSON config")
    args = parser.parse_args(args)
    return args


def run(rank, device_count, hparams):
    trainer = GradTTSTrainer(hparams, rank=rank, world_size=device_count)
    try:
        trainer.train()
    except Exception as e:
        print(f"Exception raised while training: {e}")
        # TODO: save state.
        raise e


try:
    from nbdev.imports import IN_NOTEBOOK
except:
    IN_NOTEBOOK = False
if __name__ == "__main__" and not IN_NOTEBOOK:
    args = parse_args(sys.argv[1:])
    config = GRADTTS_DEFAULTS.values()
    if args.config:
        with open(args.config) as f:
            config.update(json.load(f))
    hparams = HParams(**config)
    if hparams.distributed_run:
        device_count = torch.cuda.device_count()
        mp.spawn(run, (device_count, hparams), device_count)
    else:
        run(0, 1, hparams)
