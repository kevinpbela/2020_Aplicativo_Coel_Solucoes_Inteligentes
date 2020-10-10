class Parametros:
    def __init__(self, id_parametros, tab_de_alarmes,
                 tab_parametros, tab_parametros_dois, id_produto):
        self.id_parametros = id_parametros
        self.tab_de_alarmes = tab_de_alarmes
        self.tab_parametros = tab_parametros
        self.tab_parametros_dois = tab_parametros_dois
        self.id_produto = id_produto

    def atualizar(self, dados):
        try:
            id_parametros = dados["id_parametros"]
            tab_de_alarmes = dados["tab_de_alarmes"]
            tab_parametros = dados["tab_parametros"]
            tab_parametros_dois = dados["tab_parametros_dois"]
            id_produto = dados["id_produto"]
            self.id_parametros, self.tab_de_alarmes, self.tab_parametros,
            self.tab_parametros_dois, self.id_produto = id_parametros, tab_de_alarmes,
            tab_parametros, tab_parametros_dois, id_produto

            return self
        except Exception as e:
            print("Problema ao criar novo Parametros!")
            print(e)

    def __dict__(self):
        d = dict()
        d['id_parametros'] = self.id_parametros
        d['tab_de_alarmes'] = self.tab_de_alarmes
        d['tab_parametros'] = self.tab_parametros
        d['tab_parametros_dois'] = self.tab_parametros_dois
        d['id_produto'] = self.id_produto
        return d

    @staticmethod
    def criar(dados):
        try:
            id_parametros = dados["id_parametros"]
            tab_de_alarmes = dados["tab_de_alarmes"]
            tab_parametros = dados["tab_parametros"]
            tab_parametros_dois = dados["tab_parametros_dois"]
            id_produto = dados["id_produto"]
            return Parametros(id_parametros=id_parametros, tab_de_alarmes=tab_de_alarmes,
                           tab_parametros=tab_parametros, tab_parametros_dois=tab_parametros_dois,
                           id_produto=id_produto)
        except Exception as e:
            print("Problema ao criar novo Parametros!")
            print(e)
