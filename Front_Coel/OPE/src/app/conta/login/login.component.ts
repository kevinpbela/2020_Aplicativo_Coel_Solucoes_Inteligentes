import { ContaService } from './../shared/conta.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

import { Usuario } from './usuario';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  usuario: Usuario = new Usuario();


  constructor(private router: Router, private contaService: ContaService) { }

  ngOnInit(): void {
  }

  async onSubmit() {

    try {

      const resultado = await this.contaService.login(this.usuario)
      console.log(`login efetudado: ${resultado}`)

      this.router.navigate([''])

    } catch (error) {
      console.error(error)
    }
    
  }

}
