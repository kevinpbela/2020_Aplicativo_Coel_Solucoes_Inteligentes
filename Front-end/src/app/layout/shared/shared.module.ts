import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ModeloAlertaComponent } from './modelo-alerta/modelo-alerta.component';



@NgModule({
  declarations: [ModeloAlertaComponent],
  exports: [ModeloAlertaComponent],
  imports: [CommonModule],
  entryComponents: [ModeloAlertaComponent]
})
export class SharedModule { }
