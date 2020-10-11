import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { GenresService } from 'src/app/services/GenresService/genres.service';

@Component({
  selector: 'app-update-genre',
  templateUrl: './update-genre.component.html',
  styleUrls: ['./update-genre.component.css'],
  providers: [GenresService]
})
export class UpdateGenreComponent implements OnInit {
  genre;
  genreId:string;
  // Specify the type of form so that we know how to handle it
  formType:string = "update"

  constructor(private genresService:GenresService,private route: ActivatedRoute) { }

  ngOnInit(): void {
    // Get query params
    this.route.queryParamMap.subscribe(params => {
      this.genreId = params.get("genre_id")
    })
    // get genre by id so that we can pass this to the genreform
    this.genresService.getGenreById(parseInt(this.genreId)).subscribe(data => {
      this.genre = data.genre;
    })
    
  }

}