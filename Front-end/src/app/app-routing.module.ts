import { Routes, RouterModule } from '@angular/router';
import { NgModule, Component } from '@angular/core';

import { AutenticacaoGuard } from './shared/autenticacao.guard';

import { ProdutosListarComponent } from './components/produtos-listar/produtos-listar.component';
import { AutenticacaoComponent } from 'src/app/components/autenticacao/autenticacao.component';
import { CriarContaComponent } from 'src/app/components/criar-conta/criar-conta.component';
import { LoginComponent } from 'src/app/components/login/login.component';
import { HomeComponent } from 'src/app/components/home/home.component';
import { ProdutosCriarComponent } from './components/produtos-criar/produtos-criar.component';

const routes: Routes = [
  {
    path: '', component: HomeComponent, children: [
      { path: '', component: ProdutosListarComponent },
      { path: 'novo', component: ProdutosCriarComponent },
      { path: 'editar/:id', component: ProdutosCriarComponent }
    ],
    canActivate: [AutenticacaoGuard]
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
