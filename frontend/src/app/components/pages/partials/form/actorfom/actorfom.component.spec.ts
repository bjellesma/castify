import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ActorfomComponent } from './actorfom.component';

describe('ActorfomComponent', () => {
  let component: ActorfomComponent;
  let fixture: ComponentFixture<ActorfomComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ActorfomComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ActorfomComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
