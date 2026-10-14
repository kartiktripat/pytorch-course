This repository is for me to learn Pytorch from scratch aimed at eventually making a project for my resume.
Steps to set up:
1. Tested on: macOS on Apple Silicon (M-series, 16 GB RAM), Python 3.13.5, PyTorch 2.14.1.
2. Create the virtual environment: python3 -m venv .venv
3. Activate it: source .venv/bin/activate. The prompt should now start with (.venv).
4. Install the packages: pip install -r requirements.txt
5. Check the install: python check.py. On Mac it prints the PyTorch version and True, which means the GPU (mps) is available. On other machines it may print False, which means the code will run on CPU.
