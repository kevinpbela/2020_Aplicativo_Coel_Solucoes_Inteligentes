import { Routes, RouterModule } from '@angular/router';
import { NgModule, Component } from '@angular/core';

import { AutenticacaoGuard } from './shared/autenticacao.guard';

import { ModeloAntigoListarComponent } from './components/modelo-antigo-listar/modelo-antigo-listar.component';
import { ModeloAntigoCriarComponent } from './components/modelo-antigo-criar/modelo-antigo-criar.component';

import { ConcorrentesListarComponent } from './components/concorrentes-listar/concorrentes-listar.component';
import { ProdutosListarComponent } from './components/produtos-listar/produtos-listar.component';
import { AutenticacaoComponent } from 'src/app/components/autenticacao/autenticacao.component';
import { ProdutosCriarComponent } from './components/produtos-criar/produtos-criar.component';
import { CriarContaComponent } from 'src/app/components/criar-conta/criar-conta.component';
import { LoginComponent } from 'src/app/components/login/login.component';
import { HomeComponent } from 'src/app/components/home/home.component';
import { ConcorrentesCriarComponent } from './components/concorrentes-criar/concorrentes-criar.component';

const routes: Routes = [
  {
    path: '', component: HomeComponent, children: [
      { path: '', component: ProdutosListarComponent },
      { path: 'novo_produto', component: ProdutosCriarComponent },
      { path: 'editar/:id', component: ProdutosCriarComponent },
      { path: 'concorrente', component: ConcorrentesListarComponent },
      { path: 'novo_concorrente', component: ConcorrentesCriarComponent },
      { path: 'editar/:id', component: ConcorrentesCriarComponent },
      { path: 'modelo_antigo', component: ModeloAntigoListarComponent },
      { path: 'novo_modelo', component: ModeloAntigoCriarComponent }
    ],
    // canActivate: [AutenticacaoGuard]
  },
  {
    path: '', component: AutenticacaoComponent, children: [
      { path: '', redirectTo: 'login', pathMatch: 'full' },
      { path: 'login', component: LoginComponent },
      { path: 'nova-conta', component: CriarContaComponent }
    ]
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
