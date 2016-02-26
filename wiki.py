# coding: utf-8
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from itertools import chain

from errbot import BotPlugin, botcmd
import wikipedia


CONFIG_TEMPLATE = {'LANGUAGE': 'en',
                   'SUMMARY_MAX_LENGTH': 255}


class WikipediaPlugin(BotPlugin):
    """Basic Err integration with wikipedia.org"""

    min_err_version = '3.2.3'
    # max_err_version = '3.3.0'

    def get_configuration_template(self):
        return CONFIG_TEMPLATE

    def configure(self, configuration):
        if configuration is not None and configuration != {}:
            config = dict(chain(CONFIG_TEMPLATE.items(),
                                configuration.items()))
        else:
            config = CONFIG_TEMPLATE
        super().configure(config)
        return

    def activate(self):
        super().activate()
        if self.config['LANGUAGE'] in wikipedia.languages():
            wikipedia.set_lang(self.config['LANGUAGE'])
        else:
            self.log.warning('{0} is not a valid language code.'.format(
                self.config['LANGUAGE']))
        return

    @botcmd(split_args_with=None)
    def wiki_describe(self, mess, args):
        """Fetch the upcoming events for a from meetup.com."""
        if len(args) == 0:
            return 'What do you want me to describe ?'
        try:
            res = wikipedia.page(' '.join(args))
        except wikipedia.exceptions.DisambiguationError as e:
            return "Are you talking about {0} or {1} ?".format(
                ', '.join(e.options[:-1]), e.options[-1])
        except wikipedia.exceptions.PageError:
            return "No wikipedia entry found."
        return '{0} ({1})'.format(self.format_summary(res.summary), res.url)

    def format_summary(self, summary):
        return (summary[:self.config['SUMMARY_MAX_LENGTH']]+'...'
                if len(summary) > self.config['SUMMARY_MAX_LENGTH']
                else summary)
