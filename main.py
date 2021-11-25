import random
def son_ber():
    return random.randrange(50, 100)
def input_ol():
    return int(input("Sonni taxmin qilib ko'ring: "))
def son_kattaroq():
    print(f"Tasodifiy son {son}dan katta ")
def son_kichikroq():
    print(f"Tasodifiy son {son}dan kichik ")
def son_topildi():
    print("Sonni topdingiz!")
a = son_ber()
while True:
    son = input_ol()
    if son < a:
        son_kattaroq()
    elif son > a:
        son_kichikroq()
    else:
        son_topildi()
        break