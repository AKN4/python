import time

basla= int(time.time())

cevap=input ("merhaba yazın:")

bitiş=int (time.time())

print ("merhaba kelimesini {} saniyede girdin".format(bitiş-basla))
