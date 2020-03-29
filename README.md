# **t** is for terminal

iTerm2 automated configuration. Stop configuring your terminals or setting up your environment

t is a very simple utility that allows you to set your terminal configurations and layout and run specific commands in each properly named tabs. t keeps track of terminal and processes it created and also allows you to shut everything down gracefully or forcefully.

Be in control of your setup, trust it, forget about it and focus on your tasks.

## Usage

```
Usage: t [OPTIONS] COMMAND

Setup, management and deployment of alf for developers

Commands:
  start		Start the docker containers, api & dashboard
  stop		Stop the docker containers, api & dashboard
  help		display this page
```

## Example

```bash
$ t start "docker-compose up@docker" "cd front;yarn start@front" "cd back;yarn start@back"
```

Will create a new iTerm window with 3 tabs:

- The first tab will be named **docker** and will run **docker-compose up**
- The second tab will be named **front** and will go to the front subdirectory and run **yarn start**
- The third tab will be named **back** and will go to the back subdirectory and run **yarn start**

## System Dependencies

**t** relies the [iterm2](https://pypi.org/project/iterm2/) python package

iterm2 relies on [iTerm](https://www.iterm2.com/) 3.3.10 or higher

iTerm [python scripting API](https://www.iterm2.com/python-api/) must be enabled

Follow [the tutorial here](https://www.iterm2.com/python-api/tutorial/index.html#tutorial-index) that will guide you to enabling it

## Installation

urllib3 can be installed with [pip](https://pip.pypa.io/):

```bash
$ pip install t
```

Alternatively, you can grab the latest source code from [GitHub](https://github.com/urllib3/urllib3):

```bash
$ git clone git://github.com/michakfromparis/t.git
$ python setup.py install
```

## Documentation

t has usage and reference documentation at [t.readthedocs.io](https://t.readthedocs.io/).

Say Thanks! This is simple and keeps me motivated to make improvements

## Contributing

t happily accepts contributions. Please see our [contributing documentation](https://urllib3.readthedocs.io/en/latest/contributing.html) for some tips on getting started.

## Security Disclosures

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security). Tidelift will coordinate the fix and disclosure with maintainers.

## Maintainers

- [@michakfromparis](https://github.com/michakfromparis) (Michel Courtine)



[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/michel.courtine@docker.com)