import { Component, OnInit } from '@angular/core';
import { MoviesService } from 'src/app/services/MoviesService/movies.service';
import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.css']
})
export class MoviesComponent implements OnInit {
  movies;
  constructor(private moviesService:MoviesService,public auth: AuthService) { }

  ngOnInit(): void {
    this.moviesService.getMovies().subscribe(data => {
      this.movies = data.movies
    })
  }

}
