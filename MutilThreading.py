import threading
def hi(name):
    while 1:
        print("你好",name)
def world(msg):
    while 1:
        print("世界",msg)
thread_obj1=threading.Thread(target=hi,args=("shibi",))
thread_obj2=threading.Thread(target=world,kwargs={"msg":"hi"})
thread_obj1.start()
thread_obj2.start()