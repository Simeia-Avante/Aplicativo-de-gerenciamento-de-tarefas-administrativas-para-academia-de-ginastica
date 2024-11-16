import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import csv

# ======================
# Classe Produto para Controle de Estoque
# ======================
class Produto:
    def __init__(self, nome, categoria, fornecedor, quantidade_total=0, preco_unitario=0.0):
        self.nome = nome
        self.categoria = categoria
        self.fornecedor = fornecedor
        self.quantidade_total = quantidade_total
        self.preco_unitario = preco_unitario
        self.historico_movimentacao = []

    def entrada(self, quantidade, data=None):
        if data is None:
            data = datetime.now()
        self.quantidade_total += quantidade
        self.historico_movimentacao.append({
            'tipo': 'Entrada',
            'quantidade': quantidade,
            'data': data.strftime('%d/%m/%Y')
        })

    def saida(self, quantidade, data=None):
        if data is None:
            data = datetime.now()
        if quantidade <= self.quantidade_total:
            self.quantidade_total -= quantidade
            self.historico_movimentacao.append({
                'tipo': 'Saída',
                'quantidade': quantidade,
                'data': data.strftime('%d/%m/%Y')
            })
        else:
            messagebox.showerror("Erro de Estoque", f"Não há estoque suficiente de {self.nome} para retirar {quantidade} unidades.")

    def exportar_historico(self, filepath):
        with open(filepath, 'w', newline='') as csvfile:
            fieldnames = ['Tipo', 'Quantidade', 'Data']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for mov in self.historico_movimentacao:
                writer.writerow({'Tipo': mov['tipo'], 'Quantidade': mov['quantidade'], 'Data': mov['data']})

# ======================
# Classe Equipamento para Controle de Manutenção
# ======================
class Equipamento:
    def __init__(self, nome):
        self.nome = nome

# ======================
# Sistema de Login e Interface Gráfica (Tkinter)
# ======================
class SistemaAcademiaApp:
    # Lista de usuários permitidos
    usuarios_permitidos = {
        'Renan': 'Renan',
        'Leo': 'Leo',
        'Olli': 'Olli',
        'Anderson': 'Anderson',
        'Monara': 'Monara',
        'Adriel': 'Adriel'
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Academia")
        self.root.geometry("800x600")
        self.tela_login()  # Exibe a tela de login

    def tela_login(self):
        # Cria a interface de login
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=100)

        tk.Label(self.login_frame, text="Login", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2)

        tk.Label(self.login_frame, text="Usuário:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_usuario = tk.Entry(self.login_frame)
        self.entry_usuario.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.login_frame, text="Senha:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_senha = tk.Entry(self.login_frame, show="*")
        self.entry_senha.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.login_frame, text="Entrar", command=self.verificar_login).grid(row=3, column=0, columnspan=2, pady=10)

    def verificar_login(self):
        # Valida o login
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario in self.usuarios_permitidos and self.usuarios_permitidos[usuario] == senha:
            self.login_frame.destroy()
            self.inicializar_sistema()
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos!")

    def inicializar_sistema(self):
        # Inicializa os produtos e equipamentos
        self.produtos_estoque = [
            Produto("Água sanitária", "Limpeza", "Litro"),
            Produto("Álcool", "Limpeza", "Litro"),
            Produto("Borracha do rodo", "Limpeza", "Unidade"),
            Produto("Desinfetante", "Limpeza", "Litro"),
            Produto("Detergente", "Limpeza", "Litro"),
            Produto("Pá de lixo", "Limpeza", "Unidade"),
            Produto("Palha de aço", "Limpeza", "Pacote"),
            Produto("Papel higiênico", "Higiene", "Rolo"),
            Produto("Pano de chão 44X67", "Limpeza", "Unidade"),
            Produto("Pano de chão 90X65", "Limpeza", "Unidade"),
            Produto("Querosene", "Limpeza", "Litro"),
            Produto("Removedor", "Limpeza", "Litro"),
            Produto("Sabonete líquido", "Higiene", "Litro"),
            Produto("Saco de lixo 60L", "Limpeza", "Pacote"),
            Produto("Sabão em pó", "Limpeza", "Kg"),
            Produto("Sabão em pedra", "Limpeza", "Unidade"),
            Produto("Vassoura", "Limpeza", "Unidade")
        ]

        self.equipamentos = [
            Equipamento("Aparelho adutor/abdutor"),
            Equipamento("Secador de mão"),
            Equipamento("Lubrificação esteira"),
            Equipamento("Supino inclinado"),
            Equipamento("Barra do pulley"),
            Equipamento("Quadro de energia"),
            Equipamento("Reforma da máquina glúteo"),
            Equipamento("Máquina scot"),
            Equipamento("Lubrificação esteira 1,2,3 e 4"),
            Equipamento("Aparelho pulley"),
            Equipamento("Elevação pélvica"),
            Equipamento("Cross 1"),
            Equipamento("Cross 2"),
            Equipamento("Cross over"),
            Equipamento("Cross over 1"),
            Equipamento("Mesa flexora"),
            Equipamento("Extensora"),
            Equipamento("Esteira 1"),
            Equipamento("Esteira 2"),
            Equipamento("Esteira 2 1"),
            Equipamento("Esteira 4 3"),
            Equipamento("Esteira 1 2 3 4"),
            Equipamento("Ventilador pilates")
        ]

        self.educadores_fisicos = ["Renan", "Leo", "Olli", "Anderso"]
        self.escalas = []
        self.manutencoes = []
        self.cotacoes = []
        self.criar_abas()

    def criar_abas(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill='both')

        # Aba de Estoque
        self.aba_estoque = ttk.Frame(notebook)
        notebook.add(self.aba_estoque, text='Controle de Estoque')
        self.criar_aba_estoque()

        # Aba de Manutenção
        self.aba_manutencao = ttk.Frame(notebook)
        notebook.add(self.aba_manutencao, text='Serviços de Manutenção')
        self.criar_aba_manutencao()

        # Aba de Escala
        self.aba_escala = ttk.Frame(notebook)
        notebook.add(self.aba_escala, text='Escala de Educadores')
        self.criar_aba_escala()

        # Aba de Cadastro
        self.aba_cadastro = ttk.Frame(notebook)
        notebook.add(self.aba_cadastro, text='Cadastro')
        self.criar_aba_cadastro()

        # Aba de Cotação
        self.aba_cotacao = ttk.Frame(notebook)
        notebook.add(self.aba_cotacao, text='Cotação de Produtos')
        self.criar_aba_cotacao()

    def criar_aba_estoque(self):
        lbl_produto = ttk.Label(self.aba_estoque, text="Produto:")
        lbl_produto.grid(row=0, column=0, padx=10, pady=10)

        self.combo_produto = ttk.Combobox(self.aba_estoque, values=[p.nome for p in self.produtos_estoque])
        self.combo_produto.grid(row=0, column=1, padx=10, pady=10)

        lbl_quantidade = ttk.Label(self.aba_estoque, text="Quantidade:")
        lbl_quantidade.grid(row=1, column=0, padx=10, pady=10)

        self.entry_quantidade = ttk.Entry(self.aba_estoque)
        self.entry_quantidade.grid(row=1, column=1, padx=10, pady=10)

        btn_entrada = ttk.Button(self.aba_estoque, text="Registrar Entrada", command=self.registrar_entrada)
        btn_entrada.grid(row=2, column=0, padx=10, pady=10)

        btn_saida = ttk.Button(self.aba_estoque, text="Registrar Saída", command=self.registrar_saida)
        btn_saida.grid(row=2, column=1, padx=10, pady=10)

        # Subformulário para exibir movimentações
        self.tree_historico = ttk.Treeview(self.aba_estoque, columns=("tipo", "quantidade", "data"), show='headings')
        self.tree_historico.heading("tipo", text="Tipo")
        self.tree_historico.heading("quantidade", text="Quantidade")
        self.tree_historico.heading("data", text="Data")
        self.tree_historico.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        btn_historico = ttk.Button(self.aba_estoque, text="Exportar Histórico", command=self.exportar_historico)
        btn_historico.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def criar_aba_manutencao(self):
        lbl_equipamento = ttk.Label(self.aba_manutencao, text="Equipamento:")
        lbl_equipamento.grid(row=0, column=0, padx=10, pady=10)

        self.combo_equipamento = ttk.Combobox(self.aba_manutencao, values=[e.nome for e in self.equipamentos])
        self.combo_equipamento.grid(row=0, column=1, padx=10, pady=10)

        lbl_responsavel = ttk.Label(self.aba_manutencao, text="Responsável:")
        lbl_responsavel.grid(row=1, column=0, padx=10, pady=10)

        self.entry_responsavel = ttk.Entry(self.aba_manutencao)
        self.entry_responsavel.grid(row=1, column=1, padx=10, pady=10)

        btn_criar_manutencao = ttk.Button(self.aba_manutencao, text="Criar Manutenção", command=self.criar_manutencao)
        btn_criar_manutencao.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Subformulário para exibir manutenções
        self.tree_manutencao = ttk.Treeview(self.aba_manutencao, columns=("equipamento", "responsavel", "data_solicitacao"), show='headings')
        self.tree_manutencao.heading("equipamento", text="Equipamento")
        self.tree_manutencao.heading("responsavel", text="Responsável")
        self.tree_manutencao.heading("data_solicitacao", text="Data Solicitação")
        self.tree_manutencao.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        btn_exportar_manutencao = ttk.Button(self.aba_manutencao, text="Exportar Manutenção", command=self.exportar_manutencao)
        btn_exportar_manutencao.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def criar_aba_escala(self):
        lbl_educador = ttk.Label(self.aba_escala, text="Educador:")
        lbl_educador.grid(row=0, column=0, padx=10, pady=10)

        self.combo_educador = ttk.Combobox(self.aba_escala, values=self.educadores_fisicos)
        self.combo_educador.grid(row=0, column=1, padx=10, pady=10)

        lbl_dia_semana = ttk.Label(self.aba_escala, text="Dia da Semana:")
        lbl_dia_semana.grid(row=1, column=0, padx=10, pady=10)

        self.combo_dia_semana = ttk.Combobox(self.aba_escala, values=["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"])
        self.combo_dia_semana.grid(row=1, column=1, padx=10, pady=10)

        lbl_horarios = ttk.Label(self.aba_escala, text="Horários:")
        lbl_horarios.grid(row=2, column=0, padx=10, pady=10)

        self.entry_horarios = ttk.Entry(self.aba_escala)
        self.entry_horarios.grid(row=2, column=1, padx=10, pady=10)

        btn_criar_escala = ttk.Button(self.aba_escala, text="Criar Escala", command=self.criar_escala)
        btn_criar_escala.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Subformulário para exibir escalas
        self.tree_escala = ttk.Treeview(self.aba_escala, columns=("educador", "dia_semana", "horarios"), show='headings')
        self.tree_escala.heading("educador", text="Educador")
        self.tree_escala.heading("dia_semana", text="Dia da Semana")
        self.tree_escala.heading("horarios", text="Horários")
        self.tree_escala.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        btn_exportar_escala = ttk.Button(self.aba_escala, text="Exportar Escalas", command=self.exportar_escala)
        btn_exportar_escala.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def criar_aba_cadastro(self):
        lbl_titulo = ttk.Label(self.aba_cadastro, text="Cadastro de Produtos, Equipamentos e Educadores", font=("Helvetica", 14))
        lbl_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Cadastro de Produto
        lbl_produto_nome = ttk.Label(self.aba_cadastro, text="Nome do Produto:")
        lbl_produto_nome.grid(row=1, column=0, padx=10, pady=5)

        self.entry_produto_nome = ttk.Entry(self.aba_cadastro)
        self.entry_produto_nome.grid(row=1, column=1, padx=10, pady=5)

        lbl_produto_categoria = ttk.Label(self.aba_cadastro, text="Categoria do Produto:")
        lbl_produto_categoria.grid(row=2, column=0, padx=10, pady=5)

        self.entry_produto_categoria = ttk.Entry(self.aba_cadastro)
        self.entry_produto_categoria.grid(row=2, column=1, padx=10, pady=5)

        lbl_produto_fornecedor = ttk.Label(self.aba_cadastro, text="Fornecedor do Produto:")
        lbl_produto_fornecedor.grid(row=3, column=0, padx=10, pady=5)

        self.entry_produto_fornecedor = ttk.Entry(self.aba_cadastro)
        self.entry_produto_fornecedor.grid(row=3, column=1, padx=10, pady=5)

        btn_cadastrar_produto = ttk.Button(self.aba_cadastro, text="Cadastrar Produto", command=self.cadastrar_produto)
        btn_cadastrar_produto.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Cadastro de Equipamento
        lbl_equipamento_nome = ttk.Label(self.aba_cadastro, text="Nome do Equipamento:")
        lbl_equipamento_nome.grid(row=5, column=0, padx=10, pady=5)

        self.entry_equipamento_nome = ttk.Entry(self.aba_cadastro)
        self.entry_equipamento_nome.grid(row=5, column=1, padx=10, pady=5)

        btn_cadastrar_equipamento = ttk.Button(self.aba_cadastro, text="Cadastrar Equipamento", command=self.cadastrar_equipamento)
        btn_cadastrar_equipamento.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Cadastro de Educador Físico
        lbl_educador_nome = ttk.Label(self.aba_cadastro, text="Nome do Educador Físico:")
        lbl_educador_nome.grid(row=7, column=0, padx=10, pady=5)

        self.entry_educador_nome = ttk.Entry(self.aba_cadastro)
        self.entry_educador_nome.grid(row=7, column=1, padx=10, pady=5)

        btn_cadastrar_educador = ttk.Button(self.aba_cadastro, text="Cadastrar Educador", command=self.cadastrar_educador)
        btn_cadastrar_educador.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def criar_aba_cotacao(self):
        lbl_titulo = ttk.Label(self.aba_cotacao, text="Cotação de Produtos", font=("Helvetica", 14))
        lbl_titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        lbl_produto = ttk.Label(self.aba_cotacao, text="Produto:")
        lbl_produto.grid(row=1, column=0, padx=10, pady=5)

        self.combo_cotacao_produto = ttk.Combobox(self.aba_cotacao, values=[p.nome for p in self.produtos_estoque])
        self.combo_cotacao_produto.grid(row=1, column=1, padx=10, pady=5)

        lbl_quantidade = ttk.Label(self.aba_cotacao, text="Quantidade:")
        lbl_quantidade.grid(row=1, column=2, padx=10, pady=5)

        self.entry_cotacao_quantidade = ttk.Entry(self.aba_cotacao)
        self.entry_cotacao_quantidade.grid(row=1, column=3, padx=10, pady=5)

        btn_adicionar = ttk.Button(self.aba_cotacao, text="Adicionar à Cotação", command=self.adicionar_item_cotacao)
        btn_adicionar.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        # Subformulário para exibir itens da cotação
        self.tree_cotacao = ttk.Treeview(self.aba_cotacao, columns=("produto", "quantidade"), show='headings')
        self.tree_cotacao.heading("produto", text="Produto")
        self.tree_cotacao.heading("quantidade", text="Quantidade")
        self.tree_cotacao.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        btn_remover = ttk.Button(self.aba_cotacao, text="Remover Item", command=self.remover_item_cotacao)
        btn_remover.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        btn_exportar_cotacao = ttk.Button(self.aba_cotacao, text="Exportar Cotação", command=self.exportar_cotacao)
        btn_exportar_cotacao.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

    def adicionar_item_cotacao(self):
        produto_nome = self.combo_cotacao_produto.get()
        quantidade = self.entry_cotacao_quantidade.get()

        if not quantidade.isdigit():
            messagebox.showerror("Erro", "Por favor, insira uma quantidade válida.")
            return

        if not produto_nome:
            messagebox.showerror("Erro", "Por favor, selecione um produto.")
            return

        item_cotacao = {
            'produto': produto_nome,
            'quantidade': int(quantidade)
        }
        self.cotacoes.append(item_cotacao)
        messagebox.showinfo("Sucesso", f"Produto {produto_nome} adicionado à cotação.")
        self.atualizar_cotacao()

    def atualizar_cotacao(self):
        # Limpa a Treeview antes de inserir novos dados
        for item in self.tree_cotacao.get_children():
            self.tree_cotacao.delete(item)

        # Insere os dados dos itens da cotação na Treeview
        for item in self.cotacoes:
            self.tree_cotacao.insert("", "end", values=(item['produto'], item['quantidade']))

    def remover_item_cotacao(self):
        selected_item = self.tree_cotacao.selection()
        if selected_item:
            item = self.tree_cotacao.item(selected_item)
            produto_nome = item['values'][0]
            self.cotacoes = [i for i in self.cotacoes if i['produto'] != produto_nome]
            self.tree_cotacao.delete(selected_item)
            messagebox.showinfo("Sucesso", f"Produto {produto_nome} removido da cotação.")
        else:
            messagebox.showerror("Erro", "Por favor, selecione um item para remover.")

    def exportar_cotacao(self):
        if not self.cotacoes:
            messagebox.showerror("Erro", "Não há itens na cotação para exportar.")
            return

        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Salvar Cotação de Produtos")
        if filepath:
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = ['Produto', 'Quantidade']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for item in self.cotacoes:
                    writer.writerow({'Produto': item['produto'], 'Quantidade': item['quantidade']})
            messagebox.showinfo("Exportação Concluída", f"Cotação exportada para {filepath}")

    def cadastrar_produto(self):
        nome = self.entry_produto_nome.get()
        categoria = self.entry_produto_categoria.get()
        fornecedor = self.entry_produto_fornecedor.get()

        if nome and categoria and fornecedor:
            novo_produto = Produto(nome, categoria, fornecedor)
            self.produtos_estoque.append(novo_produto)
            self.combo_produto['values'] = [p.nome for p in self.produtos_estoque]
            self.combo_cotacao_produto['values'] = [p.nome for p in self.produtos_estoque]
            messagebox.showinfo("Sucesso", f"Produto {nome} cadastrado com sucesso.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos do produto.")

    def cadastrar_equipamento(self):
        nome = self.entry_equipamento_nome.get()

        if nome:
            novo_equipamento = Equipamento(nome)
            self.equipamentos.append(novo_equipamento)
            self.combo_equipamento['values'] = [e.nome for e in self.equipamentos]
            messagebox.showinfo("Sucesso", f"Equipamento {nome} cadastrado com sucesso.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha o nome do equipamento.")

    def cadastrar_educador(self):
        nome = self.entry_educador_nome.get()

        if nome:
            self.educadores_fisicos.append(nome)
            self.combo_educador['values'] = self.educadores_fisicos
            messagebox.showinfo("Sucesso", f"Educador {nome} cadastrado com sucesso.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha o nome do educador.")

    def registrar_entrada(self):
        produto_nome = self.combo_produto.get()
        quantidade = self.entry_quantidade.get()

        if not quantidade.isdigit():
            messagebox.showerror("Erro", "Por favor, insira uma quantidade válida.")
            return

        for produto in self.produtos_estoque:
            if produto.nome == produto_nome:
                produto.entrada(int(quantidade))
                messagebox.showinfo("Sucesso", f"Entrada de {quantidade} unidades de {produto_nome} registrada.")
                self.atualizar_historico(produto)
                return

    def registrar_saida(self):
        produto_nome = self.combo_produto.get()
        quantidade = self.entry_quantidade.get()

        if not quantidade.isdigit():
            messagebox.showerror("Erro", "Por favor, insira uma quantidade válida.")
            return

        for produto in self.produtos_estoque:
            if produto.nome == produto_nome:
                produto.saida(int(quantidade))
                messagebox.showinfo("Sucesso", f"Saída de {quantidade} unidades de {produto_nome} registrada.")
                self.atualizar_historico(produto)
                return

    def atualizar_historico(self, produto):
        # Limpa a Treeview antes de inserir novos dados
        for item in self.tree_historico.get_children():
            self.tree_historico.delete(item)

        # Insere os dados do histórico na Treeview
        for mov in produto.historico_movimentacao:
            self.tree_historico.insert("", "end", values=(mov['tipo'], mov['quantidade'], mov['data']))

    def exportar_historico(self):
        produto_nome = self.combo_produto.get()

        for produto in self.produtos_estoque:
            if produto.nome == produto_nome:
                filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Salvar Histórico de Estoque")
                if filepath:
                    produto.exportar_historico(filepath)
                    messagebox.showinfo("Exportação Concluída", f"Histórico exportado para {filepath}")
                return

    def criar_manutencao(self):
        equipamento_nome = self.combo_equipamento.get()
        responsavel = self.entry_responsavel.get()
        data_solicitacao = datetime.now()

        manutencao = {
            'equipamento': equipamento_nome,
            'responsavel': responsavel,
            'data_solicitacao': data_solicitacao.strftime('%d/%m/%Y')
        }
        self.manutencoes.append(manutencao)
        messagebox.showinfo("Manutenção Criada", f"Manutenção do equipamento {equipamento_nome} criada com sucesso.")
        self.atualizar_manutencao()

    def atualizar_manutencao(self):
        # Limpa a Treeview antes de inserir novos dados
        for item in self.tree_manutencao.get_children():
            self.tree_manutencao.delete(item)

        # Insere os dados das manutenções na Treeview
        for manutencao in self.manutencoes:
            self.tree_manutencao.insert("", "end", values=(manutencao['equipamento'], manutencao['responsavel'], manutencao['data_solicitacao']))

    def exportar_manutencao(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Salvar Histórico de Manutenção")
        if filepath:
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = ['Equipamento', 'Responsável', 'Data Solicitação']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for manutencao in self.manutencoes:
                    writer.writerow({'Equipamento': manutencao['equipamento'], 'Responsável': manutencao['responsavel'], 'Data Solicitação': manutencao['data_solicitacao']})
            messagebox.showinfo("Exportação Concluída", f"Manutenções exportadas para {filepath}")

    def criar_escala(self):
        educador = self.combo_educador.get()
        dia_semana = self.combo_dia_semana.get()
        horarios = self.entry_horarios.get()

        escala = {
            'educador': educador,
            'dia_semana': dia_semana,
            'horarios': horarios
        }
        self.escalas.append(escala)
        messagebox.showinfo("Sucesso", f"Escala para {educador} criada com sucesso para {dia_semana}.")
        self.atualizar_escala()

    def atualizar_escala(self):
        # Limpa a Treeview antes de inserir novos dados
        for item in self.tree_escala.get_children():
            self.tree_escala.delete(item)

        # Insere os dados das escalas na Treeview
        for escala in self.escalas:
            self.tree_escala.insert("", "end", values=(escala['educador'], escala['dia_semana'], escala['horarios']))

    def exportar_escala(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")], title="Salvar Escalas de Educadores")
        if filepath:
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = ['Educador', 'Dia da Semana', 'Horários']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for escala in self.escalas:
                    writer.writerow({'Educador': escala['educador'], 'Dia da Semana': escala['dia_semana'], 'Horários': escala['horarios']})
            messagebox.showinfo("Exportação Concluída", f"Escalas exportadas para {filepath}")

# ======================
# Inicialização do Tkinter
# ======================
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAcademiaApp(root)
    root.mainloop()
