from collections import defaultdict


class Navnlist:

    def __init__(self):
        self.names = []

        #sort navn
        self.fileread()
        self.display_name()

        #collections A_Z
        self.letter_count = defaultdict(int)
        self.count_letter()
        self.display_name_count()
        self.process_names()

    def fileread(self):
        try:
            with open('Data/Navne_liste.txt',"r",encoding="utf-8") as file:
                self.names = file.read().strip().split(",")
        except FileNotFoundError:
            print("can't found document")
        except Exception as e:
            print("an error Excepotion" + e)

    def display_name(self):
        if self.names:
            self.names.sort(key=len)
            names = self.sorted_name_amount(self.names,10)
            print(names)
        else:
            print("no names available")

    def sorted_name_amount(self,query,number):
       return ",".join(query[:number])
        
        
    def count_letter(self):
        for name in self.names:
            for letter in name:
                self.letter_count[letter.lower()] +=1
    
    def get_name_count(self):
        return len(self.names)
    
    def display_name_count(self):
        for name,count in sorted(self.letter_count.items()):
            print(f"name: {name}  count:  {count}")
    
    def process_names(self):
        for name in self.names[:10]:
            print(f"Name: {name}")
            for letter in name:
                print(f"Letter: {letter}")
Navnlist()


    
        