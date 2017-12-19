# import mysql
# import numpy
from random import random

def gen_rand():
	nums = [random() * 10 for i in range(13)]
	return nums

def get_max_percentage(percent):

	# cxn = mysql.connector.connect(user='root', database='numbers', passwd='qwerty')

	# cur = cnx.cursor(buffered=True)
	# cur.execute("SELECT nb FROM numbers.num")
	# results = [i[0] for i in  cur.fetchall()]
	# cur.close()

	results = gen_rand()
	results.sort()
	# print(results)
	index = (len(results) * percent) // 100
	return results[index]

if __name__ == '__main__':
	val = get_max_percentage(25)
	print(val)