import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {FilmService} from '../../services/film.service';
import {Film} from '../../models/dto/film-dto.model';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.scss']
})
export class SearchPageComponent implements OnInit {

  public params = {
    query: '',
    genre: null,
    actor: null,
    country: null,
    yearFrom: null,
    yearTo: null,
  };

  public films: Film[];
  public error;
  public offset = 0;
  public moreFlag = false;

  constructor(private route: ActivatedRoute, private router: Router, private filmService: FilmService) {
    this.route.queryParamMap
      .subscribe(params => {
        this.params.query = params.get('query');
        this.params.genre = params.getAll('genre').length > 0 ? params.getAll('genre') : null;
        this.params.actor = params.getAll('actor').length > 0 ? params.getAll('actor') : null;
        this.params.country = params.getAll('country').length > 0 ? params.getAll('country') : null;
        this.params.yearTo = +params.get('yearTo') || null;
        this.params.yearFrom = +params.get('yearFrom') || null;
        console.log(params);
      });
  }

  doSearch(params = {
    query: '',
    genre: null,
    actor: null,
    country: null,
    yearFrom: null,
    yearTo: null,
  }): void {
    this.params = params;
    this.router.navigate(['/search'], {queryParams: params});
    this.filmService.getFilms('date', this.offset, 10, params).subscribe(
      films => {
        this.films = this.films && this.moreFlag ? this.films.concat(films) : films;
        this.moreFlag = false;
      },
      error => this.error = error
    );
  }

  onMore(): void {
    this.offset += 10;
    this.doSearch(this.params);
    this.moreFlag = true;
  }

  ngOnInit(): void {
    console.log(this.params);
    this.doSearch(this.params);
  }

}
