import tkinter as tk
from tkinter import ttk
import time,random
from playsound3 import playsound
regions={1: "arg.x < 250 and arg.y < 250",
        2: "500 > arg.x > 250 and arg.y < 250",
        3: "750 > arg.x > 500 and arg.y < 250",
        4: "arg.x < 250 and  500 > arg.y > 250",
        5: "500 > arg.x > 250 and 500 > arg.y > 250",
        6: "750 > arg.x > 500 and 500 > arg.y > 250",
        7: "arg.x <250 and 750 > arg.y > 500",
        8: "500 > arg.x > 250 and 750 > arg.y > 500",
        9: "750 > arg.x > 500 and 750 > arg.y > 500"
        }
CrossCoords={"1A":"0,0,250,250",
            "1B":"0,250,250,0",
            "2A":"250,0,500,250",
            "2B":"250,250,500,0",
            "3A":"500,0,750,250",
            "3B":"500,250,750,0",
            "4A":"0,250,250,500",
            "4B":"0,500,250,250",
            "5A":"250,250,500,500",
            "5B":"250,500,500,250",
            "6A":"500,250,750,500",
            "6B":"500,500,750,250",
            "7A":"0,500,250,750",
            "7B":"0,750,250,500",
            "8A":"250,500,500,750",
            "8B":"250,750,500,500",
            "9A":"500,500,750,750",
            "9B":"500,750,750,500"
            }
CircleCoords={1:"0,0,250,250",
            2:"250,0,500,250",
            3:"500,0,750,250",
            4:"0,250,250,500",
            5:"250,250,500,500",
            6:"500,250,750,500",
            7:"0,500,250,750",
            8:"250,500,500,750",
            9:"500,500,750,750"
            }
winLines={ (1,2,3):"0,125,750,125",
        (1,4,7):"125,0,125,750",
        (1,5,9):"0,0,750,750",
        (2,5,8):"375,0,375,750",
        (3,5,7):"0,750,750,0",
        (3,6,9):"625,0,625,750",
        (4,5,6):"0,375,750,375",
        (7,8,9):"0,625,750,625"
        }
temp = lambda x: print("temp")
class TicTacToe:
    wins=[[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
    def __init__(self,window:tk.Tk,first_move):
        self.window=window
        self.window.geometry("750x775")
        # self.window.focus_force()
        self.first_move=first_move
        self.curr_move=first_move
        self.canvas=tk.Canvas(master=self.window,bg="black",height=750,width=750)
        self.canvas.create_line(250,0,250,750,fill="white")
        self.canvas.create_line(500,0,500,750,fill="white")
        self.canvas.create_line(0,250,750,250,fill="white")
        self.canvas.create_line(0,500,750,500,fill="white")
        self.board_state=[]
        self.player_state=[]
        self.computer_state=[]
        print(f"{self.first_move} moves first")
        self.canvas.pack()
        self.window.bind("<Button-1>",func=self.player_move)
        if self.first_move=="computer":
            window.after(1000,self.computer_move)
    @staticmethod
    def _checkerx(state,wins=wins):
        for win in wins:
            k=0
            for move in win:
                if move in state:
                    k+=1
                    if k == 3:
                        return win
                else: break 
        return False #fixed indent
    @staticmethod
    def _checker(state,wins=wins):
        for win in wins:
            if set(win).issubset(state): 
                return win
        return False
    @staticmethod
    def _checkerxx(state,wins=wins):
        return any(set(win).issubset(state) for win in wins)
    def player_move(self,arg):
        if self.curr_move == "player":
            for region in range(1,10):
                if eval(regions[region]) and region not in self.board_state:
                    # print("new")
                    self.canvas.create_line(eval(CrossCoords[f'{region}A']),fill="white",width=2)
                    self.canvas.create_line(eval(CrossCoords[f'{region}B']),fill="white",width=2)
                    self.board_state.append(region)
                    self.player_state.append(region)
                    break
            else : return
            self.curr_move="computer"
            if (win_case:=TicTacToe._checker(self.player_state)):
                self.canvas.create_line(eval(winLines[tuple(win_case)]),fill="red",width=10)
                ttk.Label(self.window,text="Player WON !!").pack()
                self.canvas.create_window((380,400),window=ttk.Label(master=self.window,text="Player Won",font=("Arial",40)))
                try:
                    playsound(r"assets\YouWin.mp3",block=False) # must be after label and all cuz it freezes untill sound over, #UPDATE no , still freezes because of tkinter waits for function to complete so playsound still activate #USE block arg
                except:
                    ""
                self.curr_move=None 
                return
            if len(self.board_state) == 9 :
                ttk.Label(self.window,text="DRAW!!").pack()
                self.canvas.create_window((380,400),window=ttk.Label(master=self.window,text="Its a Draw",font=("Arial",40)))
                self.curr_move=None 
                try:
                    playsound(r"assets\Draw.mp3",block=False)# # must be after label and all cuz it freezes untill sound over, #UPDATE no , still freezes because of tkinter waits for function to complete so playsound still activate #USE block arg
                except:
                    ""
                return
            self.window.after(1000,self.computer_move)
    def computer_move(self):
        while (random_move:=random.randint(1,9)) in self.board_state: ""
        self.canvas.create_oval(eval(CircleCoords[random_move]),outline="white")
        self.computer_state.append(random_move)
        self.board_state.append(random_move)
        if (lose_case:=TicTacToe._checker(self.computer_state)):
            self.canvas.create_line(eval(winLines[tuple(lose_case)]),fill="red",width=10)
            ttk.Label(self.window,text="COMPUTER WON !!").pack()
            self.canvas.create_window((380,400),window=ttk.Label(master=self.window,text="COMPUTER WON !!",font=("Arial",40)))
            try:
                playsound(r"assets\YouLose.mp3") # must be after label and all cuz it freezes untill sound over, #UPDATE no , still freezes because of tkinter waits for function to complete so playsound still activate #USE block arg
            except:  # here let block = true , so kinda build for the lose of player
                ""
            self.curr_move=None 
            return 
        if len(self.board_state) == 9 :
                ttk.Label(self.window,text="DRAW!!").pack()
                self.canvas.create_window((380,400),window=ttk.Label(master=self.window,text="Its a Draw",font=("Arial",40)))
                try:
                    playsound(r"assets\Draw.mp3",block=False) # must be after label and all cuz it freezes untill sound over, #UPDATE no , still freezes because of tkinter waits for function to complete so playsound still activate #USE block arg
                except:
                    ""
                self.curr_move=None 
                return
        self.curr_move="player"

class App:
    def __init__(self,window:tk.Tk):
        self.window1=window
        self.window1.geometry("200x200")
        ttk.Label(self.window1,text="Select The Computer Model").pack()
        self.computer_models=["Statistical","MinMax","Random","Q-Learning","Comparison"]
        for model in self.computer_models:
            # ttk.Button(self.window1, text=model,state= False if model!="Random" else True,command=lambda m=model: self.ttt_ui(computer=m)).pack(pady=3, fill='x', padx=20)
            ttk.Button(self.window1, text=model,state= "disabled" if model!="Random" else "normal", command=lambda m=model: self.ttt_ui(computer=m)).pack(pady=3, fill='x', padx=20)
            #disabled and normal NOT true/false
    def clear_window(self): 
        for wd in self.window1.winfo_children(): # NOTE the hardcoded window1 attr , default must be winow
            wd.destroy()
    def ttt_ui(self,computer=None):
        for wiget in self.window1.winfo_children(): # OR use self.clear_winow() < custom wrapper func SAME THING
            wiget.destroy()
        self.window1.geometry("200x100")
        ttk.Label(self.window1,text="Who Should Move First ?").pack(pady=(0,5))
        ttk.Button(self.window1,text="Player",command=self.player_first).pack(pady=3)
        # ttk.Button(self.window1,text="Computer",command=self.computer_first).pack(pady=4,fill="x") #try
        ttk.Button(self.window1,text="Computer",command=self.computer_first).pack(pady=4)
    def player_first(self):
        self.clear_window()
        TTT=TicTacToe(self.window1,"player")
        # window1.mainloop()
    def computer_first(self):
        # self.window1.destroy()
        self.clear_window()
        TTT=TicTacToe(self.window1,"computer")
        # window3.focus_force() 
        # window3.mainloop()
window=tk.Tk()
# window.geometry("800x800")
window.title("TicTacToe")
AppX=App(window)
window.mainloop()