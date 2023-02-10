from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from random import*
import os
import sys
os.system("cls")
class Col(QMainWindow):
    def __init__(self):
       super().__init__()
       self.setWindowTitle("LOTTO SHOW")
       self.resize(1668,1260)
       self.move(50,10)
       self.setMaximumSize(1668,1260)
       self.setStyleSheet("""
       background-color: rgb(128,128,128);
       border-width: 1px;
       border-radius: 29px;
       border-style: solid;""")
       self.dastur()
       self.show()
    def dastur(self):
       self.sch=0
       self.setFont(QFont("Calibri",20))
       self.lb1=QRadioButton("Omad (36/5)",self)
       self.lb1.setGeometry(100,10,200,50)
       self.lb2=QRadioButton("Sharqona (36/6)",self)
       self.lb2.setGeometry(300,10,200,50)
       self.lb3=QRadioButton("Super (36/7)",self)
       self.lb3.setGeometry(500,10,200,50)
       self.ly=QHBoxLayout(self)
       self.ly.addWidget(self.lb1)
       self.ly.addWidget(self.lb2)
       self.ly.addWidget(self.lb3)
       self.setLayout(self.ly)

       self.lb1.clicked.connect(self.das)
       self.lb2.clicked.connect(self.das)
       self.lb3.clicked.connect(self.das)
       

       self.ek = QLineEdit(self)
       self.ek.setGeometry(50,80,600,80)
       self.ek.setStyleSheet("""
       background-color: rgb(255,255,255);
       border-color: rgb(255,255,255);
       border-width: 1px;
       border-radius: 25px;
       border-style: outset;""")
       self.ek.setAlignment(Qt.AlignRight)
       self.ek.setFont(QFont('Arial', 30))
       
       
                                          
       self.la = QPushButton("+",self)
       self.la.setGeometry(650,80,100,80)
       self.la.setStyleSheet("""
       background-color: rgb(255,165,0);
       border-color: rgb(255,165,0);
       border-width: 1px;
       border-radius: 29px;
       border-style: outset;""")
       self.la.setFont(QFont('Arial', 40))
       self.la.clicked.connect(self.ekran)
       


       self.s1=QPushButton("1",self)
       self.s1.setGeometry(100,180,80,70)
       self.s1.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s1.setFont(QFont("clibri",20))
       
       self.s2=QPushButton("2",self)
       self.s2.setGeometry(200,180,80,70)
       self.s2.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s2.setFont(QFont("clibri",20))
      

       self.s3=QPushButton("3",self)
       self.s3.setGeometry(300,180,80,70)
       self.s3.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s3.setFont(QFont("clibri",20))
      
       self.s4=QPushButton("4",self)
       self.s4.setGeometry(400,180,80,70)
       self.s4.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s4.setFont(QFont("clibri",20))
      
       self.s5=QPushButton("5",self)
       self.s5.setGeometry(500,180,80,70)
       self.s5.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s5.setFont(QFont("clibri",20))
      
       self.s6=QPushButton("6",self)
       self.s6.setGeometry(600,180,80,70)
       self.s6.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s6.setFont(QFont("clibri",20))
       
       self.s7=QPushButton("7",self)
       self.s7.setGeometry(100,280,80,70)
       self.s7.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s7.setFont(QFont("clibri",20))
       
       self.s8=QPushButton("8",self)
       self.s8.setGeometry(200,280,80,70)
       self.s8.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s8.setFont(QFont("clibri",20))
     
       self.s9=QPushButton("9",self)
       self.s9.setGeometry(300,280,80,70)
       self.s9.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s9.setFont(QFont("clibri",20))
     
       self.s0=QPushButton("10",self)
       self.s0.setGeometry(400,280,80,70)
       self.s0.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s0.setFont(QFont("clibri",20))
     
       self.s11=QPushButton("11",self)
       self.s11.setGeometry(500,280,80,70)
       self.s11.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s11.setFont(QFont("clibri",20))
    
       self.s12=QPushButton("12",self)
       self.s12.setGeometry(600,280,80,70)
       self.s12.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s12.setFont(QFont("clibri",20))
     
       self.s13=QPushButton("13",self)
       self.s13.setGeometry(100,380,80,70)
       self.s13.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s13.setFont(QFont("clibri",20))
       
       self.s14=QPushButton("14",self)
       self.s14.setGeometry(200,380,80,70)
       self.s14.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s14.setFont(QFont("clibri",20))
      
       self.s15=QPushButton("15",self)
       self.s15.setGeometry(300,380,80,70)
       self.s15.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s15.setFont(QFont("clibri",20))
      
       self.s16=QPushButton("16",self)
       self.s16.setGeometry(400,380,80,70)
       self.s16.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s16.setFont(QFont("clibri",20))
       
       self.s17=QPushButton("17",self)
       self.s17.setGeometry(500,380,80,70)
       self.s17.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s17.setFont(QFont("clibri",20))
     
       self.s18=QPushButton("18",self)
       self.s18.setGeometry(600,380,80,70)
       self.s18.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s18.setFont(QFont("clibri",20))
     

       self.s19=QPushButton("19",self)
       self.s19.setGeometry(100,480,80,70)
       self.s19.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s19.setFont(QFont("clibri",20))
      
       self.s20=QPushButton("20",self)
       self.s20.setGeometry(200,480,80,70)
       self.s20.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s20.setFont(QFont("clibri",20))
      
       self.s21=QPushButton("21",self)
       self.s21.setGeometry(300,480,80,70)
       self.s21.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s21.setFont(QFont("clibri",20))
      
       self.s22=QPushButton("22",self)
       self.s22.setGeometry(400,480,80,70)
       self.s22.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s22.setFont(QFont("clibri",20))
       
       self.s23=QPushButton("23",self)
       self.s23.setGeometry(500,480,80,70)
       self.s23.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s23.setFont(QFont("clibri",20))
     
       self.s24=QPushButton("24",self)
       self.s24.setGeometry(600,480,80,70)
       self.s24.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s24.setFont(QFont("clibri",20))
      
       self.s25=QPushButton("25",self)
       self.s25.setGeometry(100,580,80,70)
       self.s25.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s25.setFont(QFont("clibri",20))
      
       self.s26=QPushButton("26",self)
       self.s26.setGeometry(200,580,80,70)
       self.s26.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s26.setFont(QFont("clibri",20))
      
       self.s27=QPushButton("27",self)
       self.s27.setGeometry(300,580,80,70)
       self.s27.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s27.setFont(QFont("clibri",20))
      
       self.s28=QPushButton("28",self)
       self.s28.setGeometry(400,580,80,70)
       self.s28.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s28.setFont(QFont("clibri",20))
    
       self.s29=QPushButton("29",self)
       self.s29.setGeometry(500,580,80,70)
       self.s29.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s29.setFont(QFont("clibri",20))
 
       self.s30=QPushButton("30",self)
       self.s30.setGeometry(600,580,80,70)
       self.s30.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s30.setFont(QFont("clibri",20))
    
       self.s31=QPushButton("31",self)
       self.s31.setGeometry(100,680,80,70)
       self.s31.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s31.setFont(QFont("clibri",20))
   
       self.s32=QPushButton("32",self)
       self.s32.setGeometry(200,680,80,70)
       self.s32.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s32.setFont(QFont("clibri",20))
    
       self.s33=QPushButton("33",self)
       self.s33.setGeometry(300,680,80,70)
       self.s33.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s33.setFont(QFont("clibri",20))
      
       self.s34=QPushButton("34",self)
       self.s34.setGeometry(400,680,80,70)
       self.s34.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s34.setFont(QFont("clibri",20))
      
       self.s35=QPushButton("35",self)
       self.s35.setGeometry(500,680,80,70)
       self.s35.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s35.setFont(QFont("clibri",20))
       
       self.s36=QPushButton("36",self)
       self.s36.setGeometry(600,680,80,70)
       self.s36.setStyleSheet("""
       background-color: rgb(170, 51, 106)""")
       self.s36.setFont(QFont("clibri",20))
     
       self.ss=QPushButton(self)
       self.ss.setGeometry(800,10,150,60)
       self.ss.setStyleSheet("""
       background-color: rgb(243, 207, 198);
       border-color: rgb(255,255,255);
       border-width: 1px;
       border-radius: 25px;
       border-style: outset;""")
       self.ss.setFont(QFont("clibri",20))
       self.ss.setText("START")
       self.ss.clicked.connect(self.chiq)

       self.e=QLineEdit(self)
       self.e.setGeometry(800,80,800,650)
       self.e.setStyleSheet("""
       background-color: rgb(255,255,255);
       border-color: rgb(255,255,255);
       border-width: 1px;
       border-radius: 20px;
       border-style: outset;""")
       self.e.setFont(QFont("clibri",40))

       self.j1=QLineEdit(self)
       self.j1.setGeometry(970,10,70,60)
       self.j1.setStyleSheet("""
       background-color: rgb(248, 152, 128)""")
       self.j1.setFont(QFont("clibri",20))
       self.j2=QLabel(self)
       self.j2.setGeometry(1060,10,70,60)
       self.j2.setStyleSheet("""
       background-color: rgb(248, 152, 128)""")
       self.j2.setFont(QFont("clibri",20))

       self.j3=QLabel(self)
       self.j3.setGeometry(1150,10,70,60)
       self.j3.setStyleSheet("""
       background-color: rgb(248, 152, 128)""")
       self.j3.setFont(QFont("clibri",20))

       self.j4=QLabel(self)
       self.j4.setGeometry(1240,10,70,60)
       self.j4.setStyleSheet("""
       background-color: rgb(248, 152, 128)""")
       self.j4.setFont(QFont("clibri",20))
       
       self.j5=QLabel(self)
       self.j5.setGeometry(1330,10,70,60)
       self.j5.setStyleSheet("""
       background-color: rgb(248, 152, 128)""")
       self.j5.setFont(QFont("clibri",20))

       self.j6=QLabel(self)
       self.j6.setGeometry(1420,10,70,60)
       self.j6.setStyleSheet("""
       background-color: rgb(248, 152, 128)""")
       self.j6.setFont(QFont("clibri",20))

       self.j7=QLabel(self)
       self.j7.setGeometry(1510,10,70,60)
       self.j7.setStyleSheet("""
       background-color: rgb(248, 152, 128)""")
       self.j7.setFont(QFont("clibri",20))
    
    def chiq(self):
       self.se=set()
       so=0
       if self.lb1.isChecked():
            so=5
       elif self.lb2.isChecked():
            so=6
       elif self.lb3.isChecked():
            so=7
       while(len(self.se)!=so):
          self.se.add(randint(1,36))
       self.se=list(self.se)
       if so==7:
          self.j1.setText(str(self.se[0]))
          self.j2.setText(str(self.se[1]))
          self.j3.setText(str(self.se[2]))
          self.j4.setText(str(self.se[3]))
          self.j5.setText(str(self.se[4]))   
          self.j6.setText(str(self.se[5]))
          self.j7.setText(str(self.se[6]))
       if so==6:
          self.j1.setText(str(self.se[0]))
          self.j2.setText(str(self.se[1]))
          self.j3.setText(str(self.se[2]))
          self.j4.setText(str(self.se[3]))
          self.j5.setText(str(self.se[4]))   
          self.j6.setText(str(self.se[5]))
       if so==5:
          self.j1.setText(str(self.se[0]))
          self.j2.setText(str(self.se[1]))
          self.j3.setText(str(self.se[2]))
          self.j4.setText(str(self.se[3]))
          self.j5.setText(str(self.se[4]))      
    def ekran(self): 
        sch=int()
        lis=[]
        self.e.setText(self.ek.text())
        x=self.ek.text().split()
        for i in self.se:
            lis.append(str(i))
        x=set(x)
        lis=set(lis)
        if len(lis.intersection(x))>3:
           self.e.setText(f"       You Win\n{len(lis.intersection(x))}")
           self.e.setStyleSheet("background-color:rgb(50,205,50)")
        else:
           self.e.setText(f"        You Lost\n{len(lis.intersection(x))}")
           self.e.setStyleSheet("background-color:rgb(215, 0, 64)")
        
    
    def das(self):
           self.s1.clicked.connect(self.action1)
           self.s2.clicked.connect(self.action2)
           self.s3.clicked.connect(self.action3)
           self.s4.clicked.connect(self.action4)
           self.s5.clicked.connect(self.action5)
           self.s6.clicked.connect(self.action6)
           self.s7.clicked.connect(self.action7)
           self.s8.clicked.connect(self.action8)
           self.s9.clicked.connect(self.action9)
           self.s0.clicked.connect(self.action0)
           self.s11.clicked.connect(self.action11)
           self.s12.clicked.connect(self.action12)
           self.s13.clicked.connect(self.action13)
           self.s14.clicked.connect(self.action14)
           self.s15.clicked.connect(self.action15)
           self.s16.clicked.connect(self.action16)
           self.s17.clicked.connect(self.action17)
           self.s18.clicked.connect(self.action18)
           self.s19.clicked.connect(self.action19)
           self.s20.clicked.connect(self.action20)
           self.s21.clicked.connect(self.action21)
           self.s22.clicked.connect(self.action22)
           self.s23.clicked.connect(self.action23)
           self.s24.clicked.connect(self.action24)
           self.s25.clicked.connect(self.action25)
           self.s26.clicked.connect(self.action25)
           self.s27.clicked.connect(self.action27)
           self.s28.clicked.connect(self.action28)
           self.s29.clicked.connect(self.action29)
           self.s30.clicked.connect(self.action30)
           self.s31.clicked.connect(self.action31)
           self.s32.clicked.connect(self.action32)
           self.s33.clicked.connect(self.action33)
           self.s34.clicked.connect(self.action34)
           self.s35.clicked.connect(self.action35)
           self.s36.clicked.connect(self.action36)  
    def action0(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('10')==0:
                   self.ek.setText(self.ek.text()+"10"+" ")
    def action1(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('1')==0:
                   self.ek.setText(self.ek.text()+"1"+" ")
    def action2(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('2')==0:
                   self.ek.setText(self.ek.text()+"2"+" ")
    def action3(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('3')==0:
                   self.ek.setText(self.ek.text()+"3"+" ")
    def action4(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('4')==0:
                   self.ek.setText(self.ek.text()+"4"+" ")
    def action5(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('5')==0:
                   self.ek.setText(self.ek.text()+"5"+" ")
    def action6(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('6')==0:
                   self.ek.setText(self.ek.text()+"6"+" ")
    def action7(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('7')==0:
                   self.ek.setText(self.ek.text()+"7"+" ")
    def action8(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('8')==0:
                    self.ek.setText(self.ek.text()+"8"+" ")
    def action9(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('9')==0:
                    self.ek.setText(self.ek.text()+"9"+" ")
    def action20(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('20')==0:
                    self.ek.setText(self.ek.text()+"20"+" ")
    def action11(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('11')==0:
                     self.ek.setText(self.ek.text()+"11"+" ")
    def action12(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('12')==0:
                    self.ek.setText(self.ek.text()+"12"+" ")
    def action13(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('13')==0:
                    self.ek.setText(self.ek.text()+"13"+" ")
    def action14(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('14')==0:
                    self.ek.setText(self.ek.text()+"14"+" ")
    def action15(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('15')==0:
                    self.ek.setText(self.ek.text()+"15"+" ")
    def action16(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('16')==0:
                    self.ek.setText(self.ek.text()+"16"+" ")
    def action17(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('17')==0:
                    self.ek.setText(self.ek.text()+"17"+" ")
    def action18(self):  
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('18')==0:
                    self.ek.setText(self.ek.text()+"18"+" ") 
    def action19(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('19')==0:
                    self.ek.setText(self.ek.text()+"19"+" ")
    
    def action30(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('30')==0:
                   self.ek.setText(self.ek.text()+"30"+" ")
    def action21(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('21')==0:
                    self.ek.setText(self.ek.text()+"21"+" ")
    def action22(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('22')==0:
                   self.ek.setText(self.ek.text()+"22"+" ")
    def action23(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('23')==0:
                    self.ek.setText(self.ek.text()+"23"+" ")
    def action24(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('24')==0:
                    self.ek.setText(self.ek.text()+"24"+" ")
    def action25(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('25')==0:
                    self.ek.setText(self.ek.text()+"25"+" ")
    def action26(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('26')==0:
                   self.ek.setText(self.ek.text()+"26"+" ")
    def action27(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('27')==0:
                    self.ek.setText(self.ek.text()+"27"+" ")
    def action28(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
                if ls.count('28')==0:
                    self.ek.setText(self.ek.text()+"28"+" ")
    def action29(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('29')==0:
                   self.ek.setText(self.ek.text()+"29"+" ")
    def action31(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('31')==0:
                   self.ek.setText(self.ek.text()+"31"+" ")
    def action32(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('32')==0:
                    self.ek.setText(self.ek.text()+"32"+" ")
    def action33(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('33')==0:
                   self.ek.setText(self.ek.text()+"33"+" ")
    def action34(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('34')==0:
                  self.ek.setText(self.ek.text()+"34"+" ")
    def action35(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('35')==0:
                   self.ek.setText(self.ek.text()+"35"+" ")
    def action36(self):
           x=self.ek.text()
           ls=x.split()
           son=0
           if self.lb1.isChecked():
            son=5
           elif self.lb2.isChecked():
            son=6
           elif self.lb3.isChecked():
            son=7
           if len(ls)<son:
               if ls.count('36')==0:
                   self.ek.setText(self.ek.text()+"36"+" ")
ap=QApplication(sys.argv)
loy=Col()
loy.show()
sys.exit(ap.exec())                                                                                                                                                                                                                                                                                                                     