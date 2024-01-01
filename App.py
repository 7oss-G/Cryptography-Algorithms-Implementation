import tkinter as tk
import customtkinter as ctk
import MonoAlphabetic as ma
import PolyAlphabetic as pa

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Class for the application and the GUI

class App(ctk.CTk,ma.MonoAlphabetic,pa.PolyAlphabeticCiphers):
    
    #This is the GUI specifications, all initiated in the default constructor __init_-
    def __init__(self):
        super().__init__()  
    #app=ctk.CTk()
        self.title("Cryptogtahpy Tool")
        self.geometry("500x500")
    #frame=ctk.CTkFrame(master=app)
    #frame.pack()
    #frame.pack(pady=20,padx=20,fill="both",expand=True)  
        self.user_text_label=ctk.CTkLabel(master=self,text="Plaintext")
        self.user_text_label.grid(row=0, column=0,pady=15,padx=10)
        self.user_text_entry=ctk.CTkEntry(master=self,placeholder_text="Letters only(no spaces)",width=250)
        self.user_text_entry.grid(row=0, column=1,columnspan=5,pady=15,padx=10)
        self.symmetric_key_label=ctk.CTkLabel(master=self,text="Symmetric key")
        self.symmetric_key_label.grid(row=1, column=0,pady=15,padx=10)
        self.symmetric_key_entry=ctk.CTkEntry(master=self,placeholder_text="Letters only(no spaces)",width=250)
        self.symmetric_key_entry.grid(row=1, column=1,columnspan=5,pady=15,padx=10)
        #RSA_checkbox=ctk.CTkCheckBox(master=frame,text="RSA")
        
        self.checkboxVar = tk.StringVar(value="Vigenere")
        
        self.vigenere_checkbox=ctk.CTkCheckBox(master=self,text="Vigenere",variable=self.checkboxVar,onvalue="1",offvalue="0")
        self.vernam_checkbox=ctk.CTkCheckBox(master=self,text="Vernam",variable=self.checkboxVar,onvalue="01",offvalue="00")
        self.monoalphabetic_checkbox=ctk.CTkCheckBox(master=self,text="MonoAlphabetic",variable=self.checkboxVar,onvalue="001",offvalue="000")
        #RSA_checkbox.grid(row=2, column=0,pady=15,padx=10)
        self.vigenere_checkbox.grid(row=2, column=0,pady=15,padx=10)
        self.vernam_checkbox.grid(row=2, column=1,pady=15,padx=10)
        self.monoalphabetic_checkbox.grid(row=2, column=2,pady=15,padx=10)
        self.result=ctk.CTkTextbox(master=self,width=200,height=200)
        self.result.grid(row=8, column=0,columnspan=9,sticky="nsew", pady=15, padx=20)
        self.Encrypt_button=ctk.CTkButton(master=self, text="Encrypt",command=self.Encrypt)
        self.Encrypt_button.grid(row=3,column=0, pady=15, padx=10)
        
        self.Decrypt_button=ctk.CTkButton(master=self, text="Decrypt",command=self.Decrypt)
        self.Decrypt_button.grid(row=3,column=1, pady=15, padx=10)
        
        self.clear_res_button=ctk.CTkButton(master=self, text="clear",command=self.clear_res)
        self.clear_res_button.grid(row=3,column=2, pady=15, padx=10)
    #app.mainloop()
    
#rsa=RSA_checkbox.get()

    def clear_res(self):
        self.result.delete(index1="0.0", index2="50.0")
    
    def vig_Encryption(self):
        user_txt=self.user_text_entry.get().upper()
        self.Update_text_to_number_mapping()
        #vigenere_key=self.Vigenere_key_entry.get().upper()
        #self.update_vigenere_base(vigenere_key)
        cipher=self.Encrypt_vigenere(user_txt)
        self.result.insert(index="2.0",text="Encrypted Cipher text is: "+ cipher+"\n")
        return cipher
    
    def vig_Decryption(self):
        #vig_key=self.symmetric_key_entry.get().upper()
        user_txt=self.user_text_entry.get().upper()
        self.Update_text_to_number_mapping()
        #self.update_vigenere_base(vig_key)
        plaintxt=self.Decrypt_vigenere(user_txt)
        self.result.insert(index="4.0",text="Decrypted plain text is: "+ plaintxt+"\n")
        return plaintxt
    
    def vernam_Encryption(self):
        user_txt=self.user_text_entry.get().upper()
        self.Update_text_to_number_mapping()
        cipher=self.Encrypt_vernam(user_txt)
        self.result.insert(index="7.0",text="Encrypted Cipher text is: "+ cipher+"\n")
        return cipher
    
    def vernam_Decryption(self):
        user_txt=self.user_text_entry.get().upper()
        self.Update_text_to_number_mapping()
        plaintxt=self.Decrypt_vernam(user_txt)
        self.result.insert(index="7.0",text="Decrypted plain text is: "+ plaintxt+"\n")
        return plaintxt
              
    
    def monoalphabetic_Encryption(self):
        user_txt=self.user_text_entry.get().upper()
        self.update_Txt_to_num_mapping()
        cipher=self.MonoAlphabeticEncryption(user_txt)
        self.result.insert(index="11.0",text="Encrypted Cipher text is: "+ cipher+"\n")
        return cipher
    
    def monoalphabetic_Decryption(self):
        user_txt=self.user_text_entry.get().upper()
        self.update_Txt_to_num_mapping()
        plaintxt=self.MonoAlphabeticDecryption(user_txt)
        self.result.insert(index="11.0",text="Decrypted plain text is: "+ plaintxt+"\n")
        return plaintxt
        

    def Encrypt(self):
        #vernam=self.vernam_checkbox.get()
        #monoalphabetic=self.monoalphabetic_checkbox.get()
        if (self.vigenere_checkbox.get()=="1"):
            vig_key=self.symmetric_key_entry.get().upper()
            #user_txt=self.user_text_entry.get().upper()
            self.result.insert(index="0.0",text="Vigenere:\n")
            self.update_vigenere_base(vig_key)
            self.vig_Encryption()
            
        if (self.vernam_checkbox.get()=="01"):
            self.result.insert(index="5.0",text="Vernam:\n")
            self.vernam_Encryption()
          
        if (self.monoalphabetic_checkbox.get()=="001"):
            mono_key=self.symmetric_key_entry.get().upper()
            self.result.insert(index="9.0",text="MonoAlphabetic:\n")
            self.update_key(mono_key)
            self.monoalphabetic_Encryption()
            
        elif(self.vigenere_checkbox.get()=="0" and self.vernam_checkbox.get()=="00" and self.monoalphabetic_checkbox.get()=="000"):
            self.result.insert(index="0.0",text="nohting. Please select a method for Encryption/Decryption. ")
        return
    
    def Decrypt(self):
                #vernam=self.vernam_checkbox.get()
        #monoalphabetic=self.monoalphabetic_checkbox.get()
        if (self.vigenere_checkbox.get()=="1"):
            vig_key=self.symmetric_key_entry.get().upper()
            #user_txt=self.user_text_entry.get().upper()
            self.result.insert(index="0.0",text="Vigenere:\n")
            self.update_vigenere_base(vig_key)
            self.vig_Decryption()
            
        if(self.vernam_checkbox.get()=="01"):
            self.result.insert(index="5.0",text="Vernam:\n")
            self.vernam_Decryption()
            
        if (self.monoalphabetic_checkbox.get()=="001"):
            mono_key=self.symmetric_key_entry.get().upper()
            self.result.insert(index="9.0",text="MonoAlphabetic:\n")
            self.update_key(mono_key)
            self.monoalphabetic_Decryption()
            
        elif(self.vigenere_checkbox.get()=="0" and self.vernam_checkbox.get()=="00" and self.monoalphabetic_checkbox.get()=="000"):
            self.result.insert(index="0.0",text="nohting. Please select a method for Encryption/Decryption. ")
        return
        
      
if __name__ == "__main__":
	app = App()
	app.mainloop()