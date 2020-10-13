import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

import { ModeloAlertaService } from 'src/app/shared/modelo-alerta.service';
import { ProdutosService } from 'src/app/services/produtos.service';

@Component({
  selector: 'app-produtos-criar',
  templateUrl: './produtos-criar.component.html',
  styleUrls: ['./produtos-criar.component.css']
})
export class ProdutosCriarComponent implements OnInit {

  form: FormGroup
  submitted = false

  constructor(private fb: FormBuilder, private produtosService: ProdutosService,
    private modal: ModeloAlertaService, private location: Location) { }

  ngOnInit(): void {

    this.form = this.fb.group({

      id_produto: [],
      alimentacao: [null, [Validators.required]],
      caracteristica: [null, [Validators.required]],
      categoria_venda: [null, [Validators.required]],
      certificado: [null, [Validators.required]],
      codigo_pedido: [null, [Validators.required]],
      descricao_completa: [null, [Validators.required]],
      descricao_reduzida: [null, [Validators.required]],
      fabricante: [null, [Validators.required]],
      funcao: [null, [Validators.required]],
      id_categoria: [],
      modelo: [null, [Validators.required]],
      montagem: [null, [Validators.required]],
      status: [null, [Validators.required]],
      tag: [null, [Validators.required]],
      id_parametros: [],
      id_equivalencia: [],
      id_historico: [],
      id_ligacoes: []

    })

  }

  hasError(campo: string) {
    return this.form.get(campo).errors
  }

  onSubmit() {
    this.submitted = true
    console.log(this.form.value)

    if (this.form.valid) {

      console.log("valido")
      this.produtosService.criarProdutos(this.form.value).subscribe(
        sucesso => {
          this.modal.showAlertSuccess("Sucesso na criação")
          this.location.back()
        },
        erros => this.modal.showAlertDanger("Erro ao criar produto"),
        () => console.log("Request OK")
      )

    }

  }

  onCancel() {
    this.submitted = false
    this.location.back()
  }

}
