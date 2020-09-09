import { Component, OnInit } from '@angular/core';
import { Produto } from './produto'

@Component({
  selector: 'app-produtos',
  templateUrl: './produtos.component.html',
  styleUrls: ['./produtos.component.css']
})
export class ProdutosComponent implements OnInit {

  produto: Produto = new Produto()

  constructor() { }

  ngOnInit(): void {
  }

  savar(){
    console.log(this.produto)
  }

}
