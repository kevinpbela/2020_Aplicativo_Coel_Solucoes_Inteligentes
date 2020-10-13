import { TestBed } from '@angular/core/testing';

import { ConcorrenteService } from './concorrente.service';

describe('ConcorrenteService', () => {
  let service: ConcorrenteService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ConcorrenteService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
