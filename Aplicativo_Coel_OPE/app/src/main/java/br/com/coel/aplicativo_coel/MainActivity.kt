package br.com.coel.aplicativo_coel

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import android.widget.Toast
import kotlinx.android.synthetic.main.login.*

class MainActivity : DebugActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.login)

        loginLogoCoel.setImageResource(R.drawable.logo_coel)
        //loginSaudacao.setText(R.string.mensagem_login)

        botaoLogin.setOnClickListener {
            val valorUsuario = campoUsuario.text.toString()
            val valorSenha = campoSenha.text.toString()
            // Toast.makeText(this, "Usuario $valorUsuario; Senha $valorSenha", Toast.LENGTH_LONG).show()



            //Validação do login
            Thread {
                // chama api de login enviando como parametro usuario e senha
                var retornoLogin = true // alterar para false para ativar a validação do login
                val usuario = "aluno"
                val senha = "impacta"

                // verificação de usuario cadastrado
                if (valorUsuario.equals(usuario,false)) {
                    if (valorSenha.equals(senha,false)) {
                        retornoLogin = true
                    }
                }
                runOnUiThread {
                    // depois que retorna da thread
                    if (retornoLogin) {
                        val intent = Intent(this, TelaInicialActivity::class.java) // Navega para TelaInicialActivity

                        startActivity(intent)
                    }
                    else {
                        Toast.makeText(this, "Login Inválido", Toast.LENGTH_LONG).show()
                    }
                }
            }.start()

            /*
            val intent = Intent(this, TelaInicialActivity::class.java) // Navega para TelaInicialActivity

            //modo de enviar parametros para outra tela
            val params = Bundle()
            params.putString("nome_usuario", valorUsuario)
            params.putInt("numero", 10)
            intent.putExtras(params)
            //modo de enviar parametros para outra tela
             */

            startActivity(intent)

        }

    }
}