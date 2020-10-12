import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModeloAntigoCriarComponent } from './modelo-antigo-criar.component';

describe('ModeloAntigoCriarComponent', () => {
  let component: ModeloAntigoCriarComponent;
  let fixture: ComponentFixture<ModeloAntigoCriarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModeloAntigoCriarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModeloAntigoCriarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
