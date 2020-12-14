import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Genre} from '../../../models/dto/genre-dto.model';
import {Actor} from '../../../models/dto/actor-dto.model';
import {Country} from '../../../models/dto/country-dto.model';
import {FiltersService} from '../../../services/filters.service';
import {FormControl} from '@angular/forms';

@Component({
  selector: 'app-filters',
  templateUrl: './filters.component.html',
  styleUrls: ['./filters.component.scss']
})
export class FiltersComponent implements OnInit {

  public genres: Genre[];
  public actors: Actor[];
  public countries: Country[];

  @Input() filters = {
    query: null,
    genre: null,
    actor: null,
    country: null,
    yearFrom: null,
    yearTo: null,
  };

  public genresList = new FormControl();
  public actorsList = new FormControl();
  public countriesList = new FormControl();

  @Output() public initSearch: EventEmitter<{
    query: '',
    genre: null,
    actor: null,
    country: null,
    yearFrom: null,
    yearTo: null,
  }> = new EventEmitter<{
    query: '',
    genre: null,
    actor: null,
    country: null,
    yearFrom: null,
    yearTo: null,
  }>();

  onChange(): void {
    console.log(this.genresList);
    this.filters.genre = this.genresList.value || null;
    this.filters.actor = this.actorsList.value || null;
    this.filters.country = this.countriesList.value || null;
    this.initSearch.emit(this.filters);
  }

  constructor(private filtersService: FiltersService) {
  }

  ngOnInit(): void {
    this.filtersService.getGenres().subscribe(
      genres => {
        this.genres = genres;
        this.genresList.setValue(this.filters.genre);
      },
      error => console.log(error),
    );
    this.filtersService.getActors().subscribe(
      actors => {
        this.actors = actors;
        this.actorsList.setValue(this.filters.actor);
      },
      error => console.log(error),
    );
    this.filtersService.getCountries().subscribe(
      countries => {
        this.countries = countries;
        this.countriesList.setValue(this.filters.country);
      },
      error => console.log(error),
    );
  }
}
