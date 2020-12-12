import { Component, OnInit } from '@angular/core';
import {Genre} from "../../../models/dto/genre-dto.model";
import {Actor} from "../../../models/dto/actor-dto.model";
import {Country} from "../../../models/dto/country-dto.model";
import {FilmService} from "../../../services/film.service";
import {FiltersService} from "../../../services/filters.service";

@Component({
  selector: 'app-filters',
  templateUrl: './filters.component.html',
  styleUrls: ['./filters.component.scss']
})
export class FiltersComponent implements OnInit {

  public genres: Genre[];
  public actors: Actor[];
  public countries: Country[];

  constructor(private filtersService: FiltersService) { }

  ngOnInit(): void {
    this.filtersService.getGenres().subscribe(
      genres => this.genres = genres,
      error => console.log(error),
    );
    this.filtersService.getActors().subscribe(
      actors => this.actors = actors,
      error => console.log(error),
    );
    this.filtersService.getCountries().subscribe(
      countries => this.countries = countries,
      error => console.log(error),
    );
  }
}
