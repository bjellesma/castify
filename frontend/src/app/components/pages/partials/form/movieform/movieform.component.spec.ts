import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MoviesformComponent } from './moviesform.component';

describe('MoviesformComponent', () => {
  let component: MoviesformComponent;
  let fixture: ComponentFixture<MoviesformComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MoviesformComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MoviesformComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
