import threading
import time
def walk_dog():
    time.sleep(5)
    print("walk the dog!! \n")


def take_trash():
    time.sleep(2)
    print("take out the trash!!\n")


def get_mail(boss):
    time.sleep(5)
    print(f"take out the mail!!, sent by {boss}\n")


work1 = threading.Thread(target=walk_dog)
work1.start()

work2 = threading.Thread(target=take_trash)
work2.start()

work3 = threading.Thread(target=get_mail, args=("lawda",))
work3.start()

work1.join()
work2.join()
work3.join()

print("all works are complete")