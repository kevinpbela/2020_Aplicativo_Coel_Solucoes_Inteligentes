import { ContaService } from './../shared/conta.service';
import { Conta } from './conta';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

@Component({
  selector: 'app-criar-conta',
  templateUrl: './criar-conta.component.html',
  styleUrls: ['./criar-conta.component.css']
})
export class CriarContaComponent implements OnInit {

  conta: Conta = new Conta()

  constructor(private contaService: ContaService, private location: Location) { }

  ngOnInit(): void {
  }

  async onSubmit(){
    try {

      const resultado = await this.contaService.login(this.conta)
      console.log(resultado)
      this.location.back()

    } catch (error) {
      console.error(error)
    }
  }

}
