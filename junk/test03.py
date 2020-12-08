

from time import sleep


from dataStuff import timeDateStuff as TDS


print(TDS.now())
for sex in range(121):
	if sex % 10 == 0:
		print("+", end="")
	else:
		print(".", end="")
	sleep(1)
print(TDS.now())

