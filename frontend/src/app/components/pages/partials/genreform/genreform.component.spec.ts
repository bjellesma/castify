import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GenreformComponent } from './genreform.component';

describe('GenreformComponent', () => {
  let component: GenreformComponent;
  let fixture: ComponentFixture<GenreformComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GenreformComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GenreformComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
