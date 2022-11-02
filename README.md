This repository contains different branches where I have experimented with different pieces of technologies:

## Installation

```
git clone https://github.com/qmqasim99/integrate_scanning_modules.git
```

## Running

You would only need Docker to run this repository.
Move to the relevant branch and run with `docker-compose up --build `

## sublister_submodule

In this branch, I was experimenting adding 3rd party repositories into my project, such as [Sublist3r](https://github.com/aboul3la/Sublist3r 'Sublist3r')

## add_amass

In this branch, I was experimenting integrating a CLI tool written in Go within our Python app.
I have integrated [OWASP's Amass tool](https://github.com/OWASP/Amass 'Amass')

## add_redis

In this branch, I improve my app by adding caching to the API.

## add_celery:

In this branch, I add further improvements to the app by adding background task handler - Celery
