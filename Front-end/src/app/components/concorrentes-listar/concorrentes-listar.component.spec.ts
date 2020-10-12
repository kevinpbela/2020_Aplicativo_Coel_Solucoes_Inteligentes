import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ConcorrentesListarComponent } from './concorrentes-listar.component';

describe('ConcorrentesListarComponent', () => {
  let component: ConcorrentesListarComponent;
  let fixture: ComponentFixture<ConcorrentesListarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ConcorrentesListarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ConcorrentesListarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
