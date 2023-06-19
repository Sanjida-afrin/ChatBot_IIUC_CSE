from tkinter import*
from tkinter import ttk
from textblob import TextBlob 
from PIL import Image,ImageTk
import pandas as pd
import numpy as np
import textdistance
import re


class ChatBot:
     def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)
        
        main_frame=Frame(self.root,bd=4,bg='black',width=610)
        main_frame.pack()
        
        Title_label=Label(main_frame,bd=30,relief=RAISED,anchor='center',width=730,compound=LEFT,text='CHAT ME',font=('arial',30,'bold'),fg='white',bg='black')
        Title_label.pack(side=TOP)    
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=1500,height=22,bd=3,relief=RAISED,font=('arial',14),bg='black',fg='white',yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()    
        
        btn_frame=Frame(self.root,bd=4,bg='black',width=720)
        btn_frame.pack()
        
        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='black',bg='gray')
        label_1.grid(row=0,column=0,padx=5,sticky=W)
        
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=95,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        
        self.send=Button(btn_frame,text="Send",command=self.send,font=('arial',15,'bold'),width=8,bg='grey',fg='white')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='grey',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        
        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='black')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)
     
     def enter_func(self,event):
         self.send.invoke()
         self.entry.set('')
       
     def clear(self):
         self.text.delete('1.0',END)
         self.entry.set('')
         
     
        
     def send(self):
         send=" "+'You: '+self.entry.get()
         self.text.insert(END,'\n'+send)
         self.text.yview(END)
    
         
         if (self.entry.get()==''):
             self.msg='Please enter some input'
             self.label_11.config(text=self.msg,fg='red')
         
         else:
             self.msg=''
             self.label_11.config(text=self.msg,fg='red')
             
         p = self.entry.get()
         
         if 'Hi' in p or 'hi' in p:
             self.text.insert(END,'\n'+" "+'Bot: Hi!How can I help you?'+'\n')
         elif 'Hello' in p or 'hello' in p:
             self.text.insert(END,'\n'+" "+'Bot: Hello!How can I help you?'+'\n')
         elif 'assist' in p or 'Can you assist me?' in p:
             self.text.insert(END,'\n'+'Bot: Yeah Sure' +'\n') 
         elif 'What is CSE?' in p or 'what is cse?' in p:
             self.text.insert(END,'\n'+'Bot: Computational Science and Engineering (CSE) is a discipline devoted to the study and advancement of computational methods and data analysis techniques to analyze and understand natural and engineered systems.' +'\n')     
         elif 'full' in p or 'form' in p or 'Full' in p or 'Form' in p  or 'FULL' in p or 'FORM' in p:
             self.text.insert(END,'\n'+'Bot: International Islamic University Chittagong' +'\n')
         elif 'located' in p or 'location' in p or 'Located' in p or 'Location' in p or 'LOCATED' in p or 'LOCATION' in p:
             self.text.insert(END,'\n'+'Bot: Kumira(Sitakunda),Chittagong.' +'\n')
         elif 'Area' in p or 'area' in p or 'AREA' in p:
             self.text.insert(END,'\n'+'Bot: IIUC has developed its 40 acres Permanent Campus at Kumira (Sitakunda) – 22 km off Chittagong City and situated beside the Dhaka-Chittagong highway in a hilly area with required modern facilities and in a beautiful landscape with thin forest bounties.' +'\n')
         elif 'Rank' in p or 'rank' in p or 'RANK' in p or 'ranking' in p or 'RANKING' in p:
             self.text.insert(END,'\n'+'Bot: International Islamic University, Chittagong ranked 34th in Bangladesh, 6201st in the global 2023 rating, and scored in 12 research topics.' +'\n')
         elif 'UGC' in p or 'ugc' in p or 'Ugc' in p:
             self.text.insert(END,'\n'+'Bot: This program is a University Grant Commission Bangladesh(UGC) approved program. Besides, this program has been accredited by the Board of Accreditation for Engineering and Technical Education (BAETE). IIUC has been made an application to BAETE for a renewal on 31.12.' +'\n')
         elif 'Public' in p or 'public' in p or 'PUBLIC' in p:
             self.text.insert(END,'\n'+'Bot: International Islamic University Chittagong (IIUC) is one of the top graded Government approved private universities in Bangladesh.' +'\n')
         elif 'Established?' in p or 'established' in p or 'build' in p or 'Build' in p:
             self.text.insert(END,'\n'+'Bot: February 11,1995' +'\n')
         elif 'Transport' in p or 'transport' in p or 'TRANSPORT' in p :
             self.text.insert(END,'\n'+'Bot: By Bus' +'\n')
        #  elif 'Teachers' in p or 'teachers' in p:
        #      self.text.insert(END,'\n'+'Bot: Around 400' +'\n')
         elif 'Teachers' in p or 'teachers' in p or 'TEACHERS' in p:
            if  'CSE' in p or 'Cse' in p or 'cse' in p:
               self.text.insert(END,'\n'+'Bot: 70' +'\n')
            elif 'Male' in p or 'male' in p or 'MALE' in p:
               self.text.insert(END,'\n'+'Bot: Around 250' +'\n')
            elif 'Female' in p or 'female' in p or 'FEMALE' in p:
               self.text.insert(END,'\n'+'Bot: Around 150' +'\n')
            else:
               self.text.insert(END,'\n'+'Bot: Around 150' +'\n')
         elif 'Female Academic Zone' in p or 'female academic zone' in p or 'FAZ' in p or 'faz' in p or 'female campus' in p or 'Female Campus' in p or 'FEMALE CAMPUS' in p:
             self.text.insert(END,'\n'+'Bot: From the rail line, you will go right and the south campus is the Female Academic Zone.' +'\n')
         elif 'Male Academic Zone' in p or 'male academic zone' in p or 'male campus' in p or 'Male Campus' in p or 'MALE CAMPUS' in p:
             self.text.insert(END,'\n'+'Bot: From the rail line, you will go left and the North campus is the  Male Academic Zone.' +'\n')
         elif 'Cafeteria' in p or 'cafeteria' in p or 'CAFETERIA' in p :
             self.text.insert(END,'\n'+'Bot: Both campus have their own Cafeteria.For Male campus- If you find Male Academic Zone, then go straight some yards which will bring you the Central Cafeteria.For Female campus- If you find Female Academic Zone, then go straight some yards which will bring you the Central Cafeteria.' +'\n')
         elif 'Central Mosque' in p or 'central mosque' in p or 'CENTRAL MOSQUE' in p:
             self.text.insert(END,'\n'+'Bot: After entering Male Academic Zone, go straight and you will find Central Mosque.' +'\n')
         elif 'Library?' in p or 'library' in p or 'LIBRARY' in p:
             self.text.insert(END,'\n'+'Bot: After entering Male Academic Zone, go straight and you will find Central Library.' +'\n')
         elif 'Nursery' in p or 'nursery' in p:
              self.text.insert(END,'\n'+'Bot: Yes and behind the Central Mosque you will find it.' +'\n')
         elif 'Department' in p or 'department' in p or 'DEPARTMENT' in p:
             if 'male' in p or 'MALE' in p or 'Male' in p:
               if 'law' in p or 'LAW' in p or 'Law' in p:
                self.text.insert(END,'\n'+'Bot: In right side of Central Library you will see Dept. Of Law facing towards you when entering the campus through the gate.' +'\n')
               elif 'Sharia' in p or 'sharia' in p or 'SHARIA' in p:
                self.text.insert(END,'\n'+'Bot: In right side of Central Library you will see Dept. of Sharia are facing towards you when entering the campus through the gate.' +'\n')
               elif 'Pharmacy' in p or 'pharmacy' in p or 'PHARMACY' in p:
                self.text.insert(END,'\n'+'Bot: To go to Dept. of Pharmacy you have to go past Central Cafeteria. '+'\n')
               elif 'BBA' in p or 'bba' in p or 'Bba' in p:
                self.text.insert(END,'\n'+'Bot: Dept. of BBA is exactly behind the Dept. of Pharmacy.' +'\n')
               elif 'ELL' in p or 'ell' in p or 'Ell' in p:
                self.text.insert(END,'\n'+'Bot: Dept. of ELL is situated besides the Dept. of BBA, just a tiny building ' +'\n')
               elif 'CSE' in p or 'cse' in p or 'Cse' in p:
                self.text.insert(END,'\n'+'Bot: Dept. of CSE is situated besides the Dept. of BBA.' +'\n')
               else:
                self.text.insert(END,'\n'+'Bot:sorry cant find ' +'\n')
             else :
               if 'Pharmacy' in p or 'pharmacy' in p or 'PHARMACY' in p:
                self.text.insert(END,'\n'+'Bot: It is situated in the same building as CSE Dept.' +'\n')
               elif 'BBA' in p or 'bba' in p or 'Bba' in p:
                self.text.insert(END,'\n'+'Bot: After entering Female Academic Zone, go straight and you will find Dept. of BBA,the 1st building..' +'\n')
               elif 'ELL' in p or 'ell' in p or 'Ell' in p:
                self.text.insert(END,'\n'+'Bot: Dept. of ELL is situated besides the Dept. of CSE, the last old building.' +'\n')
               elif 'CSE' in p or 'cse' in p or 'Cse' in p:
                self.text.insert(END,'\n'+'Bot: Dept. of CSE is situated besides the Dept. of BBA.' +'\n')
               else:
                self.text.insert(END,'\n'+'Bot: sorry cant find ' +'\n')
         elif 'where' in p or 'WHERE' in p or 'Where' in p:
            if 'ACAD' in p or 'acad' in p or 'Acad' in p:
             self.text.insert(END,'\n'+'Bot: For Male campus: ACAD is located on the west of Central Cafeteria,beside the central field .For Female campus : ACAD is located at the BBA building ground floor.' +'\n')
            elif 'Auditorium' in p or 'AUDITORIUM' in p or 'auditorium' in p:
             self.text.insert(END,'\n'+'Bot: Auditorium is located on the east side of Central Cafeteria. ' +'\n')
            elif 'payment' in p or 'Payment' in p or 'PAYMENT' in p or 'Pay' in p or 'pay' in p or 'PAY' in p:
             self.text.insert(END,'\n'+'Bot: In male and female campus also in FSIB and EXIM bank.' +'\n')
            else:
             self.text.insert(END,'\n'+'Bot: sorry cant find ' +'\n')  
         elif 'CR' in p or 'cr' in p :
             if '1Af' in p or '1af' in p or '1AF' in p:
                 self.text.insert(END,'\n'+'Bot: Umme Sadia Meem, C231437,01858214680, Umme12sadia@gmail.com.' +'\n')
             elif '1Bf' in p or '1bf' in p or '1BF' in p:
                 self.text.insert(END,'\n'+'Bot: Fahmida Parvin Romana, C231463,01867309485, Fahmidaromana67@gmail.com.' +'\n')
             elif '1Cf' in p or '1cf' in p or '1CF' in p:
                 self.text.insert(END,'\n'+'Bot: Umme sumaiya Jerin, C231493, 01835188065 .' +'\n')
             elif '1Df' in p or '1df' in p or '1DF' in p:
                 self.text.insert(END,'\n'+'Bot: Tasnim Nahar Raisa,C231526,01401028063, Tasnimraisa24@gmail.com.' +'\n')
             elif '2Af' in p or '2af' in p or '2AF' in p:
                 self.text.insert(END,'\n'+'Bot: Syeda Afra Anam, C223205, 01755573659, afraanamsyeda@gmail.com.' +'\n')
             elif '2Bf' in p or '2bf' in p or '2BF' in p:
                 self.text.insert(END,'\n'+'Bot: Afia Ebnath Boshra, C223236, 01885094963, afiaebnathboshra@gmail.com.' +'\n')
             elif '2Cf' in p or '2cf' in p or '2CF' in p:
                 self.text.insert(END,'\n'+'Bot: Sharmin Akter, C223300, 01860857779 Sharminsaba99@gmail.com.' +'\n')
             elif '3Af' in p or '3af' in p or '3AF' in p:
                 self.text.insert(END,'\n'+'Bot: Jannatul Adon Joha, C213235, 01880038294, C221235@ugrad.iiuc.ac.bd.' +'\n')
             elif '3Bf' in p or '3bf' in p or '3BF' in p:
                 self.text.insert(END,'\n'+'Bot: Ruiya Amin, C221267, 01618455355, 01751106363 c221267@ugrad.iiuc.ac.bd.' +'\n')
             elif '3Cf' in p or '3cf' in p or '3CF' in p:
                 self.text.insert(END,'\n'+'Bot: Uma Dhar, C221297,01838875117/01970618761, c221297@ugrad.iiuc.ac.bd.' +'\n')
             elif '4Af' in p or '4af' in p or '4AF' in p:
                 self.text.insert(END,'\n'+'Bot: Umma Mahararunnasa Mim, C213224, 01869444030 meherunnasamim88@gmail.com.' +'\n')
             elif '4Bf' in p or '4bf' in p or '4BF' in p:
                 self.text.insert(END,'\n'+'Bot: Maimuna Akter Shawon, C213236, 01634872773 c213236@ugrad.iiuc.ac.bd.' +'\n')
             elif '5Af' in p or '5af' in p or '5AF' in p:
                 self.text.insert(END,'\n'+'Bot: FARIHA ZANNAT, C211202, 01317664535 zannatfariha186@gmail.com.' +'\n')
             elif '5Bf' in p or '5bf' in p or '5BF' in p:
                 self.text.insert(END,'\n'+'Bot: Syed Fatema Suchi, C211257, 01971906476 syedfatemasuchi@gmail.com.' +'\n')
             elif '6Af' in p or '6af' in p or '6AF' in p:
                 self.text.insert(END,'\n'+'Bot: Jesmin Akter Nipa, C201231, 01725333423 c201231@ugrad.iiuc.ac.bd.' +'\n')
             elif '6Bf' in p or '6bf' in p or '6BF' in p:
                 self.text.insert(END,'\n'+'Bot: Lamisa Mashiat, C201249, 01308798682 lamisamashiat3@gmail.com.' +'\n')
             elif '7Af' in p or '7af' in p or '7AF' in p:
                 self.text.insert(END,'\n'+'Bot: Fahmida Rahman, C193204, 01754054262 fahmida.rahman103@gmail.com.' +'\n')
             elif '7Bf' in p or '7bf' in p or '7BF' in p:
                 self.text.insert(END,'\n'+'Bot: Sungeda Akter Rumi, C193251, 01628267811 c193251@ugrad.iiuc.ac.bd.' +'\n')
             elif '8Af' in p or '8af' in p or '8AF' in p:
                 self.text.insert(END,'\n'+'Bot: Sumaiya Tabassum, C191207, 01893028767, c191207@ugrad.iiuc.ac.bd.' +'\n')
             else :
                 self.text.insert(END,'\n'+'Bot: Syeda SomiaTasnim, C191267, 01866210026 C191267@ugrad.iiuc.ac.bd.' +'\n')
         
         elif 'Advisor' in p or 'advisor' in p :
             if '1Af' in p or '1af' in p or '1AF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Subrina Akter,Assistant Professor,01817751583,Spring 2023.' +'\n')
             elif '1Bf' in p or '1bf' in p or '1BF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Subrina Akter,Assistant Professor,01817751583,Spring 2023.' +'\n')
             elif '1Cf' in p or '1cf' in p or '1CF' in p:
                 self.text.insert(END,'\n'+'Bot: Mr.A.B.M.Yasir Arafat,Assistant Professor,01744656132,Spring 2023.' +'\n')
             elif '1Df' in p or '1df' in p or '1DF' in p:
                 self.text.insert(END,'\n'+'Bot: Mr.Md.Khaliluzzaman,Assistant Professor,01711199212,Spring 2023.' +'\n')
             elif '2Af' in p or '2af' in p or '2AF' in p:
                 self.text.insert(END,'\n'+'Bot: Dr.Mohammad Aman Ullah,Assosciate Professor,01815641524,Autumn 2022.' +'\n')
             elif '2Bf' in p or '2bf' in p or '2BF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Zinnia Sultana,Assosciate Professor,01716432134,Autumn 2022.' +'\n')
             elif '2Cf' in p or '2cf' in p or '2CF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Shefayatuj jobaru Chowdhury,Assistant Lecturer,01984696037,Autumn 2022.' +'\n')
             elif '3Af' in p or '3af' in p or '3AF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Farzana Tasnim,Lecturer,01521487508,Spring 2022.' +'\n')
             elif '3Bf' in p or '3bf' in p or '3BF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Farzana Tasnim,Lecturer,01521487508,Spring 2022.' +'\n')
             elif '3Cf' in p or '3cf' in p or '3CF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Sanjida Sharmin,Lecturer,01798129266,Spring 2022.' +'\n')
             elif '4Af' in p or '4af' in p or '4AF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Israt Binteh Habib,Lecturer,01937294500,Autumn 2021.' +'\n')
             elif '4Bf' in p or '4bf' in p or '4BF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Israt Binteh Habib,Lecturer,01937294500,Autumn 2021.' +'\n')
             elif '5Af' in p or '5af' in p or '5AF' in p:
                 self.text.insert(END,'\n'+'Bot: Md.Ziaur Rahman,Lecturer,01811812113,Spring 2021.' +'\n')
             elif '5Bf' in p or '5bf' in p or '5BF' in p:
                 self.text.insert(END,'\n'+'Bot: Md.Ziaur Rahman,Lecturer,01811812113,Spring 2021.' +'\n')
             elif '6Af' in p or '6af' in p or '6AF' in p:
                 self.text.insert(END,'\n'+'Bot: Dr.Muhammad Moazzam Hossen,Assosciate Professor,01671424548,Spring 2020.' +'\n')
             elif '6Bf' in p or '6bf' in p or '6BF' in p:
                 self.text.insert(END,'\n'+'Bot: Dr.Muhammad Moazzam Hossen,Assosciate Professor,01671424548,Spring 2020.' +'\n')
             elif '7Af' in p or '7af' in p or '7AF' in p:
                 self.text.insert(END,'\n'+'Bot: Mr.Saiful Islam,Lecturer,01818650864,Autumn 2019.' +'\n')
             elif '7Bf' in p or '7bf' in p or '7BF' in p:
                 self.text.insert(END,'\n'+'Bot: Mrs.Sanjida Sharmin,Lecturer,01798129266,Autumn 2019.' +'\n')
             elif '8Af' in p or '8af' in p or '8AF' in p:
                 self.text.insert(END,'\n'+'Bot: Mr.A.B.M.Yasir Arafat,Assistant Professor,01744656132,Spring 2019.' +'\n')
             else :
                 self.text.insert(END,'\n'+'Bot: Mrs.Sayma Haque,Assistant Professor,01712245515,Spring 2019.' +'\n')
         elif 'teacher' in p or 'Teacher' in p or 'list' in p or 'List' in p:
                 self.text.insert(END,'\n'+'Bot:  1. Prof. Dr. Engr. Abdul Kadar M. Masum,Chairman & Professor,01611411784, 01842411784,akmmasum@yahoo.com' + '\n'+'         2. Prof. Dr.  Md. Monirul Islam, Professor,01711701719,monirliton@yahoo.com' +'\n' +'         3. Prof. Mohammed Shamsul Alam, Professor,01711941680,alam_cse@yahoo.com' + '\n' +'          4. Prof. Dr. A. N. M. Rezaul Karim, Professor,01819941685,zakianaser@yahoo.com' +'\n' +'          5. Mr. Mohammad Mahadi Hassan, Associate Professor,01957719040,mahadi_cse@yahoo.com' +'\n' +'          6. Mr. Tanveer Ahsan, Associate Professor,01789523129,tanveerahsan@gmail.com' +'\n' +'          7. Dr. Shahidul Islam Khan, Associate Professor,01837184801,nayeemkh@gmail.com' +'\n' +'          8. Engr. Mohammad Aman Ullah, PhDAssociate professor,01815641524,ullah047@yahoo.com' +'\n' +'          9. Dr. Touhidul Alam,Associate Professor,01836797988,touhid13@gmail.com,touhid13@iiuc.ac.bd' +'\n' +'          10. Dr. Muhammad Moazzam Hossen, Associate Professor,01671424548,Moazzam.physics@gmail.com' +'\n' +'           11.	Dr. Muhammed Jamshed Alam Patwary, Associate Professor,01812654206,jamshed_cse_cu@yahoo.com,,mjap@iiuc.ac.bd' +'\n' +'          12. Mr. Md. Mahmudur Rahman, Associate Professor,01712056492,provaiiuc@gmail.com' +'\n' +'          13. Mr. Mohammad Manjur Alam, Associate Professor,01813176838,manjuralam44@yahoo.com' +'\n' +'          14.	Mr. Md. Mahiuddin, Associate Professor,01818734150,01960279300,mmuict@gmail.com' +'\n' +'          15. Mrs. Zinia Sultana, Associate Professor,01716432134,zinniaiiuc@yahoo.com' +'\n' +'          16. Mr. Mohammed Safiullah,Assistant Professor,01711304565,safiullah@gmail.com' +'\n' +'          17. Mr. Abdullahil Kafi,Assistant Professor,01720155585,ab_kafi@yahoo.com' +'\n' +'          18. Dr. Siddique Ahmed, Ph.D.Assistant Professor,01711572520,drsiddiqueahmed@gmail.com' +'\n' +'          19.	Mrs. Sayema Hoque,Assistant Professor,01712245515,sayemaiiuc@yahoo.com' +'\n' +'          20. Mr. Faisal Bin Al Abid, Assistant Professor,01306917266,faisaliut42@gmail.com' +'\n' +'          21. Mrs. Subrina Akter, Assistant Professor,01817751583,subrina_30@yahoo.com' +'\n' +'          22. Mr. Md. Khaliluzzaman, Assistant Professor,01711199212,khalil_021@yahoo.co.in,khalilcse021@gmail.com' +'\n' +'          23. Mr. Md. Rashedul Islam, Assistant Professor,01717121186,01914465684,rashed_maths@yahoo.com' +'\n' +'          24. Mr.A.B.M.Yasir Arafat,Assistant Professor,01744656132,abmya89@yahoo.com' +'\n' +'          25.	Mr. Md. Khorshed Ali,Assistant Professor,01711047038,khorshed.chem.cse@iiuc.ac.bd' +'\n' +'          26. Mohammad Sazid Zaman Khan,Assistant Professor,01770346336,szkhanctg@gmail.com' +'\n' +'          27. Mohammad Zainal Abedin,Assistant Professor,01720624156,jakcse99@gmail.com' +'\n' +'          28. Mrs. Sanjida Sharmin,Lecturer,01798129266,ssharmin114@gmail.com' +'\n' +'          29. Mr. Md. Ziaur Rahman,Lecturer,01811812113,ziaur.rahman@iiuc.ac.bd,' +'\n' +'          30.	Mrs. Israt Binteh Habib,Lecturer,01937294500,01858943393,israthabib.cse@gmail.com' +'\n' +'          31. Mr. Saiful Islam,Lecturer,01818650864,engsaiful0@gmail.com' +'\n' +'          32. Mr. Jamil-as-ad,Lecturer,01626890190,Jamilasad1@gmail.com' +'\n' +'          33.	Mr.Muhammed Nazmul Arefin,Lecturer,01797198813,Nazmul.arefin.85@gmail.com' +'\n' +'          34. Mrs.Farzana Tasnim,Lecturer,01521487508,farzanatasnim34@gmail.com' +'\n' +'          35. Mr.Md.Ariful Islam,Lecturer,01882190422,arif291006@gmail.com' +'\n' +'          36. Mrs.Nuren Nafisa,Assistant Lecturer,01624978991,nurennafisa@gmail.com' +'\n' +'          37. Mr.Md.Safayat Hossen,Assistant Lecturer,01736161688,safayathossen@iut-dhaka.edu' +'\n' +'          38. Mr.Nayeem Mahmood,Assistant Lecturer,01673793558,alive.dew@gmail.com' +'\n' +'          39. Mr.Md.Saiful Islam,Assistant Lecturer,01873525101,Saiful.iiuc36@yahoo.com' +'\n' +'          40. Ms. Shefayatuj Johara Chowdhury,Assistant Lecturer,01984696037,Shefaya61@gmail.com' +'\n' +'          41. Mr.Sahriar Reza,Assistant Lecturer,01521328094,sahariarp@gmail.com' +'\n' +'          42. Mr. Md.Taiseer Alam,Assistant Lecturer,01834884398,taiseeralam990@gmail.com' +'\n' +'          43. Ms.Sabrina Jahan Maisha,Assistant Lecturer,01712110411,Sjbm1996@gmail.com' +'\n')
         elif 'Routine' in p or 'routine' in p or 'ROUTINE' in p or 'schedule' in p or 'Schedule' in p:
             if '6bf' in p or '6BF' in p or '6Bf' in p:
                 self.text.insert(END,'\n'+'Bot: Time | 8.20am-9.20am  | 9.10am-10.00am	           | 10.00am-10.50am	| 10.50am-11.40am	| 11.40am-12.30pm	| 12.30pm-1.20pm '+'\n' + '        Sat    |   CSE-3635(SA) |                                          |                   CSE-3632(SJC)                    |           CSE-3636(SA)                        |' +'\n' + '        Sun   |                             |URED-3604((MJI CGED)|                                 |                 ECON-3501(SH)                      |            ' +'\n' + '        Mon  | CSE-3525(MMU)|                        CSE-3638+CSE-3640(ABA ADJ)                             |       CSE-3637(ABA ADJ)                   |' + '\n' + '        Tues |CSE-3637(ABA)|                CSE-3631(SJC)                                  |                                                                          | MDP-3606(IBH) |' +'\n' + '        Wed |CSE-3631(SJC)|URED-3604(MJI CGED)   |               CSE-3525(MMU)                      |                         CSE-3635(SA)             |' +   '\n')                        
             else:
                 self.text.insert(END,'\n'+'Bot: Time | 8.20am-9.20am  | 9.10am-10.00am	           | 10.00am-10.50am	| 10.50am-11.40am	| 11.40am-12.30pm	| 12.30pm-1.20pm '+'\n' + '        Sat    |                          CSE-3637(ABA)       |                        CSE-3635(SA)                             |                                                ' +'\n' + '        Sun   |           ECON-3501(SH)                |URED-3604((MJI CGED) |                   CSE-3631(SJC)                             |        MDP-3606(IBH)               ' +'\n' + '        Mon  |              CSE-3525(MMU)            |CSE-3631(SJC)    |                 CSE-3636(SA)                                                   ' + '\n' + '        Tues |              CSE-3525(MMU)          |                                                                        CSE-3638+CSE3640(ABA)                     |                ' +'\n' + '        Wed |         CSE-3632(SJC)              |URED-3604(MJI CGED)|        CSE-3637(ABA)         |                                                   ' +   '\n')
         elif 'Fee' in p or 'fee' in p or 'FEE' in p or 'Fees' in p or 'fees' in p or 'FEES' in p or 'Cost' in p or 'cost' in p or 'COST' in p:
             if 'semester' in p or 'Semester' in p:
                 self.text.insert(END,'\n'+'Bot: Around 60 thousand.' +'\n')
             elif 'payment' in p or 'Payment' in p or 'PAYMENT' in p or 'Pay' in p or 'pay' in p or 'PAY' in p:
                 self.text.insert(END,'\n'+'Bot: In male and female campus also in FSIB and EXIM bank.' +'\n')
             else:
                 self.text.insert(END,'\n'+'Bot: Around 5 lakh.' +'\n')
        
         else:
             self.text.insert(END,'\n'+"Bot: Sorry I didn't get it" +'\n')
             


     

        
if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
        