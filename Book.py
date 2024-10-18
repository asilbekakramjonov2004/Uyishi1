class book:
    def __init__(self, id, name, author, count, price):
        self.id = id
        self.nomi = name
        self.mualifi = author
        self.soni = count
        self.narx = price

    def filega_yozish(self):
        return f"""
Kitob IDsi:  {self.id}
Kitob nomi:  {self.nomi}
Kitob Mualifi: {self.mualifi}
Kitob soni:  {self.soni}
Kitob narxi: {self.narx}
"""

    def id_sonini_kamaytir(self, son):
        if son == self.id:
            self.soni-=1

    def id_ochirish(self, son):
        if son == self.id:
            return ""

#--------------------------------------------------------------------------------------
k1 = book(256, "Sapiens. A Brief History of Humankind", "Yuval Noax", 25, 120000)
k2 = book(365, "To Kill a Mockingbird", "Harper Lee", 30, 200000)
k3 = book(412, "Atomic Habits", "James Clear", 50, 100000)
k4 = book(523, "How to Stop Procrastinating", "Steve Scott", 46, 85000)
k5 = book(159, "The Richest Man in Babylon", "George Clason", 18, 250000)
k6 = book(264, "Thinking, Fast and Slow", "Daniel Kahneman", 75, 64000)
lst = [k1, k2, k3, k4, k5, k6]

with open("Kutubxona.txt", "w+") as f:
    for i in lst:
        f.write(f"{i.filega_yozish()}")
    
    def pr():    
        print("""
1. Kutubxonadagi kitoblar royxatini korish
2. Kitobni sotish
3. Kitobni sistemadan ochirish""")
        a = int(input(">>> "))
        if a == 1:
            f.seek(0)
            print(f.read())
            ortga = int(input("1. Ortga qaytish\n0. Tugatish\n"))
            if ortga:
                pr()
            else:
                return
        elif a == 2:
            f.seek(0)
            count = 0
            kamaytir = int(input("Sotmoqchi bolgan kitob ID sini kiriting: "))
            for i in lst:
                if i.id == kamaytir:
                    count+=1
                    i.id_sonini_kamaytir(kamaytir)
                f.write(f"{i.filega_yozish()}")
            print("Bizda bunday ID lik kitob mavjud emas" if count == 0 else "")
            ortga = int(input("1. Ortga qaytish\n0. Tugatish\n"))
            if ortga:
                pr()
            else:
                return
        elif a==3:
            f.truncate(0)
            count = 0
            ochir = int(input("Ochirmoqchi bolgan kitob ID sini kiriting: "))
            for i in lst:
                if i.id == ochir:
                    f.write(i.id_ochirish(ochir))
                else:
                    f.write(i.filega_yozish())
            print("Bizda bunday ID lik kitob mavjud emas" if count == 0 else "")
            ortga = int(input("1. Ortga qaytish\n0. Tugatish\n"))
            if ortga:
                pr()
            else:
                return
        else:
            print("Mavjud bo'lmagan bo'lim tanladingiz. Qaytadan urunib koring!!!")
            pr()
    pr()
    