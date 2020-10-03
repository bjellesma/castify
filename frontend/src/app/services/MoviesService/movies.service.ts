import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable } from 'rxjs'
import {Movies, Movie} from '../../models/movies'

const httpOptions = {
  headers: new HttpHeaders({
    'content-Type': 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class MoviesService {

  constructor(private http:HttpClient) { }

  getMovies():Observable<Movies>{
    return this.http.get<Movies>('http://127.0.0.1:5000/api/movies') 
  }

  getMovieById(mid:number):Observable<Movie>{
    return this.http.get<Movie>(`http://127.0.0.1:5000/api/movies/${mid}`) 
  }

  addMovie(movie):Observable<Movie>{
    let data = this.http.post<Movie>(
      'http://127.0.0.1:5000/api/movies',
      movie,
      httpOptions
    )
    return data
  }

  updateMovie(movie):Observable<any>{
    let data = this.http.patch<Movies>(
      `http://127.0.0.1:5000/api/actors/${movie.id}`,
      movie,
      httpOptions
    )
    return data
  }

  deleteMovie(mid):Observable<any>{
    return this.http.delete(`http://127.0.0.1:5000/api/actors/${mid}`, httpOptions)
  }
}
