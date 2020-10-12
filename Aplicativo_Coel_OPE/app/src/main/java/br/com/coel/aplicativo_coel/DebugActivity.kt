package br.com.coel.aplicativo_coel

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.core.view.GravityCompat
import androidx.drawerlayout.widget.DrawerLayout
import com.google.android.material.navigation.NavigationView

import kotlinx.android.synthetic.main.toolbar.*

open class DebugActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {

    private val TAG = "CoelApp"
    private val className: String
        get() {
            val s = javaClass.name
            return s.substring(s.lastIndexOf("."))
        }

    var genericLayoutMenu: DrawerLayout? = null
    var genericMenuLateral: NavigationView? = null

    // Configuração do menu lateral
    protected  fun configuraMenuLateral() {
        var toogle = ActionBarDrawerToggle(
            this,
            genericLayoutMenu,
            toolbar_view,
            R.string.nav_drawer_open,  // String para acessebilidade
            R.string.nav_drawer_close  // String para acessebilidade
        )
        genericLayoutMenu?.addDrawerListener(toogle)
        toogle.syncState()
        genericMenuLateral?.setNavigationItemSelectedListener(this)
    }

    // Define ações dos itens do menu lateral
    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.nav_produtos -> {
                val intent = Intent(this, ProdutosActivity::class.java)
                startActivity(intent)
            }
            R.id.nav_mensagns -> {
                val intent = Intent(this, MensagensActivity::class.java)
                startActivity(intent)
            }
            R.id.nav_configuracoes -> {
                val intent = Intent(this, ConfiguracoesActivity::class.java)
                startActivity(intent)
            }
            R.id.nav_forum -> {
                val intent = Intent(this, ForumActivity::class.java)
                startActivity(intent)
            }
            R.id.nav_sair -> {
                onDestroy()
            }
            R.id.nav_home -> {
                val intent = Intent(this, TelaInicialActivity::class.java)
                startActivity(intent)}
        }
        genericLayoutMenu?.closeDrawer(GravityCompat.START)
        return true
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d(TAG, "$className .onCreate chamado")
    }

    override fun onStart() {
        super.onStart()
        Log.d(TAG, "$className .onStart chamado")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d(TAG, "$className .onRestart chamado")
    }

    override fun onResume() {
        super.onResume()
        Log.d(TAG, "$className .onResume chamado")
    }

    override fun onPause() {
        super.onPause()
        Log.d(TAG, "$className .onPause chamado")
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, "$className .onStop chamado")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, "$className .onDestroy chamado")
    }
}