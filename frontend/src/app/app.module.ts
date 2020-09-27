import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
// import the http module so that we can make calls out to an API
import {HttpClientModule} from '@angular/common/http'
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
    ActorformComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
