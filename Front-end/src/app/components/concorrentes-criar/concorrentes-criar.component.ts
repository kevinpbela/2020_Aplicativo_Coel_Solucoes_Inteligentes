import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

import { ConcorrenteService } from './../../services/concorrente.service';
import { ModeloAlertaService } from 'src/app/shared/modelo-alerta.service';

@Component({
  selector: 'app-concorrentes-criar',
  templateUrl: './concorrentes-criar.component.html',
  styleUrls: ['./concorrentes-criar.component.css']
})
export class ConcorrentesCriarComponent implements OnInit {

  form: FormGroup
  submitted = false

  constructor(private fb: FormBuilder, private services: ConcorrenteService,
    private modal: ModeloAlertaService, private location: Location) { }

  ngOnInit(): void {
    this.form = this.fb.group({
      codigo_concorrente: [null, [Validators.required]],
      descricao_concorrente: [null, [Validators.required]],
      empresa_concorrente: [null, [Validators.required]],
      observacao_concorrente: [null, [Validators.required]]
    })
  }

  hasError(campo: string) {
    return this.form.get(campo).errors
  }

  onSubmit() {
    this.submitted = true
    if (this.form.valid) {
      console.log(this.form.value)
      this.services.criarConcorrente(this.form.value).subscribe(
        sucesso => {
          this.modal.showAlertSuccess("Sucesso na criação")
          this.location.back()
        },
        erro => this.modal.showAlertDanger("Erro ao criar concorrente"),
        () => console.log("Request OK")
      )

    }

  }

  onCancel() {
    this.submitted = false
    this.location.back()
  }

}
