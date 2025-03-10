# flake8: noqa
import os.path as osp

import hat.archs
import hat.data
import hat.models
from basicsr.train import train_pipeline
from accelerate import Accelerator

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    accelerator = Accelerator()
    train_pipeline(root_path)
