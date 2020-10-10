import { Component, OnInit } from '@angular/core';

import { empty, Observable, Subject } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { BsModalRef } from 'ngx-bootstrap/modal';

import { Produto } from 'src/app/models/produto';

import { ModeloAlertaService } from 'src/app/shared/modelo-alerta.service';
import { ProdutosService } from 'src/app/services/produtos.service';

@Component({
  selector: 'app-produtos-listar',
  templateUrl: './produtos-listar.component.html',
  styleUrls: ['./produtos-listar.component.css']
})
export class ProdutosListarComponent implements OnInit {

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
