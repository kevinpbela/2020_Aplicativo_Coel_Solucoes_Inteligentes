import { Component, OnInit, Input } from '@angular/core';

import { BsModalRef } from 'ngx-bootstrap/modal'

@Component({
  selector: 'app-modelo-alerta',
  templateUrl: './modelo-alerta.component.html',
  styleUrls: ['./modelo-alerta.component.css']
})
export class ModeloAlertaComponent implements OnInit {

  @Input() mensagem: string
  @Input() tipo = "success"

  constructor(public bsModalRef: BsModalRef) { }

  ngOnInit(): void {
  }

  onClose(){
    this.bsModalRef.hide()
  }

}
