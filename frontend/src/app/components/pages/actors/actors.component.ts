import { Component, OnInit } from '@angular/core';
import { ActorsService } from '../../../services/ActorsService/actors.service'

@Component({
  selector: 'app-actors',
  templateUrl: './actors.component.html',
  styleUrls: ['./actors.component.css']
})
export class ActorsComponent implements OnInit {
  actors;
  constructor(private actorsService:ActorsService) { }

  ngOnInit(): void {
    this.actorsService.getActors().subscribe(data => {
      this.actors = data.actors
    })
  }

  

}
