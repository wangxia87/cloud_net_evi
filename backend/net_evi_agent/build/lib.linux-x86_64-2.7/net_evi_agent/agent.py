#!/usr/bin/python
import classes

def getReqFromController():
	task=classes.Compute()
	task.receive()

getReqFromController()
