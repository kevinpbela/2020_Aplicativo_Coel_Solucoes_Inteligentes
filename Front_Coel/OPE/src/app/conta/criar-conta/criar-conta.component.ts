import { ContaService } from './../shared/conta.service';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { Usuario } from '../login/usuario';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ModeloAlertaService } from 'src/app/layout/shared/modelo-alerta.service';

@Component({
  selector: 'app-criar-conta',
  templateUrl: './criar-conta.component.html',
  styleUrls: ['./criar-conta.component.css']
})
export class CriarContaComponent implements OnInit {

  form: FormGroup
  submitted = false

  criaUsuario: Usuario = new Usuario()

  constructor(private fb: FormBuilder, private contaService: ContaService,
    private location: Location, private modal: ModeloAlertaService) { }

  ngOnInit(): void {
    this.form = this.fb.group({
      id: [],
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

    }

  }

}
