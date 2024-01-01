#This class contain substitution ciphers: Monoalphabetic cipher
class MonoAlphabetic:
    char_array=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    substitution_Dict={}
    key=None
    

    def update_key(self,sym_key):
        self.key=sym_key
        #self.key=input("Please Enter the key for this session:").upper()
    
    def update_Txt_to_num_mapping(self):
        s=[]
        count=0
        for char in self.key:                                                                  #time_complexity=O(n)
            if (char not in s):
                s.append(char)
                self.substitution_Dict[self.char_array[count]]=char
                count+=1
            else:
                continue
        for char in self.char_array:
            if (char not in s):
                self.substitution_Dict[self.char_array[count]]=char
                count+=1
        print("The substitution dictionary for this session is: ")
        print(self.substitution_Dict)
        return self.substitution_Dict
    
    def MonoAlphabeticEncryption(self,plain_text):
        #plain_text=input("Please enter the plain text without spaces: ").upper()            #time_compexity=O(n)
        cipher_text=""
        for char in plain_text:
            cipher_text=cipher_text+self.substitution_Dict[char]
        print("The ciphertext is: " + cipher_text)
        return cipher_text
    
    def MonoAlphabeticDecryption(self,cipher_text):                                         #time complexity= O(n)
        plain_text=""
        for char in cipher_text:
            plain_text=plain_text+list(self.substitution_Dict.keys())[list(self.substitution_Dict.values()).index(char)]
        print("The plain text is: "+ plain_text)
        return plain_text
    
"""     def __init__(self):
        print("Monoalphabetic cipher:") """
            
    
""" o1=MonoAlphabetic()
o1.update_Dictionary()
cipher=o1.Encrypt()
o1.Decrypt(cipher) """
                
        