import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import {AuthService} from '../AuthService/auth.service'
import { Observable } from 'rxjs'
import {Movies, Movie} from '../../models/movies'



@Injectable()
export class MoviesService {
  constructor(private http:HttpClient, private auth:AuthService) { }
  httpOptions = {
    headers: new HttpHeaders({
      'content-Type': 'application/json',
      'Authorization': `Bearer ${this.auth.accessToken}`
    })
  }

  

  getMovies():Observable<Movies>{
    return this.http.get<Movies>('http://127.0.0.1:5000/api/movies', this.httpOptions) 
  }

  getMovieById(mid:number):Observable<Movie>{
    return this.http.get<Movie>(`http://127.0.0.1:5000/api/movies/${mid}`) 
  }

  addMovie(movie):Observable<Movie>{
    let data = this.http.post<Movie>(
      'http://127.0.0.1:5000/api/movies',
      movie,
      this.httpOptions
    )
    return data
  }

  updateMovie(movie):Observable<any>{
    let data = this.http.patch<Movies>(
      `http://127.0.0.1:5000/api/actors/${movie.id}`,
      movie,
      this.httpOptions
    )
    return data
  }

  deleteMovie(mid):Observable<any>{
    return this.http.delete(`http://127.0.0.1:5000/api/actors/${mid}`, this.httpOptions)
  }
}
