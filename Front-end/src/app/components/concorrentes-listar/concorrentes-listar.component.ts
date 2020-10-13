import { catchError } from 'rxjs/operators';
import { ConcorrenteService } from './../../services/concorrente.service';
import { Observable, Subject, empty } from 'rxjs';
import { Component, OnInit } from '@angular/core';

import { BsModalRef } from 'ngx-bootstrap/modal';

import { Concorrente } from 'src/app/models/concorrente';
import { ModeloAlertaService } from 'src/app/shared/modelo-alerta.service';

@Component({
  selector: 'app-concorrentes-listar',
  templateUrl: './concorrentes-listar.component.html',
  styleUrls: ['./concorrentes-listar.component.css']
})
export class ConcorrentesListarComponent implements OnInit {

  bsModalRef: BsModalRef
  
  concorrentes$: Observable<Concorrente[]>
  error$ = new Subject<boolean>();

  constructor(private service: ConcorrenteService, private alerta: ModeloAlertaService) { }

  ngOnInit(): void {
    this.concorrentes$ = this.service.listarConcorrente().pipe(catchError(error => {
      console.error(error)
      this.handleError()
      return empty
    }))
  }

  handleError() {

    this.alerta.showAlertDanger('Erro ao carregar os Concorrentes, tente nomamente mais tarde!')

  }


}
