import { ContaService } from './../shared/conta.service';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { Usuario } from '../login/usuario';

@Component({
  selector: 'app-criar-conta',
  templateUrl: './criar-conta.component.html',
  styleUrls: ['./criar-conta.component.css']
})
export class CriarContaComponent implements OnInit {

  criaUsuario: Usuario = new Usuario()

  constructor(private contaService: ContaService, private location: Location) { }

  ngOnInit(): void {
  }

  async onSubmit(){
    try {

      const resultado = await this.contaService.criarConta(this.criaUsuario)
      console.log(resultado)
      this.location.back()

    } catch (error) {
      console.error(error)
    }
  }

}
