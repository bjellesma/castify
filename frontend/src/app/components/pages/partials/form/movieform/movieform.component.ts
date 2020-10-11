import { Component, OnInit, Input } from '@angular/core';
import {Router} from '@angular/router'
import { MoviesService } from 'src/app/services/MoviesService/movies.service';

@Component({
  selector: 'app-movieform',
  templateUrl: './movieform.component.html',
  styleUrls: ['./movieform.component.css']
})
export class MovieformComponent implements OnInit {
  @Input() movie;
  @Input() formType:string;
  //class properties will be bound from the form with ngModel
  movieId:string;
  title:string;

  constructor(private moviesService:MoviesService,private router: Router) { }

  ngOnInit(): void {
    setTimeout(() => {
      if(this.movie){
        this.movieId = this.movie.id
        this.title = this.movie.title
      }
    }, 200)
  }

  onSubmit(){
    // construct movie object
    const movie = {
      id: this.movieId,
      title: this.title
    }
    // You need to subscribe before any data is returned if you're using an observable
    if(this.formType == "add"){
      this.moviesService.addMovie(movie).subscribe(data => {
        this.router.navigate(['/movies']);
      })
    }else if(this.formType == "update"){
      this.moviesService.updateMovie(movie)
        .subscribe(data => {
          this.router.navigate(['/movies']);
        }, err => {
          this.router.navigate(['/movies']);
        })
      }
    
  }

}
