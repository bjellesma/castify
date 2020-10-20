import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import {AuthService} from '../AuthService/auth.service'
import { Observable } from 'rxjs'
import {Genres, Genre} from '../../models/genres'
import { environment } from '../../../environments/environment';


@Injectable()
export class GenresService {
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

  

  getGenres():Observable<Genres>{
    return this.http.get<Genres>(`${environment.api_url}/api/genres`, this.httpOptions) 
  }

  getGenreById(gid:number):Observable<Genre>{
    return this.http.get<Genre>(`${environment.api_url}/api/genres/${gid}`, this.httpOptions) 
  }

  addGenre(genre):Observable<Genre>{
    let data = this.http.post<Genre>(
      `${environment.api_url}/api/genres`,
      genre,
      this.httpOptions
    )
    return data
  }

  updateGenre(genre):Observable<any>{
    let data = this.http.patch<Genres>(
      `${environment.api_url}/api/genres/${genre.id}`,
      genre,
      this.httpOptions
    )
    return data
  }

  deleteGenre(gid):Observable<any>{
    return this.http.delete(`${environment.api_url}/api/genres/${gid}`, this.httpOptions)
  }
}
