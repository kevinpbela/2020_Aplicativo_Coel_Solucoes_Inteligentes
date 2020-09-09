import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms'; 
import { HttpClientModule } from '@angular/common/http';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './conta/login/login.component';

import { ProdutosComponent } from './layout/produtos/produtos.component';
import { HomeComponent } from './layout/home/home.component';
import { CriarContaComponent } from './conta/criar-conta/criar-conta.component';
import { AutenticacaoComponent } from './layout/autenticacao/autenticacao.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    ProdutosComponent,
    HomeComponent,
    CriarContaComponent,
    AutenticacaoComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule,
    NgbModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
