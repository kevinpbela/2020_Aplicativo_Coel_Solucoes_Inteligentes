package br.com.coel.aplicativo_coel

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.ProgressBar
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.squareup.picasso.Picasso

// Similar ao exemplo da aula "DisciplinaAdapter"
class ProdutoAdapter (
    val produtos: List<Produto>,
    val onClick: (Produto) -> Unit // método para capturar o evento de click, e não retorna nada
): RecyclerView.Adapter<ProdutoAdapter.ProdutoViewHolder> () {

    // classe interna que irá comportar todos os elementos da tela
    class ProdutoViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val cardNome: TextView
        val cardImg: ImageView
        val cardProgress: ProgressBar

        init {
            cardNome = view.findViewById((R.id.cardNome))
            cardImg = view.findViewById((R.id.cardImg))
            cardProgress = view.findViewById((R.id.cardProgress))
        }
    }

    // Esse método retorna quandos elementos tem na lista que será criada
    override fun getItemCount() = this.produtos.size

    // Esse método criar a instancia do cardView
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ProdutoViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.adapter_produto, parent, false)

        val holder = ProdutoViewHolder(view)
        return holder
    }

    //Esse método controi o cardView
    override fun onBindViewHolder(holder: ProdutoViewHolder, position: Int) {
        val produto = this.produtos[position]

        holder.cardNome.text = produto.nome
        holder.cardProgress.visibility = View.VISIBLE  // Deixa o progressBar visivel enquanto carrega a imagem

        // Biblioteca "Picasso" importada para tratar as imagens do cardView
        Picasso.with(holder.itemView.context).load(produto.foto).fit().into(holder.cardImg,
            object: com.squareup.picasso.Callback{
                override fun onSuccess() {
                    holder.cardProgress.visibility = View.GONE
                }

                override fun onError() {
                    holder.cardProgress.visibility = View.GONE
                }
            }


        )
        // método para vincular o evento de click
        holder.itemView.setOnClickListener { onClick(produto) }
    }

}