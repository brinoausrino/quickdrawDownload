# quickdrawDownloader

Downloads quickdraw images from specified categories into seperate folders.

## Install

```
git pull https://github.com/brinoausrino/quickdrawDownloader
cd quickdrawDownloader
```

assume your using conda

```
conda create -n quickdrawDownloader
conda activate quickdrawDownloader
pip install -r requirements.txt
```

## Run

```
python create_training_set.py
```

## Customize

In `create_training_set.py` you find the folowwing options

* `categories`: categories to be downloaded -> can be found in categories.txt
* `n_samples` : number of samples for each category