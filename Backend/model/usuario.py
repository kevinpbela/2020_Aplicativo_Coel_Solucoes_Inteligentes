class Usuario:

    def __init__(self, id, email: str, login, nome, senha):
        self.id = id
        self.email = email
        self.login = login
        self.nome = nome
        self.senha = senha

    def atualizar(self, dados):
        try:
            id = dados["id"]
            email = dados["email"]
            login = dados["login"]
            nome = dados["nome"]
            senha = dados["senha"]
            self.id, self.email, self.login, self.nome, self.senha = id, email, login, nome, senha
            return self
        except Exception as e:
            print("Problema ao criar novo Usuario!")
            print(e)

    def __dict__(self):
        d = dict()
        d['id'] = self.id
        d['email'] = self.email
        d['login'] = self.login
        d['nome'] = self.nome
        d['senha'] = self.senha
        return d

    @staticmethod
    def criar(dados):
        try:
            id = dados["id"]
            email = dados["email"]
            login = dados["login"]
            nome = dados["nome"]
            senha = dados["senha"]
            return Usuario(id=id, email=email, login=login, nome=nome, senha=senha)
        except Exception as e:
            print("Problema ao criar novo Usuario!")
            print(e)
