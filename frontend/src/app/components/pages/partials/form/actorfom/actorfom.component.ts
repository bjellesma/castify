import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router'
import {ActorsService} from '../../../../../services/ActorsService/actors.service'

@Component({
  selector: 'app-actorfom',
  templateUrl: './actorfom.component.html',
  styleUrls: ['./actorfom.component.css']
})
export class ActorfomComponent implements OnInit {

  //class properties will be bound from the form with ngModel
  fullName:string;
  age:number;
  gender:string;

  constructor(private actorsService:ActorsService,private router: Router) { }

  ngOnInit(): void {
  }

  onSubmit(){
    // construct actor object
    const actor = {
      name: this.fullName,
      gender: this.gender,
      age: this.age
    }
    // You need to subscribe before any data is returned if you're using an observable
    this.actorsService.addActor(actor).subscribe(data => {
      this.router.navigate(['/actors']);
    })
  }
}
