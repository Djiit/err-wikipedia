# err-wikipedia - wikipedia.com plugin for Err

[![Build Status](https://travis-ci.org/Djiit/err-meetup.svg?branch=master)](https://travis-ci.org/Djiit/err-wikipedia) [![Coverage Status](https://coveralls.io/repos/github/Djiit/err-wikipedia/badge.svg?branch=master)](https://coveralls.io/github/Djiit/err-wikipedia?branch=master)

Err-wikipedia is a plugin for [Err](https://github.com/gbin/err) that allows you to interact with [wikipedia.org](http://wikipedia.org).

## Features

* Fetch the summary of a Wikipedia page, optionally cropping it if it's too long.
* Set your language in the plugin configuration.
* Support AUTOINSTALL_DEPS thanks to the `requirements.txt` file.

Have an idea ? Open an [issue](https://github.com/Djiit/err-meetup/issues) or send me a [Pull Request](https://github.com/Djiit/err-meetup/pulls).

## Usage

### Installation

As admin of an err chatbot, send the following command over XMPP:

```
!repos install https://github.com/Djiit/err-wikipedia.git
```

### Commands

Use `!help Wikipedia` to see the available commands and their explanation.

## Configuration

Send configuration commands through chat message to this plugins as in :

```
!plugin config Wikipedia {'LANGUAGE': 'fr', 'SUMMARY_MAX_LENGTH': 255}
```
