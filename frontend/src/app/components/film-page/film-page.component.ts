import { Component, OnInit } from '@angular/core';
import {Film} from '../../models/dto/film-dto.model';

@Component({
  selector: 'app-film-page',
  templateUrl: './film-page.component.html',
  styleUrls: ['./film-page.component.scss']
})
export class FilmPageComponent implements OnInit {

  public film: Film;

  constructor() { }

  ngOnInit(): void {

  }


}
