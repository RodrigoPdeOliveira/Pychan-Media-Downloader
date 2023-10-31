
# Pychan Media Downloader

Download every media file found in a 4chan thread

## Usage/Examples

```
$ python main.py [-h] [-u URL | -f FILE] [-o OUTPUT]

options:
  -h, --help            Show this help message and exit
  -u, --url URL         4Chan thread URL
  -f, --file FILE       File with multiple urls
  -o, --output OUTPUT   Output path
```
### Download from one thread
```
$ python main.py -u https://boards.4channel.org/sci/thread/15828599
```

### Download from all threads in a file
```
$ python main.py -f ./example.txt
```
#### example.txt
```
https://boards.4channel.org/sci/thread/15828599
[...]
https://boards.4channel.org/sci/thread/5942502
```

### Change output path
```
$ python main.py -o ~/downloads -u https://boards.4channel.org/sci/thread/15828599
```
