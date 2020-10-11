import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import {Actors, Actor} from '../../models/actors'
import { Observable } from 'rxjs'
import { AuthService } from '../AuthService/auth.service';
import { environment } from '../../../environments/environment';

const httpOptions = {
  headers: new HttpHeaders({
    'content-Type': 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class ActorsService {
  authenticated:boolean
  constructor(private http:HttpClient, private auth:AuthService) {
    this.authenticated = this.auth.authenticated
  }

  getActors():Observable<Actors>{
    return this.http.get<Actors>(`${environment.api_url}/api/actors`) 
  }

  getActorById(aid:number):Observable<Actor>{
    return this.http.get<Actor>(`${environment.api_url}/api/actors/${aid}`) 
  }

  addActor(actor):Observable<Actors>{
    let data = this.http.post<Actors>(
      `${environment.api_url}/api/actors`,
      actor,
      httpOptions
    )
    return data
  }

  updateActor(actor):Observable<any>{
    let data = this.http.patch<Actors>(
      `${environment.api_url}/api/actors/${actor.id}`,
      actor,
      httpOptions
    )
    console.log(`data: ${JSON.stringify(data)}`)
    return data
  }

  deleteActor(aid):Observable<any>{
    return this.http.delete(`${environment.api_url}/${aid}`, httpOptions)
  }
}
