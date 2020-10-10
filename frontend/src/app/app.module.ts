import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
// import the http module so that we can make calls out to an API
import { HttpClientModule} from '@angular/common/http';
// Import the HTTP interceptor from the Auth0 Angular SDK
// import forms module
import{FormsModule} from '@angular/forms'
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/layout/header/header.component';
import { AboutComponent } from './components/pages/about/about.component';
import { HomeComponent } from './components/pages/home/home.component';
import { FooterComponent } from './components/layout/footer/footer.component';
import { ActorsComponent } from './components/pages/actors/actors.component';
import { LogoComponent } from './components/layout/header/logo/logo.component';
import { NavComponent } from './components/layout/header/nav/nav.component';
import { AddActorComponent } from './components/pages/add-actor/add-actor.component';
import { UpdateActorComponent } from './components/pages/update-actor/update-actor.component';
import { ActorformComponent } from './components/pages/partials/form/actorform/actorform.component';
import { ProfileComponent } from './components/pages/profile/profile.component';
import { MoviesComponent } from './components/pages/movies/movies.component';
import { GenresComponent } from './components/pages/genres/genres.component';
import { AddMovieComponent } from './components/pages/add-movie/add-movie.component';
import { UpdateMovieComponent } from './components/pages/update-movie/update-movie.component';
import { AddGenreComponent } from './components/pages/add-genre/add-genre.component';
import { UpdateGenreComponent } from './components/pages/update-genre/update-genre.component';
import { MovieformComponent } from './components/pages/partials/form/movieform/movieform.component';
//auth service
import {AuthService} from './services/AuthService/auth.service'

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    AboutComponent,
    HomeComponent,
    FooterComponent,
    ActorsComponent,
    LogoComponent,
    NavComponent,
    AddActorComponent,
    UpdateActorComponent,
    ActorformComponent,
    ProfileComponent,
    MoviesComponent,
    GenresComponent,
    AddMovieComponent,
    UpdateMovieComponent,
    AddGenreComponent,
    UpdateGenreComponent,
    MovieformComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    AuthService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
