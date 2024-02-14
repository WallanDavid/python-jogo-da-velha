import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")

        self.turno = "X"

        self.botoes = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.janela, text="", font=("Helvetica", 24), width=5, height=2,
                                              command=lambda row=i, col=j: self.clique_botao(row, col))
                self.botoes[i][j].grid(row=i, column=j)

    def clique_botao(self, row, col):
        if self.botoes[row][col]["text"] == "":
            self.botoes[row][col]["text"] = self.turno
            if self.verificar_vitoria(row, col):
                messagebox.showinfo("Fim do Jogo", f"O jogador {self.turno} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim do Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.mudar_turno()

    def verificar_vitoria(self, row, col):
        # Verifica se há vitória na linha, coluna ou diagonal
        return self.verificar_linha(row) or self.verificar_coluna(col) or self.verificar_diagonais(row, col)

    def verificar_linha(self, row):
        return all(self.botoes[row][col]["text"] == self.turno for col in range(3))

    def verificar_coluna(self, col):
        return all(self.botoes[row][col]["text"] == self.turno for row in range(3))

    def verificar_diagonais(self, row, col):
        if row == col or row + col == 2:
            return self.verificar_diagonal_principal() or self.verificar_diagonal_secundaria()
        return False

    def verificar_diagonal_principal(self):
        return all(self.botoes[i][i]["text"] == self.turno for i in range(3))

    def verificar_diagonal_secundaria(self):
        return all(self.botoes[i][2 - i]["text"] == self.turno for i in range(3))

    def verificar_empate(self):
        return all(self.botoes[i][j]["text"] != "" for i in range(3) for j in range(3))

    def mudar_turno(self):
        self.turno = "O" if self.turno == "X" else "X"

    def reiniciar_jogo(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j]["text"] = ""
        self.turno = "X"

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.janela.mainloop()
