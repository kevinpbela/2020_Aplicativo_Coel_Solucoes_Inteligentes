package br.com.coel.aplicativo_coel

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.core.view.GravityCompat
import androidx.recyclerview.widget.DefaultItemAnimator
import androidx.recyclerview.widget.LinearLayoutManager
import com.google.android.material.navigation.NavigationView
import kotlinx.android.synthetic.main.activity_tela_inicial.*
import kotlinx.android.synthetic.main.navigation_view.*
import kotlinx.android.synthetic.main.toolbar.*

class TelaInicialActivity : DebugActivity() {

    // Variavel utilizada pelo RecycleView
    private var produtos = listOf<Produto>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tela_inicial)
        //setContentView(R.layout.toolbar)

        this.genericLayoutMenu = layoutMenuLateral
        this.genericMenuLateral = menu_lateral

        // modo de pegar os dados enviados por outra tela
        //alunoval args = intent.extras
        //val nome_usuario = args?.getString("nome_usuario")
        //Toast.makeText(this, "Usuario: $nome_usuario", Toast.LENGTH_LONG).show()

        // msgTelaInicial.text = nome_usuario
        // modo de pegar os dados enviados por outra tela

        setSupportActionBar(toolbar_view)  // Seleciona a toolbar criada no layout
        supportActionBar?.title = getString(R.string.texto_titulo_menu) // Modo para definir texto do menu
        supportActionBar?.setDisplayHomeAsUpEnabled(true)  // habilita botão de retorno no menu

        configuraMenuLateral()

        // Configurações do RecyclerView criado em activity_tela_inicial.xml
        recyclerProdutos?.layoutManager = LinearLayoutManager(this)
        recyclerProdutos?.itemAnimator = DefaultItemAnimator()
        recyclerProdutos?.setHasFixedSize(true)
    }

    // OnResume utilizado para executar as tarefas após ter criado a tela. Ex: conexão com API
    override fun onResume() {
        super.onResume()
        taskProdutos()  // Fazer a chamada do método
    }

    // Esse método irá criar a lista de produtos, atualizar o adapter, tread para chamar web service
    fun taskProdutos() {
        this.produtos = ProdutoService.getProdutos()  // Método criado em ProdutoService.kt

        recyclerProdutos?.adapter = ProdutoAdapter(this.produtos) {onClickProduto(it)}
    }

    fun onClickProduto(produto: Produto){
        // chamar nova activity
        val intent = Intent(this, DescricaoProdutoActivity::class.java)
        intent.putExtra("produto", produto)

        startActivity(intent)
    }

    // Sobrescrevendo método de criação do menu de opções da tela
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu) // carrega menu criado em "menu_main.xml"
        return super.onCreateOptionsMenu(menu)
    }

    // Sobrescrendo o método para tratar os eventos de click nos botões do menu
    override fun onOptionsItemSelected(item: MenuItem?): Boolean {
        val itemId = item?.itemId // Verifica qual item foi clicado

        if (itemId == R.id.action_buscar) {
            Toast.makeText(this, "Botão Buscar", Toast.LENGTH_LONG).show()
        } else if (itemId == R.id.action_atualizar) {
            Toast.makeText(this, "Botão Atualizar", Toast.LENGTH_LONG).show()
        } else if (itemId == R.id.action_config) {
            Toast.makeText(this, "Botão de Configuração", Toast.LENGTH_LONG).show()
        } else if (itemId == android.R.id.home) {  // Trata click no botão de retorno
            finish()  // Esse metódo destroi a tela atual
        }

        return super.onOptionsItemSelected(item)
    }
}