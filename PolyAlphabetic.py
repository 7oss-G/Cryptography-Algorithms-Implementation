import random

#This class contains 2 of the polyalphabetic ciphers: veginere and vernam

class PolyAlphabeticCiphers:
    char_array=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Dict={}
    veginere_base=None
    vigenere_key=None
    vernam_key=None
    def __init__(self):
        self.Update_text_to_number_mapping()
        
    def update_vigenere_base(self,base):
        self.veginere_base=base
        #self.veginere_base=input("Please Enter the Vegenere encryption key for this session:").upper()
    
         
    def Update_text_to_number_mapping(self):                                          #time complexity= O(n) here, n=26
#        random.shuffle(self.char_array)               #To have a diff text to number mapping each time    
        for i in range (0,len(self.char_array)):
            self.Dict[self.char_array[i]]=i            #keys=chars, values=numbers(also the indices of the key/char list)
        #print("Character-to-number mapping updated successfully.")
        #print("New char-to-number-mapping for this session is:")
        #print(self.Dict)
        return
    
    #n is already the index of the character in the global char_array
    def num_to_text(self,n):                                                          #time complexity= O(1)
        return self.char_array[n] 
    
    def Generate_key_vigenere(self, key,n_text): #where n_text is len(plain_text)     #same
        if (len(key)==n_text):
            return key
        elif (len(key)>n_text):
            return key[:n_text]
        else:
            Q=n_text//len(key)
            R=n_text%len(key)
            return (Q*key)+key[:R]
    
    #1 time key for vernam method:    
    def Generate_key_vernam(self,plain_text):                                         #time complexity= O(n)
        vernam_key=""
        for i in range (0,len(plain_text)):
            vernam_key=vernam_key+self.num_to_text(random.randint(0,9))
        print("vernam 1-timekey for this session is: "+vernam_key)
        return vernam_key
    
    def PolyAlphabeticEncryption(self,encryption_key,plain_text):                    #time complexity= O(n) 
        cipher_text=""
        count=0
        for i in plain_text:
            cipher_numeric=((self.Dict[i]+self.Dict[encryption_key[count]])%25)
            cipher_text=cipher_text+(self.num_to_text(cipher_numeric))
            count+=1
        print("The encrypted message is: "+cipher_text)
        return cipher_text
       
    def PolyAlphabeticDecryption(self,cipher_text,decryption_key):                   #time complexity= O(n)
        plain_text=""
        count=0
        for i in cipher_text:
            plain_numeric=((self.Dict[i]-self.Dict[decryption_key[count]])%25)
            plain_text=plain_text+(self.num_to_text(plain_numeric))
            count+=1
        print("The decrypted message is: "+plain_text)
        return plain_text         
        
    def Encrypt_vigenere(self,plain_text):
        #plain_text=input("Please Enter the plain text to be encrypted without spaces:").upper()    #time complexity= O(n)+O(1)
        #print("The plain text message is: "+ plain_text)
        self.vigenere_key=self.Generate_key_vigenere(self.veginere_base,len(plain_text))
        return self.PolyAlphabeticEncryption(self.vigenere_key,plain_text)
                 
    def Decrypt_vigenere(self,cipher_text):
        self.vigenere_key=self.Generate_key_vigenere(self.veginere_base,len(cipher_text))           #time complexity= same
        return self.PolyAlphabeticDecryption(cipher_text,self.vigenere_key)
            
    def Encrypt_vernam(self,plain_text):
        #plain_text=input("Please Enter the plain text to be encrypted without spaces:").upper()    #time complexity= O(n)+O(n)
        #print("The plain text message is: "+ plain_text)
        self.vernam_key=self.Generate_key_vernam(plain_text)
        return self.PolyAlphabeticEncryption(self.vernam_key,plain_text)       
                         
    def Decrypt_vernam(self,cipher_text):
        return self.PolyAlphabeticDecryption(cipher_text,self.vernam_key)                           #time complexity= O(n)+O(n)
    
        
        
        
            
"""         plain_text=""
        count=0
        for i in cipher_text:
            plain_numeric=((self.Dict[i]-self.Dict[vigenere_key[count]])%25)
            plain_text=plain_text+(self.num_to_text(plain_numeric))
            count+=1
        print("The decrypted message is: "+plain_text)
        return plain_text     """
    


"""         cipher_text=""
        count=0
        for i in plain_text:
            cipher_numeric=((self.Dict[i]+self.Dict[vigenere_key[count]])%25)
            cipher_text=cipher_text+(self.num_to_text(cipher_numeric))
            count+=1
        print("The encrypted message is: "+cipher_text)
        return cipher_text """          
            
        
        
            
        
    
#o1=PolyAlphabeticCiphers()





#o1.update_text_to_number_mapping()





""" print(o1.Generate_key_vigenere("hello",2))
print(o1.Generate_key_vigenere("hello",5))
print(o1.Generate_key_vigenere("hello",20))  """



""" print("Vigenere:")
o1.update_vigenere_base()
cipher1=o1.Encrypt_vigenere()
o1.Decrypt_vigenere(cipher1)
print("vernam:")
chipher2=o1.Encrypt_vernam()  """




""" print(x)
print(type(x)) """




#o1.Decrypt_vernam(chipher2)