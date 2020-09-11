import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Location } from '@angular/common';

import { ProdutosService } from '../produtos/produtos.service';
import { ModeloAlertaService } from '../shared/modelo-alerta.service';

@Component({
  selector: 'app-produtos-form',
  templateUrl: './produtos-form.component.html',
  styleUrls: ['./produtos-form.component.css']
})
export class ProdutosFormComponent implements OnInit {

  form: FormGroup
  submitted = false

  constructor(private fb: FormBuilder, private produtosService: ProdutosService,
    private modal: ModeloAlertaService, private location: Location) { }

  ngOnInit(): void {

    this.form = this.fb.group({

      id: [],
      modelo: [null, [Validators.required, Validators.maxLength(5)]],
      funcao: [null, [Validators.required, Validators.minLength(3), Validators.maxLength(20)]],
      descricaoReduzida: [null, [Validators.required, Validators.minLength(3)]],
      categoria: [null, [Validators.required, Validators.minLength(3)]],
      subCategoria1: [null, [Validators.required]],
      subCategoria2: [null, [Validators.required]],
      subCategoria3: [null, [Validators.required]],
      subCategoria4: [null, [Validators.required]],
      aplicacaoNavegacao: [null, [Validators.required, Validators.maxLength(200)]],
      descricao: [null, [Validators.required, Validators.maxLength(200)]],
      caracteristicas: [null, [Validators.required, Validators.maxLength(200)]],
      aplicacoes: [null, [Validators.required, Validators.maxLength(200)]],
      manuais: [null, [Validators.required, Validators.maxLength(200)]],
      categoriaVenda: [null, [Validators.required, Validators.maxLength(200)]],
      fotos: [null]

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
    this.form.reset()
  }


}
