import { AutenticacaoGuard } from './conta/shared/autenticacao.guard';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CriarContaComponent } from './conta/criar-conta/criar-conta.component';
import { HomeComponent } from './layout/home/home.component';
import { ProdutosComponent } from './layout/produtos/produtos.component';
import { LoginComponent } from './conta/login/login.component';
import { AutenticacaoComponent } from './layout/autenticacao/autenticacao.component';

const routes: Routes = [
  {
    path: '', component: HomeComponent, children: [
      { path: '', component: ProdutosComponent }
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
