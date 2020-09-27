import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from 'src/app/components/pages/home/home.component'
import { AboutComponent } from './components/pages/about/about.component';
import { ActorsComponent } from './components/pages/actors/actors.component';
import { AddActorComponent } from './components/pages/add-actor/add-actor.component';
import { UpdateActorComponent } from './components/pages/update-actor/update-actor.component';


const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'about',
    component: AboutComponent
  },
  {
    path: 'actors',
    component: ActorsComponent
  },
  {
    path: 'add-actor',
    component: AddActorComponent
  },
  {
    path: 'update-actor',
    component: UpdateActorComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
