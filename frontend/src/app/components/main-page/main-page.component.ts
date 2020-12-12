import {Component, OnInit} from '@angular/core';
import {Film} from "../../models/dto/film-dto.model";
import {FilmService} from "../../services/film.service";

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss']
})
export class MainPageComponent implements OnInit {

  public mostRatingFilms: Film[];
  public mostCommentedFilms: Film[];

  constructor(private filmService: FilmService) {
  }

  ngOnInit(): void {
    this.filmService.getFilms('rating', 0, 5).subscribe(
      films => this.mostRatingFilms = films,
      err => console.log('Error: ', err)
    );
    this.filmService.getFilms('date', 0, 5).subscribe(
      films => this.mostCommentedFilms = films,
      err => console.log('Error: ', err)
    );
  }
}
