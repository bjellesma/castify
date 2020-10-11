import { Injectable } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import {
  Router, Resolve,
  ActivatedRouteSnapshot, RouterStateSnapshot
} from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService implements Resolve<any> {

  constructor(public auth: AuthService, private router: Router) { }

  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<any>|Promise<any>|any {

    return this.auth.user$
  }
}
