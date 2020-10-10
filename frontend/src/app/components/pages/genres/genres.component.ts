import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router'
import { GenresService } from 'src/app/services/GenresService/genres.service';

@Component({
  selector: 'app-genres',
  templateUrl: './genres.component.html',
  styleUrls: ['./genres.component.css'],
  providers: [GenresService]
})
export class GenresComponent implements OnInit {
  authenticated:boolean
  genres;
  constructor(private genresService:GenresService,private router: Router) { }
  // TODO use imdb to get a lot of this information
  ngOnInit(): void {
    this.authenticated = this.genresService.authenticated
    this.genresService.getGenres().subscribe(data => {
      this.genres = data.genres
    })
  }

  deleteGenre(gid): void {
    this.genresService.deleteGenre(gid).subscribe(data => {
      this.router.navigate(['/genres']);
    })
  }

}