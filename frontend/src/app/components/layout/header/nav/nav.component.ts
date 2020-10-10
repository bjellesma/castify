import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../../../services/AuthService/auth.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {
  authenticated:boolean;

  constructor(public auth: AuthService) {}

  ngOnInit(): void {}

  login(): void {
    // Call this to redirect the user to the login page
    this.auth.login();
  }

  logout(): void {
    // Call this to log the user out of the application
    this.auth.logout();
  }

}
