import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import {AuthService} from '../AuthService/auth.service'
import { Observable } from 'rxjs'
import {Movies, Movie} from '../../models/movies'
import { environment } from '../../../environments/environment';


@Injectable()
export class MoviesService {
  authenticated:boolean
  constructor(private http:HttpClient, private auth:AuthService) { 
    this.authenticated = this.auth.authenticated
  }
  httpOptions = {
    headers: new HttpHeaders({
      'content-Type': 'application/json',
      'Authorization': `Bearer ${this.auth.accessToken}`
    })
  }

  

  getMovies():Observable<Movies>{
    return this.http.get<Movies>(`${environment.api_url}/api/movies`, this.httpOptions) 
  }

  getMovieById(mid:number):Observable<Movie>{
    return this.http.get<Movie>(`${environment.api_url}/api/movies/${mid}`, this.httpOptions) 
  }

  addMovie(movie):Observable<Movie>{
    let data = this.http.post<Movie>(
      `${environment.api_url}/api/movies`,
      movie,
      this.httpOptions
    )
    console.log(data)
    return data
  }

  updateMovie(movie):Observable<any>{
    let data = this.http.patch<Movies>(
      `${environment.api_url}/api/movies/${movie.id}`,
      movie,
      this.httpOptions
    )
    return data
  }

  deleteMovie(mid):Observable<any>{
    return this.http.delete(`${environment.api_url}/api/movies/${mid}`, this.httpOptions)
  }
}
