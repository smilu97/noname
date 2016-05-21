import random

stack = {}
count = 0
while True :
	key = random.random()
	if stack.get(key, 0) == 0 :
		stack[key] = 1
		count += 1
	else :
		break
	if count % 1000 == 0 :
		print count
print count