import { ContaService } from './../shared/conta.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

import { Usuario } from './usuario';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ModeloAlertaService } from 'src/app/layout/shared/modelo-alerta.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  // usuario: Usuario = new Usuario();

  form: FormGroup
  submitted = false

  constructor(private fb: FormBuilder, private router: Router,
    private modal: ModeloAlertaService, private contaService: ContaService) { }

  ngOnInit(): void {

    this.form = this.fb.group({
      nome: [null, [Validators.required]],
      senha: [null, [Validators.required]]
    })
  }


  hasError(campo: string) {
    return this.form.get(campo).errors
  }


  async onSubmit() {

    try {

      const resultado = await this.contaService.login(this.form.value)
      // console.log(this.form.value)
      console.log(`login efetudado: ${resultado}`)

      if (resultado == false) {
        this.handleError()
      }

      this.router.navigate([''])

    } catch (error) {
      console.error(error)
    }

  }

  handleError() {

    this.modal.showAlertDanger('Usuario ou senha incorretos')

  }

}
