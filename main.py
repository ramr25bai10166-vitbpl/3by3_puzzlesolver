import tkinter as tk               # for the gui
from tkinter import messagebox     # for error boxes
import random                      # to shuffle the board
import solver                      # where the math happens

class PuzzleUI:
    def __init__(self,root):
        # setup main window
        self.root=root
        self.root.title("3x3 Puzzle Solver")
        self.root.geometry("450x850")
        self.root.configure(padx=20,pady=20, bg="#f0f0f0")
        
        self.goal=(1,2,3,4,5,6,7,8,0)
        self.curr=list(self.goal)
        self.sol_path=[]
        self.step=0
        
        title_lbl=tk.Label(root,text="AI Puzzle Solver", font=("Helvetica",20,"bold"),bg="#f0f0f0")
        title_lbl.pack(pady=5)

        self.grid_frm=tk.Frame(root,bg="#f0f0f0")
        self.grid_frm.pack(pady=10)
        
        self.tiles=[]
        for i in range(9):
            r=i//3
            c=i%3
            bdr=tk.Frame(self.grid_frm, bg="#333",bd=2)
            bdr.grid(row=r,column=c, padx=5,pady=5)
            
            lbl=tk.Label(bdr,text="", font=("Helvetica",36,"bold"),width=3,height=1, bg="white",fg="#333")
            lbl.pack(expand=True,fill='both')
            
            lbl.bind("<Button-1>",lambda event,idx=i:self.on_click(idx))
            self.tiles.append(lbl)
            
        self.info_lbl=tk.Label(root,text="Click 'Shuffle' or manually move tiles.", font=("Helvetica",14),bg="#f0f0f0")
        self.info_lbl.pack(pady=10)
        
        self.ctrl_frm=tk.Frame(root,bg="#f0f0f0")
        self.ctrl_frm.pack(pady=5)
        
        btn_font=("Helvetica",12,"bold")
        
        self.btn_shuf=tk.Button(self.ctrl_frm,text="Shuffle", command=self.shuffle,width=12,font=btn_font,bg="#2196F3",fg="white")
        self.btn_shuf.grid(row=0,column=0,padx=8,pady=8)
        
        self.btn_solve=tk.Button(self.ctrl_frm, text="Solve",command=self.solve,width=12, font=btn_font,bg="#4CAF50",fg="white")
        self.btn_solve.grid(row=0,column=1,padx=8,pady=8)
        
        self.btn_steps=tk.Button(self.ctrl_frm,text="Show steps",command=self.show_first, width=12,font=btn_font,bg="#FF9800",fg="white",state=tk.DISABLED)
        self.btn_steps.grid(row=1,column=0,padx=8,pady=8)
        
        self.btn_quit=tk.Button(self.ctrl_frm,text="Quit",command=self.root.quit,width=12,font=btn_font, bg="#f44336",fg="white")
        self.btn_quit.grid(row=1,column=1,padx=8,pady=8)
        
        self.update_main()

        self.sol_cnt=tk.Frame(root, bg="#f0f0f0")
        
        self.sol_lbl=tk.Label(self.sol_cnt, text="Solution Steps:",font=("Helvetica",14,"bold"), bg="#f0f0f0")
        self.sol_lbl.pack(pady=5)
        
        self.sol_frm=tk.Frame(self.sol_cnt,bg="#f0f0f0")
        self.sol_frm.pack()
        
        self.sol_tiles=[]
        for i in range(9):
            r=i//3
            c=i%3
            bdr= tk.Frame(self.sol_frm,bg="#333",bd=2)
            bdr.grid(row=r,column=c,padx=3,pady=3)
            
            lbl= tk.Label(bdr,text="",font=("Helvetica",24,"bold"),width=3,height=1,bg="white",fg="#333")
            lbl.pack(expand=True,fill='both')
            self.sol_tiles.append(lbl)

        self.btn_next = tk.Button(self.sol_cnt,text="Next",command=self.show_next,width=12,font=btn_font,bg="#9C27B0",fg="white")

    def on_click(self,idx):
        emp_idx=self.curr.index(0)
        
        r1,c1=idx//3, idx%3
        r2,c2=emp_idx//3, emp_idx%3

        # swap tiles if they next to each other
        if abs(r1-r2)+abs(c1-c2)==1:
            self.curr[emp_idx], self.curr[idx]=self.curr[idx],self.curr[emp_idx]
            self.update_main()
            
            self.sol_cnt.pack_forget()
            self.btn_steps.config(state=tk.DISABLED)
            self.btn_next.pack_forget()
            self.btn_solve.config(state=tk.NORMAL)
            self.info_lbl.config(text="Custom board. Click Solve when ready.")

    def update_main(self):
        for i,val in enumerate(self.curr):
            if val==0:
                self.tiles[i].config(text="",bg="#cfcfcf")
            else:
                self.tiles[i].config(text=str(val),bg="white")

    def update_sol(self,state):
        for i,val in enumerate(state):
            if val==0:
                self.sol_tiles[i].config(text="", bg="#cfcfcf")
            else:
                self.sol_tiles[i].config(text=str(val), bg="#fff9c4") 

    def shuffle(self):
        st=list(self.goal)
        prev=set([tuple(st)])

        # 50 random valid moves to shuffle
        for _ in range(50):
            nbrs=solver.get_nbrs(tuple(st))
            valid=[n for n in nbrs if tuple(n) not in prev]
            if not valid: 
                valid=nbrs
            
            nxt=random.choice(valid)
            prev.add(nxt)
            st=list(nxt)
            
        self.curr=list(st)
        self.update_main()
        
        self.sol_cnt.pack_forget()
        self.btn_steps.config(state=tk.DISABLED)
        self.btn_next.pack_forget()
        self.btn_solve.config(state=tk.NORMAL)
        self.info_lbl.config(text="Puzzle shuffled. Ready to solve.")

    def solve(self):
        if tuple(self.curr) == self.goal:
            self.info_lbl.config(text="Already solved!")
            return

        self.info_lbl.config(text="Solving...")
        self.btn_solve.config(state=tk.DISABLED)
        self.root.update()
        
        self.sol_path = solver.solve(tuple(self.curr))

        # check if it actually solved
        if self.sol_path:
            tot= len(self.sol_path)-1
            self.info_lbl.config(text=f"Min steps: {tot}.")
            self.btn_steps.config(state=tk.NORMAL)
        else:
            self.info_lbl.config(text="Error: Unsolvable state.")
            self.btn_solve.config(state=tk.NORMAL)

    def show_first(self):
        self.step=1
        
        self.sol_cnt.pack(pady=10)
        self.update_sol(self.sol_path[self.step])
        
        tot=len(self.sol_path)-1
        self.sol_lbl.config(text=f"Step {self.step} / {tot}")
        
        self.btn_steps.config(state=tk.DISABLED)
        self.btn_next.pack(pady=10)
        self.btn_next.config(state=tk.NORMAL)
        
        if self.step ==tot:
            self.btn_next.config(state=tk.DISABLED)
            self.sol_lbl.config(text="Solved! (1 step)")

    def show_next(self):
        if self.step<len(self.sol_path)-1:
            self.step+=1
            self.update_sol(self.sol_path[self.step])
            
            tot=len(self.sol_path)-1
            self.sol_lbl.config(text=f"Step {self.step} / {tot}")
            
            if self.step==tot:
                self.btn_next.config(state=tk.DISABLED)
                self.sol_lbl.config(text="Goal Reached!")

if __name__=="__main__":
    root=tk.Tk()
    app=PuzzleUI(root)
    root.mainloop()
