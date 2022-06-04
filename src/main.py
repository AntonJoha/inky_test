from extract import set_page
import time

while True:
    set_page(401)
    time.sleep(4*60)
    for i in range(105,200):
        try:
            set_page(i)
            time.sleep(4*60)
        except:
            print("Error " + str(i))
