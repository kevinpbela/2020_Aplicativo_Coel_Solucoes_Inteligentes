import { AutenticacaoGuard } from './conta/shared/autenticacao.guard';
import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CriarContaComponent } from './conta/criar-conta/criar-conta.component';
import { HomeComponent } from './layout/home/home.component';
import { ProdutosComponent } from './layout/produtos/produtos.component';
import { LoginComponent } from './conta/login/login.component';
import { AutenticacaoComponent } from './layout/autenticacao/autenticacao.component';
import { ProdutosFormComponent } from './layout/produtos-form/produtos-form.component';

const routes: Routes = [
  {
    path: '', component: HomeComponent, children: [
      { path: '', component: ProdutosComponent },
      { path: 'novo', component: ProdutosFormComponent },
      { path: 'editar/:id', component: ProdutosFormComponent }
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
