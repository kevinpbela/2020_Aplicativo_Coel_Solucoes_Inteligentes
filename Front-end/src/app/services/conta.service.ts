import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { take } from 'rxjs/operators';

import { environment } from '../../environments/environment.prod';

@Injectable({
  providedIn: 'root'
})
export class ContaService {

  constructor(private http: HttpClient) { }


  async login(usuario) {

    const resultado = await this.http.get<any[]>(`${environment.api}/usuario`).toPromise()

    for (let index = 0; index < resultado.length; index++) {
      if (resultado[index]['login'] === usuario.login && resultado[index]['senha'] === usuario.senha) {
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
