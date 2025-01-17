# 🦆 Uberduck Text-to-Speech ![](https://img.shields.io/github/forks/uberduck-ai/uberduck-ml-dev) ![](https://img.shields.io/github/stars/uberduck-ai/uberduck-ml-dev) ![](https://img.shields.io/github/issues/uberduck-ai/uberduck-ml-dev)

[**Uberduck**](https://uberduck.ai/) is a tool for fun and creativity with neural text-to-speech. This repository will get you creating your own speech synthesis models. Please see our [**training**](https://colab.research.google.com/drive/1jF-Otw2_ssEcus4ISaIZu3QDmtifUvyY) and [**synthesis**](https://colab.research.google.com/drive/1wXWuhnw2pdfFy1L-pUzHfopW10W2GiJS) notebooks, and the [**Wiki**](https://github.com/uberduck-ai/uberduck-ml-dev/wiki).

## Overview

The main "Tacotron2" model in this repository is based on the NVIDIA Mellotron.  The main reasons to use this repository instead are

- simple fill-populating and rhythm predicting inference
- vocoders!
- more languages
- improved performance in fine tuning using additive covariates
- improved tensorboard logging
- all types of categorical covariates either supported or in progress (multispeaker, torchmoji, signal-to-noise ration, zero shot, pitch support)
- sensibly refactored, production tested code

## Usage

The notebooks are the easiest ways to try us out.

### Installation

If you want to install on your own machine, create a virtual environment and install like 

```bash
conda create -n 'uberduck-ml-dev' python=3.8
source activate uberduck-ml-dev
pip install git+https://github.com/uberduck-ai/uberduck-ml-dev.git
```

### Training

Please see the tests subfolder for examples of up to date training and inference invocation.

## Development

We love contributions! Feel free to reach out to discuss contribution.

### Installation

To install in development mode, run

```bash
pip install pre-commit black # format your code on commit by installing black!
git clone git@github.com:uberduck-ai/uberduck-ml-dev.git
cd uberduck-ml-dev
pre-commit install # Install required Git hooks
python setup.py develop # Install the library
```

### 🚩 Testing

In an environment or image with uberduck-ml-dev installed in the uberduck-ml-dev root folder, run 

```bash
python -m pytest
```
