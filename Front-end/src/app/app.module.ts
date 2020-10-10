import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ModalModule } from 'ngx-bootstrap/modal'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './conta/login/login.component';

import { ProdutosComponent } from './layout/produtos/produtos.component';
import { HomeComponent } from './layout/home/home.component';
import { CriarContaComponent } from './conta/criar-conta/criar-conta.component';
import { AutenticacaoComponent } from './layout/autenticacao/autenticacao.component';
import { ProdutosFormComponent } from './layout/produtos-form/produtos-form.component';
import { SharedModule } from './layout/shared/shared.module'

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    ProdutosComponent,
    HomeComponent,
    CriarContaComponent,
    AutenticacaoComponent,
    ProdutosFormComponent,

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule,
    NgbModule,
    ReactiveFormsModule,
    ModalModule.forRoot(),
    SharedModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
