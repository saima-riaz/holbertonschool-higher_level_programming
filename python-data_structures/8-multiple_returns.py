#!/usr/bin/python3
def multiple_returns(sentence):
    return (sentence[0], len(sentence)) if sentence else (None, 0)
