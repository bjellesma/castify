import { Component, OnInit } from '@angular/core';
import { MoviesService } from 'src/app/services/MoviesService/movies.service';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.css'],
  providers: [MoviesService]
})
export class MoviesComponent implements OnInit {
  movies;
  constructor(private moviesService:MoviesService) { }

  ngOnInit(): void {
    this.moviesService.getMovies().subscribe(data => {
      this.movies = data.movies
    })
  }

}
