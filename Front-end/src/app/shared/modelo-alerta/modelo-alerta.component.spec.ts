import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModeloAlertaComponent } from './modelo-alerta.component';

describe('ModeloAlertaComponent', () => {
  let component: ModeloAlertaComponent;
  let fixture: ComponentFixture<ModeloAlertaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModeloAlertaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModeloAlertaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
