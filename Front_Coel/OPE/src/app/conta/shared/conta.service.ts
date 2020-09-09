import { environment } from './../../../environments/environment.prod';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Conta } from './../criar-conta/conta';
import { Usuario } from '../login/usuario';

@Injectable({
  providedIn: 'root'
})
export class ContaService {

  constructor(private http: HttpClient) { }

  async login(usuario: Usuario) {

    const resultado = await this.http.get<any>(`${environment.api}/usuario`).toPromise()

    if (resultado && resultado.access_token) {

      window.localStorage.setItem('token', resultado.access_token)
      return true

    }
    return false

  }

  async criarConta(conta: Conta) {

    const resulado = await this.http.post<any>(`${environment.api}/conta`, conta).toPromise()
    return resulado
  }

}
