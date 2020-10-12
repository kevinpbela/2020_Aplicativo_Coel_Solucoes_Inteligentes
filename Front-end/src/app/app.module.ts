import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ModalModule } from 'ngx-bootstrap/modal'

import { AppRoutingModule } from './app-routing.module';
import { SharedModule } from './shared/shared.module';

import { AutenticacaoComponent } from 'src/app/components/autenticacao/autenticacao.component';
import { CriarContaComponent } from 'src/app/components/criar-conta/criar-conta.component';
import { LoginComponent } from 'src/app/components/login/login.component';
import { HomeComponent } from 'src/app/components/home/home.component';
import { AppComponent } from './app.component';
import { ProdutosListarComponent } from './components/produtos-listar/produtos-listar.component';
import { ProdutosCriarComponent } from './components/produtos-criar/produtos-criar.component';
import { ConcorrentesListarComponent } from './components/concorrentes-listar/concorrentes-listar.component';
import { ConcorrentesCriarComponent } from './components/concorrentes-criar/concorrentes-criar.component';
import { ModeloAntigoListarComponent } from './components/modelo-antigo-listar/modelo-antigo-listar.component';
import { ModeloAntigoCriarComponent } from './components/modelo-antigo-criar/modelo-antigo-criar.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    CriarContaComponent,
    AutenticacaoComponent,
    ProdutosListarComponent,
    ProdutosCriarComponent,
    ConcorrentesListarComponent,
    ConcorrentesCriarComponent,
    ModeloAntigoListarComponent,
    ModeloAntigoCriarComponent,

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
