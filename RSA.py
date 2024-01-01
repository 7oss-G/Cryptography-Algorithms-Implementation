import random
#This class contains 1 of the practical ciphers: RSA
class RSA:
    primes=[] #to hold the primes used in key generation
    N=None
    phi=None
    e=None
    d=None
    char_array=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Dict={}
    
####defining some functions that will be useful later in the implementation:###
    def update_text_to_number_mapping(self):
#        random.shuffle(self.char_array)               #To have a diff text to number mapping each time
        
        for i in range (0,len(self.char_array)):
            self.Dict[self.char_array[i]]=i            #keys=chars, values=numbers(also the indices of the key/char list)
        #print("Character-to-number mapping updated successfully.")
        #print("new char-to-number-mapping is: ")
        #print(self.Dict)
        return

    def num_to_text(self,n):
        return self.char_array[n]
    
    def text_to_num(self,char):
        return self.Dict[char]

    def is_prime(self,a):                                                                        ##time complexity O(sqrt(a))
        if a==2:
            return True
        elif ((a<2) or (a%2==0)):
            return False
        else:
            for i in range(2,int(a**0.5)+1):
                if a %i ==0:
                    return False
            return True
    
    #To select a range for my prime numbers used in p&q                                        ##time complexity O((end-start)*sqrt(a))
    def update_primes(self, start, end):         
##        primes=[]
        for i in range (start,end):
            if (self.is_prime(i)):
                self.primes.append(i)       #append in the global primes list
        print("Primes list updated successfully with range from "+str(start)+" to "+str(end))
        print(self.primes)
        return 
    
    #steps 1&2 in choosing the key
    #start and end define the numeric range
    #function called to update N and phi each time
    
    def get_N_phi(self ):                                                                      ##time ocmplexity O(1)
        p=random.choice(self.primes)
        self.primes.remove(p)               #to make sure that p and q are never the same
        q=random.choice(self.primes)
        print("P= "+str(p))
        print("q= "+str(q))
        N=p*q
        phi=(p-1)*(q-1)  
        return N,phi
        
    #Greatest commpn divisor(euclidean algorithm):
    #Needed in get_coprime function
    def gcd(self,a,b):             #where a>b                                                 ##time complexity O(a/b)
        while b != 0:
            a,b= b, a%b
        return a
    
    #coprime check, to be used in choosing e                                                ##time complexity O(a**2)
    def get_coprimes_list(self,a,b):
        coprimes_list=[]
        x = min(a,b)   
        for num in range(2,x):
            if (self.gcd(a,num)==1) and (self.gcd(b,num)==1): 
                coprimes_list.append(num)
        if (len(coprimes_list) ==0):
            print("There are no possible coprimes for N and phi values")
        else:
            return coprimes_list

    def get_e(self):                                                                     
        comprimes=self.get_coprimes_list(self.N,self.phi)                               ##time complexity O(a**2)+O(phi*n)
        possible_e=[]
        for i in range (1,self.phi):
            if(i in comprimes):
                possible_e.append(i)
        if len(possible_e)==0:
            print("There is no possible e value. check again")
        else:
            e=random.choice(possible_e)
            return e
     #d is found by the extended euclidean algorithm as the modilous multiplicative inverse   
    def get_d(self,mod,e):                                                               ##time complexity O(a/b)
        a,b,T1,T2=mod,e,0,1
        while(b!=0):
            T=(T1-T2*(a//b)) % mod
            T1,T2=T2,T
            a,b=b,a%b
        return abs(T1)
    
    def generate_key_pairs(self):                                           ##time complexity O(1)+  O(a**2)+O(phi*n) +O(a/b)
        self.N,self.phi=self.get_N_phi()
        self.e=self.get_e()
        self.d=self.get_d(self.phi,self.e)
        print("N= "+ str(self.N))
        print("phi= "+  str(self.phi))
        print("e= "+ str(self.e))
        print("d= "+ str(self.d))
        
    def encrypt(self,plain_text):                                         ##time complexity =O(n)
        numeric_Value=[]
        cipher_numeric=[]
        for char in plain_text:
            numeric_Value.append(self.text_to_num(char))
        print("Plain_text is:"+ plain_text)
        for p_num in numeric_Value:
            cipher_numeric.append((p_num**self.e)%self.N)
        print("Cipher_numeric value after RSA encryption is:")
        print(cipher_numeric)
        return cipher_numeric
       
    def decrypt(self, cipher_numeric):                                  ##time complexity= O(n)
        plain_text_list=[]
        for ci_num in cipher_numeric:
            plain_text_list.append(self.num_to_text((ci_num**self.d) %self.N))
        plain_text="".join(plain_text_list)
        print("plain_text after RSA decryption is: "+plain_text)
        return plain_text
      
"""     def encrypt(self,plain_text):                                           ##time compelxity O(1)
        print("The plain_text numeric value is: "+str(plain_text))
        cipher_text=(int(plain_text)**self.e)%self.N
        print("Cipher text after RSA encryption is: "+ str(cipher_text))
        return cipher_text
         
    def decrypt(self, cipher_text):
        plain_text=(int(cipher_text)**self.d) %self.N
        print("Plain text numeric value after RSA decryption is: "+ str(plain_text))

        return plain_text """    


 #.............   
###.................................................TESTs......................................................
#

""" #Test1.............................................testing the char-num-mapping.............

o1.update_text_to_number_mapping()
print(o1.num_to_text(3))
"""
"""#Test2.................................................testing is_prime and update_primes
print(o1.is_prime(50))
print(o1.is_prime(11))
print(o1.is_prime(2))
print(o1.is_prime(1))
print(o1.is_prime(3))
o1.update_primes(20,70) """

""" #Test3...............................................N and phi...................
o1.update_primes(50,100)
print(o1.get_N_phi()) 

#Test4..................................................gcd and get_coprime

#print(o1.gcd(11,7))
print(o1.get_e()) """

""" #TEST5..................................................extended gdc to get_d()
print(o1.get_d(6,5))
print(o1.get_d(5,3))
print(o1.get_d(7,20))
 """
 
 #TEST_keys
 
 
o1=RSA()
o1.update_primes(2,50)
o1.generate_key_pairs()
o1.update_text_to_number_mapping()
plain_text=input("Kindly enter the value to be encrypted using RSA: ").upper()
cipher=o1.encrypt(plain_text)
o1.decrypt(cipher)

end=input("press enter to finish")





#o1.decrypt(o1.encrypt()
#Test Encryptin and Decryption
