class Login:

    def __init__(self, id_usuario, login, senha):
        self.id_usuario = id_usuario
        self.login = login
        self.senha = senha

    def atualizar(self, dados):
        try:
            id_usuario = dados["id_usuario"]
            login = dados["login"]
            senha = dados["senha"]
            self.id_usuario, self.login, self.senha = id_usuario, login, senha
            return self
        except Exception as e:
            print("Problema ao criar novo Usuario!")
            print(e)

    def __dict__(self):
        d = dict()
        d['id_usuario'] = self.id_usuario
        d['login'] = self.login
        d['senha'] = self.senha
        return d

    @staticmethod
    def criar(dados):
        try:
            id_usuario = dados["id_usuario"]
            login = dados["login"]
            senha = dados["senha"]
            return Login(id_usuario=id_usuario, login=login, senha=senha)
        except Exception as e:
            print("Problema ao criar novo Usuario!")
            print(e)
