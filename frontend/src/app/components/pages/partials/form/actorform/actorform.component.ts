import { Component, Input, OnInit } from '@angular/core';
import {Router} from '@angular/router'
import {ActorsService} from '../../../../../services/ActorsService/actors.service'

@Component({
  selector: 'app-actorform',
  templateUrl: './actorform.component.html',
  styleUrls: ['./actorform.component.css']
})
export class ActorformComponent implements OnInit {
  @Input() actor;
  @Input() formType:string;
  //class properties will be bound from the form with ngModel
  actorId:string;
  fullName:string;
  age:number;
  gender:string;

  constructor(private actorsService:ActorsService,private router: Router) { }

  ngOnInit(): void {
    //create timeout to get data of actor
    //todo are we able to return a promise
    setTimeout(() => {
      if(this.actor){
        this.actorId = this.actor.id
        this.fullName = this.actor.name
        this.age = this.actor.age
        this.gender = this.actor.gender
      }
    }, 200)
    
    
  }

  onSubmit(){
    // construct actor object
    const actor = {
      id: this.actorId,
      name: this.fullName,
      gender: this.gender,
      age: this.age
    }
    // You need to subscribe before any data is returned if you're using an observable
    if(this.formType == "add"){
      this.actorsService.addActor(actor).subscribe(data => {
        this.router.navigate(['/actors']);
      })
    }else if(this.formType == "update"){
      this.actorsService.updateActor(actor)
        .subscribe(data => {
          this.router.navigate(['/actors']);
        }, err => {
          //TODO make error response
          this.router.navigate(['/actors']);
        })
      }
    
  }
}
