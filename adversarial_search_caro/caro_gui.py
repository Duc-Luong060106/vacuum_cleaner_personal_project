import tkinter as tk
import time

from helper import get_next_turn, generate_next_states, is_terminal, evaluate_if_terminal
from minimax_search import MiniMax
from alpha_beta_search import AlphaBeta
from expectimax_search import Expectimax

ALGO_MAP = ('Minimax', 'Alpha-Beta', 'Expectimax')

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Cờ Caro')
        self.root.resizable(False, False)

        BG       = '#F8F7F4'
        PANEL_BG = '#EEEDFE'
        BTN_BG   = '#534AB7'
        BTN_FG   = '#FFFFFF'
        CELL_BG  = '#FFFFFF'
        CELL_HOV = '#F1EFE8'
        BORDER   = '#D3D1C7'
        TEXT_SEC = '#5F5E5A'

        self.X_COLOR = '#534AB7'
        self.O_COLOR = '#993C1D'
        self.CELL_BG = CELL_BG
        self.root.configure(bg=BG)


        main_frame = tk.Frame(self.root, bg=BG)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, bg=BG)
        left_frame.pack(side='left', fill='y')

        right_frame = tk.Frame(main_frame, bg=PANEL_BG, padx=10, pady=10, highlightbackground=BORDER, highlightthickness=1)
        right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        top = tk.Frame(left_frame, bg=PANEL_BG, padx=16, pady=5)
        top.pack(fill='x')
        tk.Label(top, text='Chọn thuật toán cho Agent:', bg=PANEL_BG, font=('Helvetica', 11), fg=TEXT_SEC).pack(side='left')

        self.algo_var = tk.StringVar(value='Alpha-Beta')
        for name in ALGO_MAP:
            tk.Radiobutton(top, text=name, variable=self.algo_var, value=name,
                           bg=PANEL_BG, activebackground=PANEL_BG,
                           font=('Helvetica', 11), fg='#3C3489',
                           selectcolor=PANEL_BG, cursor='hand2',
                           command=self.on_algo_change).pack(side='left', padx=10)

        turn_frame = tk.Frame(left_frame, bg=PANEL_BG, padx=16, pady=5)
        turn_frame.pack(fill='x')
        tk.Label(turn_frame, text='Người đi trước:', bg=PANEL_BG, font=('Helvetica', 11), fg=TEXT_SEC).pack(side='left')

        self.first_player_var = tk.StringVar(value='Human')
        self.rb_human = tk.Radiobutton(turn_frame, text='Bạn (X)', variable=self.first_player_var, value='Human',
                       bg=PANEL_BG, activebackground=PANEL_BG, font=('Helvetica', 11), fg='#3C3489',
                       selectcolor=PANEL_BG, cursor='hand2', command=self.reset)
        self.rb_human.pack(side='left', padx=10)

        self.rb_ai = tk.Radiobutton(turn_frame, text='Agent (X)', variable=self.first_player_var, value='AI',
                       bg=PANEL_BG, activebackground=PANEL_BG, font=('Helvetica', 11), fg='#3C3489',
                       selectcolor=PANEL_BG, cursor='hand2', command=self.reset)
        self.rb_ai.pack(side='left', padx=10)

        board_frame = tk.Frame(left_frame, bg=BG, padx=24, pady=20)
        board_frame.pack()

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    board_frame, text='', width=4, height=2,
                    font=('Helvetica', 28, 'bold'),
                    bg=CELL_BG, relief='flat',
                    highlightbackground=BORDER, highlightthickness=1,
                    cursor='hand2',
                    command=lambda r=i, c=j: self.human_move(r, c)
                )
                btn.grid(row=i, column=j, padx=4, pady=4)
                btn.bind('<Enter>', lambda e, b=btn: b.config(bg=CELL_HOV))
                btn.bind('<Leave>', lambda e, b=btn: b.config(bg=self.CELL_BG))
                row.append(btn)
            self.buttons.append(row)

        bottom = tk.Frame(left_frame, bg=BG, pady=10)
        bottom.pack(fill='x')

        self.status_var = tk.StringVar()
        tk.Label(bottom, textvariable=self.status_var, font=('Helvetica', 13), bg=BG, fg=TEXT_SEC).pack()
        tk.Button(bottom, text='Chơi lại', font=('Helvetica', 11), bg=BTN_BG, fg=BTN_FG, relief='flat',
                  padx=20, pady=6, cursor='hand2', command=self.reset).pack(pady=8)


        tk.Label(right_frame, text='Log panel', bg=PANEL_BG, font=('Helvetica', 12, 'bold'), fg=TEXT_SEC).pack(anchor='w', pady=(0, 5))
        
        self.log_text = tk.Text(right_frame, width=40, height=20, font=('Consolas', 10), state='disabled', relief='flat', bg='#FFFFFF')
        scrollbar = tk.Scrollbar(right_frame, command=self.log_text.yview)
        self.log_text.config(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        self.reset()

    def write_log(self, message):
        self.log_text.config(state='normal')
        self.log_text.insert('end', message + '\n')
        self.log_text.see('end') 
        self.log_text.config(state='disabled')

    def on_algo_change(self):
        if self.algo_var.get() == 'Expectimax':
            self.first_player_var.set('AI')
            self.rb_human.config(state='disabled')
        else:
            self.rb_human.config(state='normal')
        self.reset()

    def render(self):
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                color = self.X_COLOR if val == 'X' else (self.O_COLOR if val == 'O' else '#CCCCCC')
                self.buttons[i][j].config(text=val if val != ' ' else '', fg=color)

    def check_end(self):
        if is_terminal(self.board):
            val = evaluate_if_terminal(self.board)
            if val == 1:
                winner = 'Bạn' if self.human_piece == 'X' else 'Agent'
                self.status_var.set(f'{winner} thắng!')
                self.write_log(f"\n--- KẾT THÚC: {winner.upper()} THẮNG! ---")
            elif val == -1:
                winner = 'Bạn' if self.human_piece == 'O' else 'Agent'
                self.status_var.set(f'{winner} thắng!')
                self.write_log(f"\n--- KẾT THÚC: {winner.upper()} THẮNG! ---")
            else:
                self.status_var.set('Hòa!')
                self.write_log("\n--- KẾT THÚC: HÒA! ---")
                
            self.game_over = True
            return True
        return False

    def human_move(self, r, c):
        if self.game_over or self.board[r][c] != ' ': return
        if get_next_turn(self.board) != self.human_piece: return

        self.board[r][c] = self.human_piece
        self.write_log(f"- Người ({self.human_piece}): Đánh ô ({r}, {c})")
        self.render()
        if self.check_end(): return
            
        self.status_var.set('AI đang suy nghĩ...')
        self.root.after(50, self.ai_move)

    def ai_move(self):
        if self.game_over: return
        
        algo = self.algo_var.get()
        pos = None
        val = 0
        
        start_time = time.time()
        
        if algo == 'Minimax':
            ai_instance = MiniMax(self.board)
            val, pos = ai_instance.minimax_search()
        elif algo == 'Alpha-Beta':
            ai_instance = AlphaBeta(self.board)
            val, pos = ai_instance.alpha_beta_search()
        elif algo == 'Expectimax':
            ai_instance = Expectimax(self.board)
            val, pos = ai_instance.expectimax_search()
                
        end_time = time.time()
        search_time = (end_time - start_time) * 1000 
            
        if pos:
            self.board[pos[0]][pos[1]] = self.ai_piece
            
            val_str = f"{val:.2f}" if isinstance(val, float) else f"{val}"
            
            self.write_log(f"- Agent ({self.ai_piece}): Đánh ô ({pos[0]}, {pos[1]})")
            self.write_log(f"  --> Đánh giá: {val_str} | Tgian: {search_time:.1f} ms")
            
            self.render()
            if not self.check_end():
                self.status_var.set(f'Lượt của bạn ({self.human_piece})')

    def reset(self):
        self.board = [[' '] * 3 for _ in range(3)]
        self.game_over = False
        
        self.log_text.config(state='normal')
        self.log_text.delete('1.0', 'end')
        self.log_text.config(state='disabled')
        
        if self.first_player_var.get() == 'Human':
            self.human_piece = 'X'
            self.ai_piece = 'O'
            self.status_var.set(f'Lượt của bạn ({self.human_piece})')
            self.write_log("--- TRẬN MỚI BẮT ĐẦU ---")
            self.write_log("Người chơi đi trước (X)")
        else:
            self.human_piece = 'O'
            self.ai_piece = 'X'
            self.status_var.set('AI đang suy nghĩ...')
            self.write_log("--- TRẬN MỚI BẮT ĐẦU ---")
            self.write_log(f"AI đi trước (X) bằng {self.algo_var.get()}")
            
        self.render()
        
        if self.first_player_var.get() == 'AI':
            self.root.after(50, self.ai_move)

if __name__ == '__main__':
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()