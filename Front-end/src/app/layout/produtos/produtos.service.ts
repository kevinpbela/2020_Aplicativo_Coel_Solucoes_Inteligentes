import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { environment } from './../../../environments/environment';
import { tap, delay, take } from 'rxjs/operators';
import { Produto } from './produto';

@Injectable({
  providedIn: 'root'
})
export class ProdutosService {

  constructor(private http: HttpClient) { }

  listarProdutos() {
    return this.http.get<Produto[]>(`${environment.api}/produto`).pipe(delay(1000), tap(console.log))
  }

  criarProdutos(produto) {
    return this.http.post(`${environment.api}/produto`, produto).pipe(take(1))
  }
}
