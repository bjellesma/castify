import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router'
import { ActorsService } from '../../../services/ActorsService/actors.service'

@Component({
  selector: 'app-actors',
  templateUrl: './actors.component.html',
  styleUrls: ['./actors.component.css']
})
export class ActorsComponent implements OnInit {
  authenticated:boolean
  actors;
  constructor(private actorsService:ActorsService,private router: Router) { }

  ngOnInit(): void {
    this.authenticated = this.actorsService.authenticated
    this.actorsService.getActors().subscribe(data => {
      this.actors = data.actors
    })
  }

    //TODO handle delete better
  deleteActor(aid): void {
    this.actorsService.deleteActor(aid).subscribe(data => {
      this.router.navigate(['/actors']);
    })
  }

}
