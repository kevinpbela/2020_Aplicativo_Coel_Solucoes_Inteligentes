import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModeloAntigoListarComponent } from './modelo-antigo-listar.component';

describe('ModeloAntigoListarComponent', () => {
  let component: ModeloAntigoListarComponent;
  let fixture: ComponentFixture<ModeloAntigoListarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModeloAntigoListarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModeloAntigoListarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
