class Produto:
    def __init__(self, id_produto, alimentacao, caracteristica,
                 categoria_venda, certificado, codigo_pedido,
                 descricao_completa, descricao_reduzida,
                 fabricante, funcao, id_categoria, modelo,
                 montagem, status, tag, id_parametros,
                 id_equivalencia, id_historico, id_ligacoes):
        self.id_produto = id_produto
        self.alimentacao = alimentacao
        self.caracteristica = caracteristica
        self.categoria_venda = categoria_venda
        self.certificado = certificado
        self.codigo_pedido = codigo_pedido
        self.descricao_completa = descricao_completa
        self.descricao_reduzida = descricao_reduzida
        self.fabricante = fabricante
        self.funcao = funcao
        self.id_categoria = id_categoria
        self.modelo = modelo
        self.montagem = montagem
        self.status = status
        self.tag = tag
        self.id_parametros = id_parametros

        self.id_equivalencia = id_equivalencia
        self.id_historico = id_historico
        self.id_ligacoes = id_ligacoes

    def atualizar(self, dados):
        try:
            id_produto = ["id_produto"]
            alimentacao = ["alimentacao"]
            caracteristica = ["caracteristica"]
            categoria_venda = ["categoria_venda"]
            certificado = ["certificado"]
            codigo_pedido = ["codigo_pedido"]
            descricao_completa = ["descricao_completa"]
            descricao_reduzida = ["descricao_reduzida"]
            fabricante = ["fabricante"]
            funcao = ["funcao"]
            id_categoria = ["id_categoria"]
            modelo = ["modelo"]
            montagem = ["montagem"]
            status = ["status"]
            tag = ["tag"]
            id_parametros = ["id_parametros"]

            id_equivalencia = ["id_equivalencia"]
            id_historico = ["id_historico"]
            id_ligacoes = ["id_ligacoes"]

            self.id_produto = id_produto,
            self.alimentacao = alimentacao,
            self.caracteristica = caracteristica,
            self.categoria_venda = categoria_venda,
            self.certificado = certificado,
            self.codigo_pedido = codigo_pedido,
            self.descricao_completa = descricao_completa
            self.descricao_reduzida = descricao_reduzida,
            self.fabricante = fabricante,
            self.funcao = funcao,
            self.id_categoria = id_categoria,
            self.modelo = modelo,
            self.montagem = montagem,
            self.status = status,
            self.tag = tag,
            self.id_parametros = id_parametros

            self.id_equivalencia = id_equivalencia
            self.id_historico = id_historico
            self.id_ligacoes = id_ligacoes
        except Exception as error:
            print("Problema ao criar novo produto!")
            print(error)

    def __dict__(self):
        d = dict()
        d["id_produto"] = self.id_produto
        d["alimentacao"] = self.alimentacao
        d["caracteristica"] = self.caracteristica
        d["categoria_venda"] = self.categoria_venda
        d["certificado"] = self.certificado
        d["codigo_pedido"] = self.codigo_pedido
        d["descricao_completa"] = self.descricao_completa
        d["descricao_reduzida"] = self.descricao_reduzida
        d["fabricante"] = self.fabricante
        d["funcao"] = self.funcao
        d["id_categoria"] = self.id_categoria
        d["modelo"] = self.modelo
        d["montagem"] = self.montagem
        d["status"] = self.status
        d["tag"] = self.tag
        d["id_parametros"] = self.id_parametros

        d["id_equivalencia"] = self.id_equivalencia
        d["id_historico"] = self.id_historico
        d["id_ligacoes"] = self.id_ligacoes

        return d

    @staticmethod
    def criar(dados):
        try:
            id_produto = ["id_produto"]
            alimentacao = ["alimentacao"]
            caracteristica = ["caracteristica"]
            categoria_venda = ["categoria_venda"]
            certificado = ["certificado"]
            codigo_pedido = ["codigo_pedido"]
            descricao_completa = ["descricao_completa"]
            descricao_reduzida = ["descricao_reduzida"]
            fabricante = ["fabricante"]
            funcao = ["funcao"]
            id_categoria = ["id_categoria"]
            modelo = ["modelo"]
            montagem = ["montagem"]
            status = ["status"]
            tag = ["tag"]
            id_parametros = ["id_parametros"]

            id_equivalencia = ["id_equivalencia"]
            id_historico = ["id_historico"]
            id_ligacoes = ["id_ligacoes"]

            return Produto(id_produto=id_produto, alimentacao=alimentacao, caracteristica=caracteristica,
                           categoria_venda=categoria_venda, certificado=certificado, codigo_pedido=codigo_pedido,
                           descricao_completa=descricao_completa, descricao_reduzida=descricao_reduzida,
                           fabricante=fabricante, funcao=funcao, id_categoria=id_categoria, modelo=modelo,
                           montagem=montagem, status=status, tag=tag, id_parametros=id_parametros,
                           id_equivalencia=id_equivalencia, id_historico=id_historico, id_ligacoes=id_ligacoes)

        except Exception as e:
            print("Problema ao criar novo produto!")
            print(e)
