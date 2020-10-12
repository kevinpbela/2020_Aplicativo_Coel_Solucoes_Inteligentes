package br.com.coel.aplicativo_coel

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_mensagens.*
import kotlinx.android.synthetic.main.navigation_view.*
import kotlinx.android.synthetic.main.toolbar.*

class DescricaoProdutoActivity : DebugActivity () {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_descricao_produto)

        // Captura os dados enviados por outra activity
        var produto = intent.getSerializableExtra("produto")
        Toast.makeText(this, "$produto", Toast.LENGTH_LONG).show()

        this.genericLayoutMenu = layoutMenuLateral
        this.genericMenuLateral = menu_lateral

        setSupportActionBar(toolbar_view)  // Seleciona a toolbar criada no layout
        supportActionBar?.title = getString(R.string.texto_titulo_descricao_produto) // Modo para definir texto do menu
        supportActionBar?.setDisplayHomeAsUpEnabled(true)  // habilita botão de retorno no menu

        configuraMenuLateral()
    }
}