# [WIP] Response Measurer

A simple python HTTP request response measurer

## Installation

```bash
pip install response-measurer
```

## Usage

```bash
response-measurer --help

response-measurer --host http://httpbin.org/post --loop-count 5 --timeout 10 --log-level DEBUG post
```

Also, you can run httpbin in your environment as a dummy HTTP Request & Response Service.

```bash
docker pull kennethreitz/httpbin
docker run -p 80:80 kennethreitz/httpbin
```

```bash
response-measurer --host http://localhost/post --loop-count 5 --timeout 10 --log-level DEBUG post
```
