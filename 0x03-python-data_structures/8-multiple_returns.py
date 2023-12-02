#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        myTuple = ()
        if len(sentence) == 0:
            myTuple = None
        else:
            myTuple = len(sentence), sentence[0]
        return myTuple
