# SELECT TOP (1000) [id_categoria]
#       ,[categoria]
#       ,[sub_categoria_um]
#       ,[sub_categoria_dois]
#       ,[sub_categoria_tres]
#       ,[sub_categoria_quatro]
#       ,[id_produto]
#   FROM [dbo].[categoria]



class Categoria:

    def __init__(self, id_categoria, categoria, sub_categoria_um,
                 sub_categoria_dois, sub_categoria_tres, sub_categoria_quatro,
                 id_produto):

        self.id_categoria = id_categoria
        self.categoria = categoria
        self.sub_categoria_um = sub_categoria_um
        self.sub_categoria_dois = sub_categoria_dois
        self.sub_categoria_tres = sub_categoria_tres
        self.sub_categoria_quatro = sub_categoria_quatro
        self.id_produto = id_produto

    def atualizar(self, dados):
        try:
            id_categoria = dados["id_categoria"]
            categoria = dados["categoria"]
            sub_categoria_um = dados["sub_categoria_um"]
            sub_categoria_dois = dados["sub_categoria_dois"]
            sub_categoria_tres = dados["sub_categoria_tres"]
            sub_categoria_quatro = dados["sub_categoria_quatro"]
            id_produto = dados["id_produto"]

            self.id_categoria, self.categoria, self.sub_categoria_um,
            self.sub_categoria_dois, self.sub_categoria_tres,
            self.sub_categoria_quatro,
            self.id_produto = id_categoria,
            categoria, sub_categoria_um, sub_categoria_dois, sub_categoria_tres,
            sub_categoria_quatro, id_produto

            return self
        except Exception as e:
            print("Problema ao criar novo Categoria!")
            print(e)

    def __dict__(self):
        d = dict()
        d["id_categoria"] = self.id_categoria
        d["categoria"] = self.categoria
        d["sub_categoria_um"] = self.sub_categoria_um
        d["sub_categoria_dois"] = self.sub_categoria_dois
        d["sub_categoria_tres"] = self.sub_categoria_tres
        d["sub_categoria_quatro"] = self.sub_categoria_quatro
        d["id_produto"] = self.id_produto

        return d

    @staticmethod
    def criar(dados):
        try:
            id_categoria = dados["id_categoria"]
            categoria = dados["categoria"]
            sub_categoria_um = dados["sub_categoria_um"]
            sub_categoria_dois = dados["sub_categoria_dois"]
            sub_categoria_tres = dados["sub_categoria_tres"]
            sub_categoria_quatro = dados["sub_categoria_quatro"]
            id_produto = dados["id_produto"]

            return Categoria(id_categoria=id_categoria, categoria=categoria,
                             sub_categoria_um=sub_categoria_um,
                             sub_categoria_dois=sub_categoria_dois,
                             sub_categoria_tres=sub_categoria_tres,
                             sub_categoria_quatro=sub_categoria_quatro,
                             id_produto=id_produto)
        
        except Exception as e:
            print("Problema ao criar novo Categoria!")
            print(e)