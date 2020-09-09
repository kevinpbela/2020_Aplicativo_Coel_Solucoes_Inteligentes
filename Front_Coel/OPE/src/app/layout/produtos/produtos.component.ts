import { Component, OnInit } from '@angular/core';
import { Observable, empty, Subject } from 'rxjs';

import { Produto } from './produto';
import { ProdutosService } from './produtos.service';
import { catchError } from 'rxjs/operators';
import { BsModalRef } from 'ngx-bootstrap/modal';
import { ModeloAlertaService } from '../shared/modelo-alerta.service'

@Component({
  selector: 'app-produtos',
  templateUrl: './produtos.component.html',
  styleUrls: ['./produtos.component.css']
})
export class ProdutosComponent implements OnInit {

  bsModalRef: BsModalRef

  produtos$: Observable<Produto[]>;
  error$ = new Subject<boolean>();


  constructor(private produtosService: ProdutosService, private alertaServico: ModeloAlertaService) { }

  ngOnInit(): void {
    this.produtos$ = this.produtosService.listarProdutos().pipe(catchError(error => {
      console.error(error);
      // this.error$.next(true)
      this.handleError()
      return empty()
    }))

    this.produtosService.listarProdutos().pipe(catchError(error => empty())).subscribe(dados => console.log(dados))

  }

  handleError() {

    this.alertaServico.showAlertDanger('Erro ao carregar os produtos, tente nomamente mais tarde!')

  }

}
