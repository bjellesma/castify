import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router'
import { MoviesService } from 'src/app/services/MoviesService/movies.service';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.css'],
  providers: [MoviesService]
})
export class MoviesComponent implements OnInit {
  authenticated:boolean
  movies;
  constructor(private moviesService:MoviesService,private router: Router) { }
  // TODO use imdb to get a lot of this information
  ngOnInit(): void {
    this.authenticated = this.moviesService.authenticated
    this.moviesService.getMovies().subscribe(data => {
      this.movies = data.movies
    })
  }

  deleteMovie(mid): void {
    this.moviesService.deleteMovie(mid).subscribe(data => {
      this.router.navigate(['/movies']);
    })
  }

}
