import { environment } from './../../../environments/environment.prod';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Usuario } from '../login/usuario';

@Injectable({
  providedIn: 'root'
})
export class ContaService {

  constructor(private http: HttpClient) { }

  async login(usuario: Usuario) {

    const resultado = await this.http.get<Usuario>(`${environment.api}/usuario`).toPromise()

    if (resultado.nome == usuario.nome && resultado.senha == usuario.senha) {

      window.localStorage.setItem('token', resultado.nome)
      return true

    }
    return false

  }

  async criarConta(criaUsuario: Usuario) {

    const resulado = await this.http.post<any>(`${environment.api}/usuario`, criaUsuario).toPromise()
    return resulado
  }

}
