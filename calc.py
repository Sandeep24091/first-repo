from my_code import clr_scrn
clr_scrn()

def title() :
      print('''
 ====================================================

                  PY CALCULATOR
 ====================================================
      ''')


title()
txt ='abcdefghijklmnopqrstuvwxyz'
result = 0
lbl = ''
opt = ''
m_items = 'm :'
while True :
      if opt.upper()=='E':
            clr_scrn()
            break
      elif opt.upper()== 'R':
                 result = 0
                 lbl = ''
                 opt = ''
      clr_scrn()
      title()
      print (m_items)
      print('----------------------------------')
      print(result)
      print('----------------------------------')
      print (lbl + opt)
      print('----------------------------------')
      ui = input('enter number >' )
      for i in txt :
          if i in ui or i.upper() in ui :
                input('please enter only numbers !!!.\nPress enter to continue')
                break
      else:
           ui = int(ui)
           if opt == '+':
            result += ui
            lbl += '+' + str(ui) 
           elif opt == '-' :
            result -= ui 
            lbl += '-' + str(ui) 
           elif opt == '*' :
            result *= ui 
            lbl += 'x' + str(ui) 
           elif opt == '/' :
            result /= ui 
            lbl += '/' + str(ui)
           
           else :
                 result = ui
                 lbl =str(ui) 
      
      clr_scrn()
      title()
      print(f'm:{len(m_items)}')
      print('----------------------------------')
      print(result)
      print('----------------------------------')
      print (lbl )
      print('----------------------------------')
      opt =input('''
*************************************
menu
*************************************
      "E" - Exit
      "R" - reset
      "m" - memory
      select operator (+,-,X,/) >
      ''')




