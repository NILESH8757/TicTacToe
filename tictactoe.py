# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:10:07 2018

@author: nilesh8757
"""

#basic tic-tac-toe game

from IPython.display import clear_output
board=[' ']*10
P1=' '
P2=' '

def printBoard():
    clear_output()
    global board
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])
 
def checkResult():
    global P1
    global P2 
    global board 
    p1=False
    p2=False
    temp=False
    for item in board[1:]:
        if item == ' ':
            temp=True
            break
    
        
    if board[1] == P1 and board[2] == P1 and board[3] == P1:
        p1=True
    elif board[4] == P1 and board[5] == P1 and board[6] == P1:
        p1=True
    elif board[7] == P1 and board[8] == P1 and board[9] == P1:
        p1=True
    elif board[1] == P1 and board[4] == P1 and board[7] == P1:
        p1=True
    elif board[2] == P1 and board[5] == P1 and board[8] == P1:
        p1=True
    elif board[3] == P1 and board[6] == P1 and board[9] == P1:
        p1=True
    elif board[1] == P1 and board[5] == P1 and board[9] == P1:
        p1=True 
    elif board[3] == P1 and board[5] == P1 and board[7] == P1:
        p1=True 
    elif board[1] == P2 and board[2] == P2 and board[3] == P2:
        p2=True
    elif board[4] == P2 and board[5] == P2 and board[6] == P2:
        p2=True
    elif board[7] == P2 and board[8] == P2 and board[9] == P2:
        p2=True
    elif board[1] == P2 and board[4] == P2 and board[7] == P2:
        p2=True
    elif board[2] == P2 and board[5] == P2 and board[8] == P2:
        p2=True
    elif board[3] == P2 and board[6] == P2 and board[9] == P2:
        p2=True
    elif board[1] == P2 and board[5] == P2 and board[9] == P2:
        p2=True 
    elif board[3] == P2 and board[5] == P2 and board[7] == P2:
        p2=True 
    else:
        p2=False

    
    
    if p1 == True :
        print("Whoah! Player 1 won!!")
        return 1
    elif p2 == True :
        print("Whoah! Player 2 won!!")
        return 2
    elif temp == True:
        print("continue...")
        return 0
    else:
        print("Match Draw :(")
        return 3
        
def startGame():
    clear_output()
    global P1
    global P2
    print("Game begins,Board positions are as follows:")
    bl=['0','1','2','3','4','5','6','7','8','9']
    print(bl[7]+'|'+bl[8]+'|'+bl[9])
    print('-----')
    print(bl[4]+'|'+bl[5]+'|'+bl[6])
    print('-----')
    print(bl[1]+'|'+bl[2]+'|'+bl[3])

    P1=input("Player 1 , Enter your marker: ")
    if P1=='X':
        P2='O'
    else:
        P2='X'
    
def user_input():
    cnt=1
    global P1
    global P2 
    global board 
    
    while cnt<=9:
        if cnt & 1:
            pos=int(input("Player 1, Enter your position: "))
            board[pos]=P1
            printBoard()
            res=checkResult()
        else:
            pos=int(input("Player 2, Enter your position: "))
            board[pos]=P2
            printBoard()
            res=checkResult()
        cnt+=1
        if(res>0):
            break
    
    
    #checkResult()    

def main():
    while True:
        startGame()
        user_input()
        choice=input("Do you want to play again? (y/n): ")
        if choice == 'n':
            break

if __name__ == "__main__":
    main()    
            
            
        
        
