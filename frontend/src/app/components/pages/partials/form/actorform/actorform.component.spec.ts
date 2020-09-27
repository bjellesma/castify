import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ActorformComponent } from './actorform.component';

describe('ActorformComponent', () => {
  let component: ActorformComponent;
  let fixture: ComponentFixture<ActorformComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ActorformComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ActorformComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
