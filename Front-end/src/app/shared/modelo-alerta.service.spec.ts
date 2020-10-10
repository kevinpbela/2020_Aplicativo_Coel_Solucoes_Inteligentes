import { TestBed } from '@angular/core/testing';

import { ModeloAlertaService } from './modelo-alerta.service';

describe('ModeloAlertaService', () => {
  let service: ModeloAlertaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ModeloAlertaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
