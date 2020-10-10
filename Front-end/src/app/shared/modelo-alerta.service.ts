import { Injectable } from '@angular/core';

import { BsModalService, BsModalRef } from 'ngx-bootstrap/modal';

import { ModeloAlertaComponent } from './modelo-alerta/modelo-alerta.component';

export enum TiposAlertas {
  DANGER = 'danger',
  SUCCESS = 'success'

}

@Injectable({
  providedIn: 'root'
})
export class ModeloAlertaService {

  constructor(private modalService: BsModalService) { }

  private showAlert(mensagem: string, tipo: string, dismissTimeout?: number) {

    const bsModalRef: BsModalRef = this.modalService.show(ModeloAlertaComponent)
    bsModalRef.content.tipo = tipo
    bsModalRef.content.mensagem = mensagem

    if (dismissTimeout) {
      setTimeout(() => bsModalRef.hide(), dismissTimeout)
    }

  }

  showAlertDanger(mensagem: string) {

    this.showAlert(mensagem, TiposAlertas.DANGER)

  }

  showAlertSuccess(mensagem: string) {

    this.showAlert(mensagem, TiposAlertas.SUCCESS, 3000)

  }
}
