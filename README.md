# iterm-magic: **t** is for terminal

**iTerm2** automated configuration. Stop configuring your terminals or setting up your environment.

**iterm-magic** is a very simple utility that allows you to define your terminal configurations and layout for a specific project and run **specific commands** in each **properly named tabs**. **t** keeps track of terminals and processes it creates and allows you to shut everything down **gracefully** or **forcefully**.

Be in control of your setup, trust it, forget about it and **focus on your tasks**.

## Usage

```
Usage: iterm-magic [OPTIONS] COMMAND

iTerm2 automated configuration

Commands:
  start		Start commands in named tabs or named configuration
  stop		Stop commands and close opened tabs / windows
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

## Say Thanks!

[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/michel.courtine@docker.com)

Simply **click on the icon above** to let me know you like it. Takes less than a minute.<br/>
This is simple and keeps me motivated to make improvements

## System Dependencies

**iterm-magic** relies on the [iterm2](https://pypi.org/project/iterm2/) python package<br/>
iterm2 relies on [iTerm](https://www.iterm2.com/) **3.3.10** or higher<br/>
iTerm [python scripting API](https://www.iterm2.com/python-api/) must be enabled<br/>
Follow [the tutorial here](https://www.iterm2.com/python-api/tutorial/index.html#tutorial-index) that will guide you to enable it<br/>

## Installation

**t** can be installed with [pip](https://pip.pypa.io/):

```bash
$ pip install iterm-magic
```

Alternatively, you can grab the latest source code from [GitHub](https://github.com/michakfromparis/iterm-magic):

```bash
$ git clone git://github.com/michakfromparis/iterm-magic.git
$ cd iterm-magic
$ python setup.py install
```

### Documentation

[![Documentation Status](https://readthedocs.org/projects/iterm-magic/badge/?version=latest)](https://iterm-magic.readthedocs.io/en/latest/?badge=latest)

iterm-magic has usage and reference documentation at [iterm-magic.readthedocs.io](https://iterm-magic.readthedocs.io/).<br/>
Say Thanks! This is simple and keeps me motivated to make improvements

### Contributing

**iterm-magic** happily accepts contributions. Please see our [contributing documentation](https://iterm-magic.readthedocs.io/en/latest/contributing.html) for some tips on getting started.

### Security Disclosures

To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security).<br/>
Tidelift will coordinate the fix and disclosure with maintainers.

### Maintainers

- [@michakfromparis](https://github.com/michakfromparis) (Michel Courtine)

### Credits

Infinite thanks to George Nachman ([@gnachman](https://github.com/gnachman)) for brewing OSX's favorite terminal for so many years and opening the scripting API to python after years of solid AppleScripting (not sure solid was the right word).
