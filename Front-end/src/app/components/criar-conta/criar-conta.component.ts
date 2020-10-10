import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

import { ModeloAlertaService } from 'src/app/shared/modelo-alerta.service';
import { ContaService } from 'src/app/services/conta.service';

@Component({
  selector: 'app-criar-conta',
  templateUrl: './criar-conta.component.html',
  styleUrls: ['./criar-conta.component.css']
})
export class CriarContaComponent implements OnInit {

  form: FormGroup
  submitted = false

  constructor(private fb: FormBuilder, private contaService: ContaService,
    private location: Location, private modal: ModeloAlertaService) { }

  ngOnInit(): void {

    this.form = this.fb.group({
      id: [] = "1",
      email:[null, [Validators.required]],
      login: [null, [Validators.required]],
      nome: [null, [Validators.required]],
      senha: [null, [Validators.required]]
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
      this.contaService.criarConta(this.form.value).subscribe(
        sucesso => {
          this.modal.showAlertSuccess("Sucesso na criação")
          this.location.back()
        },
        erros => this.modal.showAlertDanger("Erro ao criar usuario"),
        () => console.log("Request OK")
      )
      this.location.back()
      this.modal.showAlertSuccess("Sucesso na criação")
    }

  }

}
