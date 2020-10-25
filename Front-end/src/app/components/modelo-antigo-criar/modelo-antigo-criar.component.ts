import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

import { ModeloAlertaService } from 'src/app/shared/modelo-alerta.service';
import { ModelosService } from 'src/app/services/modelo.service';


@Component({
  selector: 'app-modelo-antigo-criar',
  templateUrl: './modelo-antigo-criar.component.html',
  styleUrls: ['./modelo-antigo-criar.component.css']
})
export class ModeloAntigoCriarComponent implements OnInit {

  form: FormGroup
  submitted = false

  constructor(private fb: FormBuilder, private modelosService: ModelosService,
    private modal: ModeloAlertaService, private location: Location) { }

  ngOnInit(): void {

    this.form = this.fb.group({

     id_modelo_antigo: [],
      descricao_modelo_antigo: [null, [Validators.required]],
      modelo_antigo: [null, [Validators.required]],
      observacao_modelo_antigo: [null, [Validators.required]],
      id_foto: []

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
      this.modelosService.criarModelos(this.form.value).subscribe(
        sucesso => {
          this.modal.showAlertSuccess("Sucesso na criação")
          this.location.back()
        },
        erros => this.modal.showAlertDanger("Erro ao criar modelo"),
        () => console.log("Request OK")
      )

    }

  }

  onCancel() {
    this.submitted = false
    this.location.back()
  }

}
