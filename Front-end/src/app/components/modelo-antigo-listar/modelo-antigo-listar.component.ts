import { Component, OnInit } from '@angular/core';


import { empty, Observable, Subject } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { BsModalRef } from 'ngx-bootstrap/modal';

import { Modelo } from 'src/app/models/modelo';

import { ModeloAlertaService } from 'src/app/shared/modelo-alerta.service';
import { ModelosService } from 'src/app/services/modelo.service';


@Component({
  selector: 'app-modelo-antigo-listar',
  templateUrl: './modelo-antigo-listar.component.html',
  styleUrls: ['./modelo-antigo-listar.component.css']
})
export class ModeloAntigoListarComponent implements OnInit {

  bsModalRef: BsModalRef

  modelos$: Observable<Modelo[]>;
  error$ = new Subject<boolean>();

  constructor(private modelosService: ModelosService, private alertaServico: ModeloAlertaService) { }

  ngOnInit(): void {
    this.modelos$ = this.modelosService.listarModelos().pipe(catchError(error => {
      console.error(error);
      // this.error$.next(true)
      this.handleError()
      return empty()
    }))

    this.modelosService.listarModelos().pipe(catchError(error => empty())).subscribe(dados => console.log(dados))

  }

  handleError() {

    this.alertaServico.showAlertDanger('Erro ao carregar os modelos, tente nomamente mais tarde!')

  }

}
