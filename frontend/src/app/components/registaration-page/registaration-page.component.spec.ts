import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistarationPageComponent } from './registaration-page.component';

describe('RegistarationPageComponent', () => {
  let component: RegistarationPageComponent;
  let fixture: ComponentFixture<RegistarationPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistarationPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistarationPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
