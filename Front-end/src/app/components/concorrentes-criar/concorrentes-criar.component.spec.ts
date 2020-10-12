import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ConcorrentesCriarComponent } from './concorrentes-criar.component';

describe('ConcorrentesCriarComponent', () => {
  let component: ConcorrentesCriarComponent;
  let fixture: ComponentFixture<ConcorrentesCriarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConcorrentesCriarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConcorrentesCriarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
