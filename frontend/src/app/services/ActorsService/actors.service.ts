import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import {Actors} from '../../models/actors'
import { Observable } from 'rxjs'

const httpOptions = {
  headers: new HttpHeaders({
    'content-Type': 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class ActorsService {

  constructor(private http:HttpClient) { }

  getActors():Observable<Actors>{
    return this.http.get<Actors>('http://127.0.0.1:5000/api/actors') 
  }

  addActor(actor):Observable<Actors>{
    console.log(`data to post ${JSON.stringify(actor)}`)
    let data = this.http.post<Actors>(
      'http://127.0.0.1:5000/api/actors',
      actor
    )
    console.log(`data: ${JSON.stringify(data)}`)
    return data
  }
}
