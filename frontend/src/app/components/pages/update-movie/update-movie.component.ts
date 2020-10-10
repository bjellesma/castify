import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MoviesService } from 'src/app/services/MoviesService/movies.service';

@Component({
  selector: 'app-update-movie',
  templateUrl: './update-movie.component.html',
  styleUrls: ['./update-movie.component.css'],
  providers: [MoviesService]
})
export class UpdateMovieComponent implements OnInit {
  movie;
  movieId:string;
  // Specify the type of form so that we know how to handle it
  formType:string = "update"

  constructor(private moviesService:MoviesService,private route: ActivatedRoute) { }

  ngOnInit(): void {
    // Get query params
    this.route.queryParamMap.subscribe(params => {
      this.movieId = params.get("movie_id")
    })
    // get movie by id so that we can pass this to the movieform
    this.moviesService.getMovieById(parseInt(this.movieId)).subscribe(data => {
      this.movie = data.movie;
    })
    
  }

}