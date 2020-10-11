import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ActorsService } from 'src/app/services/ActorsService/actors.service';

@Component({
  selector: 'app-update-actor',
  templateUrl: './update-actor.component.html',
  styleUrls: ['./update-actor.component.css']
})
export class UpdateActorComponent implements OnInit {
  actor;
  actorId:string;
  // Specify the type of form so that we know how to handle it
  formType:string = "update"

  constructor(private actorsService:ActorsService,private route: ActivatedRoute) { }

  ngOnInit(): void {
    // Get query params
    this.route.queryParamMap.subscribe(params => {
      this.actorId = params.get("actor_id")
    })
    // get actor by id so that we can pass this to the actorform
    this.actorsService.getActorById(parseInt(this.actorId)).subscribe(data => {
      this.actor = data.actor;
    })
    
  }

}
