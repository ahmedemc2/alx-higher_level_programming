#!/usr/bin/python3
def multiple_returns(sentence):
    myTuple = ()
    if len(sentence) > 0:
        myTuple = len(sentence), sentence[0]
    else:
        myTuple = 0, "None"
    return myTuple
