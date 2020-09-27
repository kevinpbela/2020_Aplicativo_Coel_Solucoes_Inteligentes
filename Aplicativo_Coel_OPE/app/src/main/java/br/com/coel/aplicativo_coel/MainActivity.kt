package br.com.coel.aplicativo_coel

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import android.widget.Toast
import kotlinx.android.synthetic.main.login.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.login)

        loginLogoCoel.setImageResource(R.drawable.logo_coel)
        //loginSaudacao.setText(R.string.mensagem_login)

        botaoLogin.setOnClickListener {
            val valorUsuario = campoUsuario.text.toString()
            val valorSenha = campoSenha.text.toString()
            Toast.makeText(this, "Usuario $valorUsuario; Senha $valorSenha", Toast.LENGTH_LONG).show()
        }

    }
}