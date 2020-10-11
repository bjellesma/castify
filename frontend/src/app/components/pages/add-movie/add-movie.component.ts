import { Component, OnInit } from '@angular/core';
import { MoviesService } from 'src/app/services/MoviesService/movies.service';

@Component({
  selector: 'app-add-movie',
  templateUrl: './add-movie.component.html',
  styleUrls: ['./add-movie.component.css'],
  providers: [MoviesService]
})
export class AddMovieComponent implements OnInit {
  formType:string = "add"

  constructor() { }

  ngOnInit(): void {
  }

}
