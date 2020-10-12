package br.com.coel.aplicativo_coel

import java.io.Serializable

//Similar ao exemplo da aula "class Disciplina"
class Produto: Serializable {
    
    var id: Long = 0
    var nome = ""

    var foto = ""

    override fun toString(): String {
        return "Produto(nome=$nome)"
    }
}