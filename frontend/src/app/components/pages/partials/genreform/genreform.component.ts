import { Component, OnInit, Input } from '@angular/core';
import {Router} from '@angular/router'
import { GenresService } from 'src/app/services/GenresService/genres.service';

@Component({
  selector: 'app-genreform',
  templateUrl: './genreform.component.html',
  styleUrls: ['./genreform.component.css']
})
export class GenreformComponent implements OnInit {
  @Input() genre;
  @Input() formType:string;
  //class properties will be bound from the form with ngModel
  genreId:string;
  name:string;

  constructor(private genresService:GenresService,private router: Router) { }

  ngOnInit(): void {
    setTimeout(() => {
      if(this.genre){
        this.genreId = this.genre.id
        this.name = this.genre.name
      }
    }, 200)
  }

  onSubmit(){
    // construct genre object
    const genre = {
      id: this.genreId,
      name: this.name
    }
    // You need to subscribe before any data is returned if you're using an observable
    if(this.formType == "add"){
      this.genresService.addGenre(genre).subscribe(data => {
        this.router.navigate(['/genres']);
      })
    }else if(this.formType == "update"){
      this.genresService.updateGenre(genre)
        .subscribe(data => {
          this.router.navigate(['/genres']);
        }, err => {
          this.router.navigate(['/genres']);
        })
      }
    
  }

}
