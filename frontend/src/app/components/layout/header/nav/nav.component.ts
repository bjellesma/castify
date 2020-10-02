import { Component, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {
  user = null
  authenticated

  constructor(public auth: AuthService) {}

  ngOnInit(): void {
    this.auth.user$.subscribe(data => {
      this.user = data
    })
  }

  login(): void {
    // Call this to redirect the user to the login page
    this.auth.loginWithRedirect();
  }

  logout(): void {
    // Call this to log the user out of the application
    this.auth.logout({ returnTo: window.location.origin });
  }

}
