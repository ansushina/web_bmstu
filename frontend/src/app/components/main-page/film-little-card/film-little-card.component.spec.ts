import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FilmLittleCardComponent } from './film-little-card.component';

describe('FilmLittleCardComponent', () => {
  let component: FilmLittleCardComponent;
  let fixture: ComponentFixture<FilmLittleCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FilmLittleCardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FilmLittleCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
