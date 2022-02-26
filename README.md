# [WIP] Response Measurer

A HTTP request response measurer

## Installation

```bash
pip install response-measurer
```

## Usage

```bash
$ response-measurer --help
usage: response-measurer [-h] [--version] {post,get} ...

a HTTP request response measurer

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit

subcommands:
  run one of the HTTP methods

  {post,get}  enter a request method
```

Also, you can run httpbin in your environment as a dummy HTTP Request & Response Service.

```bash
docker pull kennethreitz/httpbin
docker run -p 80:80 kennethreitz/httpbin
```

```bash
# Sample input and output
$ response-measurer post http://localhost/post --bytes 100000 --seed 5 --loop-count 5 --timeout 10 --output print 
[{'time': '2022-02-26T22:42:20.125598', 'name': 'random-string-post', 'method': 'post', 'mean': 0.0075218, 'P50': 0.006888, 'P99': 0.008008}]
[{'time': '2022-02-26T22:42:20.215853', 'name': 'random-string-post', 'method': 'post', 'result': 0.00675}, {'time': '2022-02-26T22:42:20.301020', 'name': 'random-string-post', 'method': 'post', 'result': 0.00768}, {'time': '2022-02-26T22:42:20.385517', 'name': 'random-string-post', 'method': 'post', 'result': 0.006888}, {'time': '2022-02-26T22:42:20.474916', 'name': 'random-string-post', 'method': 'post', 'result': 0.008283}, {'time': '2022-02-26T22:42:20.560010', 'name': 'random-string-post', 'method': 'post', 'result': 0.008008}]
```

## Use tox

Make sure you run `tox` command to keep the code up to the standard. 

```bash
pip install tox
```
