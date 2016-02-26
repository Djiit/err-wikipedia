# coding: utf-8
from errbot.backends.test import testbot

import wiki


class TestWikipediaPlugin(object):
    extra_plugin_dir = '.'

    def test_meetup_describe_no_args(self, testbot):
        testbot.push_message('!wiki describe')
        assert ('What do you want me to describe ?'
                in testbot.pop_message())

    def test_meetup_describe(self, testbot):
        testbot.push_message('!wiki describe notaword')
        assert ('No wikipedia entry found.'
                in testbot.pop_message())
