import { Component, OnInit } from '@angular/core';
import { GenresService } from 'src/app/services/GenresService/genres.service';


@Component({
  selector: 'app-add-genre',
  templateUrl: './add-genre.component.html',
  styleUrls: ['./add-genre.component.css'],
  providers: [GenresService]
})
export class AddGenreComponent implements OnInit {
  formType:string = "add"

  constructor() { }

  ngOnInit(): void {
  }

}
