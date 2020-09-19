import { environment } from './../../../environments/environment.prod';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Usuario } from '../login/usuario';
import { take } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ContaService {

  constructor(private http: HttpClient) { }


  async login(usuario) {

    const resultado = await this.http.get<Usuario[]>(`${environment.api}/usuario`).toPromise()

    // console.log(usuario.nome)
    // console.log(resultado)


    for (let index = 0; index < resultado.length; index++) {
      if (resultado[index]['login'] == usuario.login && resultado[index]['senha'] == usuario.senha) {
        window.localStorage.setItem('token', 'meu token')
        return true
      } 

    }
    return false


  }

  criarConta(criaUsuario) {
    return this.http.post(`${environment.api}/usuario`, criaUsuario).pipe(take(1))
  }

}
