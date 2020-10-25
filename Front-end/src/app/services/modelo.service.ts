import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { tap, delay, take } from 'rxjs/operators';

import { Modelo } from 'src/app/models/modelo';

import { environment } from 'src/environments/environment.prod';

@Injectable({
  providedIn: 'root'
})
export class ModelosService {

  constructor(private http: HttpClient) { }

  listarModelos() {
    return this.http.get<Modelo[]>(`${environment.api}/modelo`).pipe(delay(1000), tap(console.log))
  }

  criarModelos(modelo) {
    return this.http.post(`${environment.api}/modelo`, modelo).pipe(take(1))
  }
}