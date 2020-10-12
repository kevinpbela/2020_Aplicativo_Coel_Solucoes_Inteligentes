package br.com.coel.aplicativo_coel

// Similar ao exemplo da aula "DisciplinaService"
object ProdutoService {

    // método para criar uma lista simulada para usar como exemplo na criação dos cards
    fun getProdutos():List<Produto> {
        val produtos = mutableListOf<Produto>()
        for (i in 1..10) {
            val p = Produto()
            p.nome = "Produto $i"
            p.foto = "https://www.ascontecnologic.com/images/igallery/resized/1-100/2-34-800-600-80.jpg"

            produtos.add(p)
        }
        return produtos
    }
}